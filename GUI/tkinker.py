import tkinter
top = tkinter.Tk()

# Code to add widgets will go here...
top.mainloop()

import tkinter as tk
class App(tk.Tk):
   def __init__(self):
      super().__init__()

app = App()
app.mainloop()

from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry("100x100")


def show():
    num = askinteger("Input", "Input an Integer")
    print(num)


B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()