from tkinter import *
from datetime import datetime
root = Tk()
root.title('Digital Clock')
root.minsize(520, 100)

font_1 = 'Cursed Timer ULiL', 72
font_2 = 'Cursed Timer ULiL', 48

time_str = StringVar()
sec_str = StringVar()
time_str.set('00:00')
sec_str.set("00")

time_label = Label(textvariable=time_str, font=font_1)
sec_label = Label(textvariable=sec_str, font=font_2)
time_label.grid(row=0, column=0, sticky='S')
sec_label.grid(row=0, column=1, sticky='S')

def update():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    time_str.set('{:02d}:{:02d}'.format(hour, minute))
    sec_str.set('{:02d}'.format(second))
    root.after(1000, update)

update()
mainloop()
