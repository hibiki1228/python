import sqlite3

# データベースに接続 --- (*1)
conn = sqlite3.connect("ejdict.sqlite3")
c = conn.cursor()
# SQLでデータを10件取り出す --- (*2)
sql = 'SELECT * FROM items LIMIT 10'
rows = c.execute(sql)
# 取り出した10件を一つずつ表示 --- (*3)
for n in rows:
    print(n)