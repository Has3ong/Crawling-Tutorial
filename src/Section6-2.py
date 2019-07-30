import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
executable = BASE_DIR + "/chromedriver"

browser = webdriver.Chrome(options=options, executable_path=executable)
browser.get('http://prod.danawa.com/list/?cate=11317599&15main_11_03')

WebDriverWait(browser, 5) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="searchAttributeValue132506"]'))).click()

WebDriverWait(browser, 5) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="searchAttributeValueRep177798"]'))).click()

soup = BeautifulSoup(browser.page_source, "html.parser")
productList = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

for product in productList:
    if not product.find('div', class_='ad_header'):
        print(product.select('p.prod_name > a')[0].text.strip())
        print(product.select('p.price_sect > a')[0].text.strip())

browser.quit()
