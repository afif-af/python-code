from tkinter.simpledialog import askfloat
from tkinter import *

top = Tk()

top.geometry("100x100")


def show():
    num = askfloat("Input", "Input a floating point number")
    print(num)


B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()