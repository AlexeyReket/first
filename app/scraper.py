import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.ChromeOptions()
# options.add_argument('headless')  # для открытия headless-браузера
browser = webdriver.Chrome(chrome_options=options)

url = 'https://www.grsu.by/e-raspisanie/student.html'
browser.get(url)
# Поиск тегов по имени

Faculty_chosen = browser.find_element_by_xpath("//div[@title_id='ddlFaculty_chosen']")
Faculty_chosen.click()
"""login = browser.find_element_by_id("username")

log_but = browser.find_element_by_xpath("//button[@class='btn waves-effect waves-light blue darken-2']")
log_but.click()
url += "/my/"
browser.get(url)
btn = browser.find_element_by_id("schedule")
btn.click()
time.sleep(10)
table = browser.find_element_by_xpath("//ul[@role='tablist']")

print(table.get_attribute("text"))
browser.close()
"""