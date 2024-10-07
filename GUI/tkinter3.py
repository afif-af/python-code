from tkinter.filedialog import askopenfile
from tkinter import *

top = Tk()

top.geometry("100x100")


def show():
    filename = askopenfile()
    print(filename)


B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()