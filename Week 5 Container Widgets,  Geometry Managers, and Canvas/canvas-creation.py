import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")
frame = tk.Frame()
frame.pack()
canvas = tk.Canvas(frame, width=500, height=400, background='gray75')
canvas.pack()

root.mainloop()
