# Selenium_Basic_1

#### Install Selenium

```
> pip3 install selenium

> http://chromedriver.chromium.org/downloads
> download chrome webdriver

> selenium = 3.141.0 
> ChromeDriver = 75.0.3770.140
```

<img width=600 src="https://user-images.githubusercontent.com/44635266/62006583-582ec800-b17d-11e9-8ad3-a3c82c4e68cd.png">

#### Capture WebSite

```
> Section6-1.py
import os
from selenium import webdriver

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

executable = BASE_DIR + "/chromedriver"

browser = webdriver.Chrome(executable_path=executable)
browser.implicitly_wait(2)
browser.set_window_size(1920, 1280)

browser.get('https://www.naver.com')
browser.save_screenshot(BASE_DIR + "/6-1/Test1.png")
browser.get('https://www.daum.net')
browser.get_screenshot_as_file(BASE_DIR + "/6-1/Test2.png")

browser.quit()
```


#### Control WebSite

<img width=600 src="https://user-images.githubusercontent.com/44635266/62007116-bdd28280-b184-11e9-9d22-92e8c0ddb19d.png">

* Copy Xpath

```
> Section6-2.py

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
```