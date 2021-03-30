import time
import tkinter as tk
import tkinter.ttk as ttk

class Ball:
    def __init__(self, canvas, size, color, speed):
        self.canvas = canvas
        self.size = size
        self.id = canvas.create_oval(0, 0, size, size, fill=color)
        self.speed = speed
        self._coro = self
    def move(self, x, y):
        self.canvas.moveto(self.id, x-self.size/2, y-self.size/2)
    def update(self):
        next(self._coro)

    def animate(self):
        while True:
            for x in range(100,200):
                self.move(x, 100)
                yield
            for y in range(100,200):
                self.move(200,y)
                yield
            for x in range(200,100,-1):
                self.move(x,200)
                yield
            for y in range(200,100,-1):
                self.move(100,y)
                yield


class App(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="news")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.create_widgets()
        self.is_animating = False

    def create_widgets(self):
        self.canvas = tk.Canvas(self, borderwidth=0,
                                highlightthickness=0, bg="yellow")
        self.canvas.grid(row=0, column=0, columnspan=2,
                         sticky="news", padx=10, pady=10)
        self.btn_animate = ttk.Button(self, text="Animate",
                                      command=self.toggle_animation)
        self.btn_animate.grid(row=1, column=0, pady=10)
        ttk.Button(self, text="Quit", command=root.destroy).grid(
            row=1, column=1, pady=10)

    def toggle_animation(self):
        self.is_animating = not self.is_animating
        if self.is_animating:
            self.btn_animate.config(text="Stop")
            self.animate()
        else:
            self.btn_animate.config(text="Animate")

    def animate(self):
        # put animation update code here
        #   :

        # schedule the next update
        if self.is_animating:
            self.after(33, self.animate)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Basic Animation")
    root.geometry("300x300")
    app = App(root)
    root.mainloop()
