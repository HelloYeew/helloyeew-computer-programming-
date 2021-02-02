import tkinter as tk
import tkinter.ttk as ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My First App in OOP")
        self.geometry("300x200")
        label1 = ttk.Label(text="My first label")
        label1.pack()
app = Application()
app.mainloop()