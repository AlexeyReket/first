import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('headless')  # для открытия headless-браузера
browser = webdriver.Chrome(chrome_options=options)

url = 'https://www.yandex.by'
browser.get(url)
Faculty_chosen = browser.find_element_by_xpath("//div//form//div//input[@id='text']")
Faculty_chosen.send_keys("Танос")
search = browser.find_element_by_xpath("//button[@role='button']")
search.click()

"""url = "https://www.grsu.by/e-raspisanie/student.html"
browser.get(url)
browser.find_element_by_xpath("//input[@id='username']/following-sibling:input[1]")
"""