import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")
frame = tk.Frame()
frame.pack()
canvas = tk.Canvas(frame, width=500, height=400, background='gray75')
canvas.pack()

canvas.create_rectangle(100, 100, 200, 200,
                        width=2, fill="lightblue")

canvas.create_oval(120, 120, 140, 150,
                   width=3, fill="lightgray", outline="green")

canvas.create_oval(160, 120, 180, 150,
                   width=3, fill="lightgray", outline="green")

canvas.create_line(120, 175, 180, 175,
                   width=10, fill="brown")

canvas.create_text(150, 210, text='Hello, World!',
                   anchor='n', fill='red', font=("Arial", 30))

root.mainloop()
