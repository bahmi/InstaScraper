from selenium import webdriver
from time import sleep
import json

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
        self.main_url = 'https://instagram.com'
        self.driver.get((self.main_url)) # opens the url
        sleep(2)
        self.log_in()
        sleep(2)
        self.close_dialog_box()
        sleep(2)
        self.open_target_profile()
        sleep(3)
        self.scroll_down()
        sleep(2)

        self.driver.close()

    def log_in(self):
        """
        logs into instagram by typing the credentials into the input form
        """
        login_button = self.driver.find_element_by_xpath("//span[@id='react-root']//p[@class='izU2O']/a")
        sleep(1)
        login_button.click()
        sleep(2)
        username_input = self.driver.find_element_by_xpath("//input[@name='username']")
        sleep(1)
        username_input.send_keys(self.username) # inputs data into the form
        sleep(1)
        password_input = self.driver.find_element_by_xpath("//input[@name='password']")
        sleep(2)
        password_input.send_keys(self.password)
        sleep(1)
        password_input.submit() # submits the form

    def close_dialog_box(self):
        """
        closes the dialog box that pops up after log in
        """
        try:
            sleep(1)
            close_dialog = self.driver.find_element_by_xpath("//div[@class='mt3GC']/button[@class='aOOlW   HoLwm ']")
            sleep(1)
            close_dialog.click()
            sleep(1)
        except:
            pass

    def open_target_profile(self):
        """
        types the target username into the search bar and
        opens the profile
        """
        search_bar = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        sleep(2)
        search_bar.send_keys(self.target_username)
        target_profile_url = self.main_url + '/' + self.target_username + '/'
        sleep(1)
        self.driver.get(target_profile_url)

    def scroll_down(self):
        """
        scrolls down in the target profile to load all the images available
        """
        sleep(1)
        no_of_posts = self.driver.find_element_by_xpath("//span[@class='g47SY ']") # finds the number of posts
        no_of_posts = str(no_of_posts.text).replace(',', '')
        self.no_of_posts = int(no_of_posts)
        if self.no_of_posts > 12:
            no_of_scrolls = int(self.no_of_posts/12) + 2 # calculate the number of times to scroll

            for value in range(no_of_scrolls):
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # scrolls down
                sleep(2)


if __name__ == '__main__':
    app = App() # creates an App instance
