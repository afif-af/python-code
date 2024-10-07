from tkinter import *
from tkinter import ttk

top = Tk()
top.geometry("200x150")

frame = Frame(top)
frame.pack()

langs = ["C", "C++", "Java",
         "Python", "PHP"]

Combo = ttk.Combobox(frame, values=langs)
Combo.set("Pick an Option")
Combo.pack(padx=5, pady=5)
top.mainloop()