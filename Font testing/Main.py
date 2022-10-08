from tkinter import *
import random

window = Tk()
window.title('Font Testing')
window.geometry('600x600')
def change_family(event):
    font_size.focus()
    return ('break')

def change_size(event):
    label.config(font=(f'{font_family.get()}',int(font_size.get())))
    label_.config(font=(f'{font_family.get()}',int(font_size.get())))
    if int(font_size.get()) > 25:
        label_.config(font=(f'{font_family.get()}',int(font_size.get())))
        label_.config(text='ABCDEFGHIJKLM\nNOPQRSTUVWXYZ')
    else:
        label_.config(text='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    font_family.focus()

font_family_label = Label(window, text='Font name:', font=("Times new roman", 14))
font_family_label.place(x=35, y=18)

font_size_label = Label(window, text='Font size:', font=("Times new roman", 14))
font_size_label.place(x=170, y=75)

font_family = Entry(window, font=('Courier', 20), relief=SOLID)
font_family.bind("<Return>", change_family)
font_family.pack(pady=15)

font_size = Entry(window, font=('Calibri', 20), width=5,relief=SOLID)
font_size.bind("<Return>", change_size)
font_size.pack()

label = Label(window, text='Example text')
label.pack(pady=(50,0))

label_ = Label(window, text='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
label_.pack()

window.mainloop()






























