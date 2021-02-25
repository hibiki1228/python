import sqlite3

 # データベースに接続
 conn = sqlite3.connect("ejdict.sqlite3")
 c = conn.cursor()

 # SQLでデータを取り出して表示
 sql = 'SELECT * FROM sqlite_master'
 rows = c.execute(sql)
 for n in rows:
     print(n[4])