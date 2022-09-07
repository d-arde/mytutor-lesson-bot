import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
import os
import time
#check imports

# Base url
base_url = 'https://www.mytutor.co.uk/tutors/secure/opportunities.html'

chrome_options = webdriver.ChromeOptions()
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}


driver = webdriver.Chrome(executable_path=r'C:\\vscode\\webdriver\\chromedriver') 
#download webdriver - change path accordingly

#recurring slots
for i in range(10):#10 is temporary solution
    driver.get(base_url) #open mytutor
    lesson_button = driver.find_element(By.LINK_TEXT, 'View') #get button element of lesson
    lesson_button.click() #press accept button

    for i in range(10):
        r = driver.find_element(By.LINK_TEXT, 'Accept') #finds button that says accept
        r.click() #clicks button/element


# time.sleep(5)


# driver.find_element(By.LINK_TEXT,'Store details').click()

# time.sleep(10)

# c = driver.find_element(By.XPATH,'//*[@id="schema-location"]/script')



