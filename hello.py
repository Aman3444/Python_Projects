# print("Hello World")

from tkinter import ttk

from ttkthemes import ThemedTk

root = ThemedTk(theme="radiance")

root.geometry("380x180")
font = "Helvetica 18 bold"

l = ttk.Label(root, text="this is label", font=font)
b = ttk.Button(root, text="Button")
e = ttk.Entry(root, font=font)
r = ttk.Radiobutton(root, text="Radio")

e.place(x=40, y=5)
b.place(x=100, y=50)
l.place(x=90, y=100)
r.place(x=120, y=150)

root.mainloop()
