# Tkinterのライブラリを取り込む --- (*1)
import tkinter as tk

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("Hello, World!") # タイトル
win.geometry("400x300") # サイズ

# ウィンドウを動かす --- (*3)
win.mainloop()
