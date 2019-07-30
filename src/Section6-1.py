import os
from selenium import webdriver

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

executable = BASE_DIR + "/chromedriver"

browser = webdriver.Chrome(executable_path=executable)
browser.implicitly_wait(2)

browser.get('https://www.naver.com')
browser.save_screenshot(BASE_DIR + "/6-1/Test1.png")
browser.get('https://www.daum.net')

element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')
element.send_keys('라이언')
element.submit()

browser.get_screenshot_as_file(BASE_DIR + "/6-1/Test2.png")

browser.quit()
