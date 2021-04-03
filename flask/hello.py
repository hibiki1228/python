from flask import Flask

#flaskオブジェクトの生成
app = Flask(__name__)

#ルート（ / ）へのアクセスがあったときの処理を記述
@app.route("/")
def root():
    return "Hello"

#サーバーを起動
if __name__=="__main__":
    app.run(debug=True, port=8888)