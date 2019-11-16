from bs4 import BeautifulSoup
from selenium import webdriver

from time import sleep
from random import randint
import json
import os
import requests
import shutil

# load environment variables
with open('config.json','r') as f:
    config = json.load(f)


class App:
    def __init__(self, username=config['user']['username'], password=config['user']['password'],
                 target_username=config['user']['target_username'], path=config['user']['path']):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.path = path
        self.driver = webdriver.Chrome() # creates an instance of Chrome
        self.error = False
        self.main_url = 'https://instagram.com'
        self.driver.get((self.main_url)) # opens the url
        sleep(randint(1,3))
        self.log_in()
        sleep(randint(1, 3))
        if self.error is False:
            self.close_dialog_box()
            sleep(randint(1, 2))
            self.open_target_profile()
            sleep(randint(1, 3))
        if self.error is False: # to prevent from scrolling the news feed
            self.scroll_down()
            sleep(randint(1, 3))
        if self.error is False:
            if not os.path.exists(path): # create a directory if it doesn't exist
                os.mkdir(path)
            self.download_photos()

        self.driver.close()

    def log_in(self):
        """
        logs into instagram by typing the credentials into the input form
        """
        try:
            login_button = self.driver.find_element_by_xpath("//span[@id='react-root']//p[@class='izU2O']/a")
            sleep(randint(1, 3))
            login_button.click()
            sleep(randint(1, 3))
            try:
                username_input = self.driver.find_element_by_xpath("//input[@name='username']")
                sleep(randint(1, 3))
                username_input.send_keys(self.username) # inputs data into the form
                sleep(randint(1, 3))
            except Exception:
                self.error = True
                print('Couldn\'t find the username input field')
            try:
                password_input = self.driver.find_element_by_xpath("//input[@name='password']")
                sleep(randint(1, 3))
                password_input.send_keys(self.password)
                sleep(randint(1, 3))
                password_input.submit() # submits the form
            except Exception:
                self.error = True
                print('Couldn\'t find the password input field')
        except Exception:
            self.error = True
            print('Unable to locate the login button')

    def close_dialog_box(self):
        """
        closes the dialog box that pops up after log in
        """
        try:
            sleep(randint(1, 2))
            close_dialog = self.driver.find_element_by_xpath("//div[@class='mt3GC']/button[@class='aOOlW   HoLwm ']")
            sleep(randint(1, 2))
            close_dialog.click()
            sleep(randint(1, 2))
        except:
            pass

    def open_target_profile(self):
        """
        types the target username into the search bar and
        opens the profile
        """
        try:
            search_bar = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
            sleep(randint(1, 3))
            search_bar.send_keys(self.target_username)
            target_profile_url = self.main_url + '/' + self.target_username + '/'
            sleep(randint(1, 3))
            self.driver.get(target_profile_url)
        except Exception:
            self.error = True
            print('Couldn\'t find the search bar')

    def scroll_down(self):
        """
        scrolls down in the target profile to load all the images available
        """
        try:
            no_of_posts = self.driver.find_element_by_xpath("//span[@class='g47SY ']") # finds the number of posts
            no_of_posts = str(no_of_posts.text).replace(',', '')
            self.no_of_posts = int(no_of_posts)
            if self.no_of_posts > 12:
                no_of_scrolls = int(self.no_of_posts/12) + 2 # calculate the number of times to scroll
                try:
                    for value in range(no_of_scrolls):
                        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # scrolls down
                        sleep(randint(3, 4))
                except Exception:
                    self.error = True
                    print('Error occured while scrolling down')
            sleep(randint(3, 4))
        except Exception:
            self.error = True
            print('Couldn\'t find number of posts while scrolling')

    def download_photos(self):
        """
        download images from the target profile
        """
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        all_images = soup.find_all('img')
        print('number of photos: ', len(all_images))

        for index, image in enumerate(all_images):
            file_name = 'image_' + str(index) + '.jpg'
            image_path = os.path.join(self.path, file_name) # create image path
            link = image['src']
            print('Downloading image #' + str(index))
            try:
                response = requests.get(link, stream=True)  # get the image
                with open(image_path, 'wb') as file:
                    shutil.copyfileobj(response.raw, file) # save image to storage device
            except requests.exceptions.MissingSchema:
                print('Couldn\'t download image #' + str(index))
                print('image link: ' + str(link))


if __name__ == '__main__':
    app = App() # creates an App instance
