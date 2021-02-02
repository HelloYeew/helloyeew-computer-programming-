import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Event Demonstration")
root.geometry("500x200")

# lbl = ttk.Label(text="Starting...", font=("Arial",36))
# # make the label fill the container and also expand when the container is resized
# lbl.pack(fill=tk.BOTH, expand=1)
# lbl.bind("<Leave>", lambda e: lbl.config(text="Moved mouse outside"))
# lbl.bind("<Enter>", lambda e: lbl.config(text="Moved mouse inside"))
# lbl.bind("<ButtonPress-1>", lambda e: lbl.config(text="Clicked left mouse button"))
# lbl.bind("<Double-1>", lambda e: lbl.config(text="Double clicked"))
# root.bind("<Return>", lambda e: lbl.config(text="Enter key is pressed"))
# root.bind("<Key-F1>", lambda e: lbl.config(text="Key F1 is pressed"))
# root.bind("<KeyRelease-F1>", lambda e: lbl.config(text="Key F1 is released"))

def onclick():
    btn.config(text="Wait for 2 seconds", state=tk.DISABLED)
    btn.after(2000, lambda: btn.config(text="Done", state=tk.NORMAL))

btn = ttk.Button(text="Start", command=onclick)
btn.pack()

root.mainloop()