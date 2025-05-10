import requests
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest
from urllib.request import urlopen
import re
from urllib.parse import urljoin
import pandas as pd
import itertools
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

main_url = input("Please enter the product's URL from epay: ")

options = webdriver.ChromeOptions()
options.add_argument('--headless')  
driver = webdriver.Chrome(options=options)

driver.get(main_url)
time.sleep(3)
html = driver.page_source
url_soup = BeautifulSoup(html, "lxml")
text_url = url_soup.get_text()

# driver = webdriver.Chrome(options=options)

# href = url_soup.find("a" , class_="fdbk-detail-list__tabbed-btn fake-btn fake-btn--large fake-btn--secondary")

# # html = requests.get(href['href'])
# driver.get(href['href'])
# time.sleep(5)
# html=driver.page_source





# url_soup = BeautifulSoup(html.text, "lxml")
# text_url = url_soup.get_text()



# print(href['href'])
# main_div = url_soup.find("div",id="s0-1-20-13-tabpanel-0")
# print(main_div)
divs = url_soup.find_all("div", class_="fdbk-container__details__comment")
print('Connected Successfully.++++++++++++')

arr = []
for div in divs:
    print(div.get_text())
    arr.append(div.get_text())
    print('-------appended successfully-----------')
    
    
    
df=pd.DataFrame(arr)
df.to_csv("bahy.csv",index=False)
