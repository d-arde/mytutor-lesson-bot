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


driver = webdriver.Chrome(executable_path='/Users/dani/vscode/chromedriver') 
#download webdriver - change path accordingly

#recurring slots

driver.get(base_url) #open mytutor

time.sleep(1)

lesson_button = driver.find_element(By.XPATH, '//*[@id="recurringslotstable:0:view"]') #get button element of lesson
lesson_button.click() #press accept button

time.sleep(0.2)

r = driver.find_element(By.XPATH, '//*[@id="recurringslotdetailsform:acceptRecurringSlot"]/span') #finds button that says accept
r.click() #clicks button/element





