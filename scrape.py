from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import time 
import pandas as pd 


driver = webdriver.Chrome('PATH_TO_SELENIUM')
driver.get('URL_TO_scrape')
driver.maximize_window()

email = driver.find_element_by_xpath('//*[@id="login_username"]')
email.send_keys('USERNAME')
time.sleep(3)

password = driver.find_element_by_xpath('//*[@id="login_password"]')
password.send_keys('PASSWORD')
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="layout"]/div[2]/div/form/div[7]/button')
login.click()
time.sleep(3)

joblook = driver.find_element_by_xpath('//*[@id="search-box-el"]')
joblook.send_keys('SEO')

time.sleep(3)

button = driver.find_element_by_xpath('//*[@id="js-basic-search-form"]/div/label/span/span[1]')
button.click()

time.sleep(5)

elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    print (elem.get_attribute("href"))


time.sleep(3)

driver.quit()
