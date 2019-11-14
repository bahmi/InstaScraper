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
        self.log_in() # logs into instagram

        sleep(2)
        self.driver.close()

    def log_in(self):
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

if __name__ == '__main__':
    app = App() # creates an App instance
