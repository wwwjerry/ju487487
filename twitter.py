from selenium import webdriver
from bs4 import BeautifulSoup
browser = webdriver.Chrome('chromedriver.exe')
url = 'https://twitter.com/login'
browser.get(url)
userName = browser.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input')
userName.send_keys('0905380430')
pwd = browser.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
pwd.send_keys('ju487487')
loginbotton=browser.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > div.clearfix > button')
loginbotton.click()
time.sleep(5)
tweetbox = browser.find_element_by_css_selector('#react-root > div > div > div > header > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-jw8lkh.r-e7q0ms > a > div')
tweetbox.click()
tweetbox.send_keys('')