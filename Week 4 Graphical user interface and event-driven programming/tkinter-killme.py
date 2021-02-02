import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Event Demonstration")
        self.geometry("500x200")
        self.style = ttk.Style()
        self.style.configure(".", font=("Arial", 24))
        self.text = tk.StringVar()
        self.lbl = ttk.Label(textvariable=self.text)
        self.lbl.pack()
        self.btn = ttk.Button(text="Destroy Me!", command=self.start)
        self.btn.pack()

    def start(self):
        self.counter = 5
        self.after(1000, self.countdown)

    def countdown(self):
        self.counter -= 1
        if self.counter == 0:
            self.destroy()
        self.text.set("This app will destroy itself in {} seconds".format(self.counter))
        self.after(1000, self.countdown)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
