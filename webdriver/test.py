import selenium
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

driver.get('https://kujirahand.com/sample/dummy-card/post.php?mml_id=1')
driver.get_cookies()