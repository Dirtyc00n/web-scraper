import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
import os
import pathlib


nav = webdriver.ChromeOptions()
option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')
option.add_argument('--disable-extencions')
pwdchromedrive = pathlib.Path(__file__).parent.absolute()
pwdchromedrive = str(pwdchromedrive) + str('\chromedriver.exe')
driver = webdriver.Chrome(pwdchromedrive, chrome_options=option)
driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(1)
driver.get('https://mercadolibre.cl')
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.nav-search-input'))).send_keys('teclado')
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.nav-icon-search'))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/aside/section/div[12]/ul/li[6]/a')))
url = driver.find_element_by_xpath('/html/body/main/div/div/aside/section/div[12]/ul/li[6]/a').get_attribute("href")
driver.get(url)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/section/ol')))
html_list = driver.find_element_by_css_selector("ol.ui-search-layout.ui-search-layout--stack")
items = html_list.find_elements_by_tag_name("li")
for item in items:
    text = item.get_attribute('innerHTML')
    soup = BeautifulSoup(text, 'html.parser')
    title = soup.findAll("h2")[0].string
    print(title)
    price = soup.select("span.price-tag-fraction")[0].text
    print(price)
    for url in soup.select("a.ui-search-item__group__element.ui-search-link"):
        print(url.get('href'))
    print('*'*5)
