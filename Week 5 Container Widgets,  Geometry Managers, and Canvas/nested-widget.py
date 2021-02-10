import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Container Example")
style = ttk.Style()
style.configure(".", font=("Arial", 24))
top = ttk.Frame(name="top", borderwidth=5, padding=5, relief="ridge")
bottom = ttk.Frame(name="bottom", borderwidth=5, padding=5, relief="ridge")
inner = ttk.Frame(bottom, name="inner", borderwidth=5, padding=5, relief="ridge")
ttk.Label(top, name="label1", text="Label 1: Inside top frame").pack()
ttk.Label(top, name="label2", text="Label 2: Inside top frame").pack()
ttk.Label(bottom, name="label3", text="Label 3: Inside bottom frame").pack()
ttk.Label(inner, name="label4", text="Label 4: Inside inner frame").pack()
btn_quit = ttk.Button(name="quit", text="Quit", command=root.destroy)
top.pack(fill=tk.BOTH)
bottom.pack(fill=tk.BOTH)
inner.pack(fill=tk.BOTH)
btn_quit.pack()


def dump_widget(widget, indent=0):
    print((" "*indent) + str(widget))
    for w in widget.winfo_children():
        dump_widget(w, indent+2)


dump_widget(root)
root.mainloop()
