import tkinter as tk
import tkinter.ttk as ttk

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("Title")
        self.master.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        for i in range(1, 11):
            ttk.Button(self, text=f"ボタン{i}", command=self.show_message(i)).pack()

    def show_message(self, index):
        def inner():
            print(f"ボタン{index}がクリックされました")
        return inner

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()