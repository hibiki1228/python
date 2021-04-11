from flask import *

app = Flask(__name__)

#ルート( / )へアクセスがあった時 --- (*1)
@app.route("/")
def root():
    #HTMLでWebフォームを記述 --- (*2)
    return """
    <html><body>
    <form action="/add" method="post">
        <input type="text" name="a"> +
        <input type="text" name="b">
        <input type="submit" value="計算">
    </form>

    <form action="/mainus" method="post">
        <input type="text" name="a"> -
        <input type="text" name="b">
        <input type="submit" value="計算">
    </form>
    
    <form action="/addadd" method="post">
        <input type="text" name="a"> ×
        <input type="text" name="b">
        <input type="submit" value="計算">
    </form>
    
    <form action="/decre" method="post">
        <input type="text" name="a"> ÷
        <input type="text" name="b">
        <input type="submit" value="計算">
    </form>
    """


#フォームの値を受け取って結果を表示 --- (*3)
@app.route("/add", methods=["post"])
def add():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a + b
    return "<h1>答えは…" + str(r) + "</h1>"

@app.route("/mainus", methods=["post"])
def mainus():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a - b
    return "<h1>答えは…" + str(r) + "</h1>"
@app.route("/addadd", methods=["post"])
def addadd():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a * b
    return "<h1>答えは…" + str(r) + "</h1>"
@app.route("/decre", methods=["post"])
def decre():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a / b
    return "<h1>答えは…" + str(r) + "</h1>"


#サーバーを起動
if __name__=="__main__":
    app.run(debug=True, port=8888)
