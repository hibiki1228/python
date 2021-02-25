import time
from selenium import webdriver

# Chromeを起動する --- (*1)
path = r"C:\Users\hibiki\Anaconda3\Lib\site-packages\chromedriver_binary\chromedriver.exe"
driver = webdriver.Chrome(path)
# Googleのページを開く --- (*2)
driver.get('https://www.google.com')
# ページが開くまで待つ --- (*3)
time.sleep(5) 
# 検索ボックスのオブジェクトを得る --- (*4)
q = driver.find_element_by_name('q')
# 検索ボックスにキーを送信する --- (*5)
q.send_keys('ゼロからはじめるPython')
# フォームを投稿する --- (*6)
q.submit()
# 結果を30秒表示して終了する --- (*7)
time.sleep(30)
driver.quit()