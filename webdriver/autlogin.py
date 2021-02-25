import time, os
from selenium import webdriver
import chromedriver_binary

user_id = "aubn8560"
password = "Hibiki1228"

driver = webdriver.Chrome()

driver.get('https://ict-t.el.kyutech.ac.jp/')
time.sleep(3)

tag = driver.find_element_by_link_text('ログイン')
tag.click()

# ログインするお
u = driver.find_element_by_name('j_username')
u.send_keys(user_id)

p = driver.find_element_by_name('j_password')
p.send_keys(password)

tag = driver.find_element_by_name('_eventId_proceed')
tag.click()
time.sleep(3)

# コースに飛ぶお
tag = driver.find_element_by_name('_eventId_proceed')
tag.click()