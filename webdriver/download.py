import time, os, requests
from selenium import webdriver
import chromedriver_binary

# パスワードの指定
user_id = "test"
password = "pwpw"
download_dir = os.path.dirname(__file__)

# 保存先などオプションを指定してChromeを起動 --- (*1)
opt = webdriver.ChromeOptions()
opt.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
})
driver = webdriver.Chrome(options=opt)

# カード会社のページを開く
driver.get('https://kujirahand.com/sample/dummy-card/')
time.sleep(3) # ページが開くまで待つ

# ログインページを開く --- (*2)
tag = driver.find_element_by_link_text('ログイン')
tag.click()

# ログイン画面のユーザー名にキーを送信 --- (*3)
u = driver.find_element_by_name('username_mmlbbs6')
u.send_keys(user_id)
# ログイン画面のパスワードにキーを送信
p = driver.find_element_by_name('password_mmlbbs6')
p.send_keys(password)
p.submit()
time.sleep(3) # ページが開くまで待つ

# 今月の明細のページを開く
tag = driver.find_element_by_link_text('今月の明細')
tag.click()

# データのダウンロードリンク先を取得 --- (*4)
tag = driver.find_element_by_link_text('*ダウンロード*')
href = tag.get_attribute('href')

# Chromeからクッキーデータを得る --- (*5)
c = {}
print(driver.get_cookies())
for cookie in driver.get_cookies():
    c[cookie['name']] = cookie['value']
# requestsを利用してデータのダウンロード --- (*6)
r = requests.get(href, cookies=c)
with open("data.csv", 'wb') as f:
    f.write(r.content)

print(c)
# 結果を30秒表示して終了する
time.sleep(30)
driver.quit()