# InstaScraper
A python scraper that lets user download given instagram profile's photos. 

## Prerequisities
You need to have [Python (3.7+)](https://www.python.org/downloads/) and [ChromeDriver](https://chromedriver.chromium.org/) 
installed to run this project

## Setup
- clone this repository
```
git clone https://github.com/bahmi/InstaScraper.git
```
-  After cloning the repo, go to its root directory and run the following command to install required packages
```
pip install -r requirements.txt
```
- Once the packages are installed, create a config file `config.json` at the root directory and fill it out with your 
credentials. You don't want to put sensitive information like password or secret key out in the wild. :-)
```
{
  "user": {
    "username": "your_username",
    "password": "your_password",
    "target_username": "your_target_username",
    "path": "/path/to/save/images"
  }
}
```
- Finally, to run the project simply do 
```
python insta_scraper.py
```

## How It Works
When we run the scraper, it creates an instance of Chrome. After that, it opens the url of instagram. Then it locates 
the login button and clicks on it to go to the next page. It inputs the given username and password then submits the form.
Sometimes a dialog box pops up after login, it closes that. Then, it input the target username into the search bar. 
After the username is retrieved, it opens the target profile and gets the number of posts to calculate how many times it 
has to scroll down as it's a dynamically rendered page. Once all the images has been loaded it grabs the page source and extracts
the image urls from it. Finally, it gets the images and saves them in the storage device.  

## Challenges Encountered
Although, I had worked with BeautifulSoup before, I didn't have any experience with Selenium Webdriver prior to this project. 
I've struggled my way through learning to use Selenium. Now that I'm familiar with it, I sort of like it. 
There were instances when Webdriver wouldn't login to Instagram. It couldn't locate the login button. I thought 
the script had bugs. I checked multiple times only to figure out that it can't do everything instantaneously while 
surfing, instagram blocks it. As a newbie, I didn't know that I had to put `sleep()` every once in a while to humanize the program!  
Additionally, learning xPath was another challenging aspect. I read couple of blogs, watched few YouTube videos to learn xPath. 
Couldn't get it initially. Later, I found out that Chrome has build-in functionality to copy xPath! It's fun to play with new technologies.  
Futhermore, scrolling down a profile seemed like a daunting task. I had no clue of doing it. So, I looked up on Google and 
few StackOverflow articles showed up. Once I read through them, it didn't seem that much difficult.  
Last but not the least, the issue I'm encountering currently is, the scraper can't download all the images. It only does
a handful of images. The issue is that image tags disappear once the page is scrolled down. Working on it to fix the issue. 

## Things I Learned
The most valuable thing that I learned from this project was my way around Selenium. I worked with Selenium for the 
first time while doing this project. I also acquired the knowledge of how to login to websites using Selenium Webdriver. 
Oh, and I taught myself xPath as well. It seems to be much faster than other alternatives, such as CSS Selectors. 

## Built With
- [Python](https://www.python.org/) - Scraping Language
- [pip](https://pypi.org/project/pip/) - Package Manager
- [PyCharm](https://www.jetbrains.com/pycharm/) - IDE
- [Selenium](https://www.seleniumhq.org/) - Browser Automation
- [JSON](https://www.json.org/) - To configure Environment Variables
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - For parsing HTML and XML documents

## To Do
- Extract profile info such as number of followers and following
- Capture the captions and AI generated photo descriptions
- Make it compatible with downloading all the images and videos for any profile and hash tags
