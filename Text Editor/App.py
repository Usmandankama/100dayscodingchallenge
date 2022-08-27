# text editor with four menus
# file, edit, about, help
# file ~~ open,save,quit
# edit ~~ cut,paste,copy
# about ~~ messagebox.showinfo
# help ~~ not available at the moment
from textwrap import fill
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
# functions
def main():
    saved = False
    return saved
main()
def Open():
    file_name = filedialog.askopenfilename(filetypes=(('text files','*.txt'),('All files','*.*')))
    window.title(os.path.basename(file_name))
    with open(file_name, 'r') as teXt:
        text_area.delete(1.0,END)
        text_area.insert(1.0, teXt.read())
def New():
    text_area.delete(1.0,END)
    window.title('Untitled.txt')


def Save():
    file_name = filedialog.asksaveasfilename(filetypes=(('Text documents','*.txt'),('Python files',"*.py")))
    window.title(os.path.basename(file_name))
    with open(file_name, 'w') as fiLe:
        fiLe.write(text_area.get(1.0,END))
def Quit():
    question=messagebox.askyesno(message= 'Are you sure you want to leave without saving?', title='Save file')
    if question == True:
        quit
    else:
        pass
def Cut():
    text_area.event_generate("<<Cut>>")
def Copy():
    text_area.event_generate("<<Copy>>")
def Paste():
    text_area.event_generate("<<Paste>>")
def Help():
    messagebox.showerror(message = 'Tab not ready at the moment.',title = 'Not available!')

# window related 
window = Tk();window.geometry('600x450');window.title('*Untitled.py - SLS')
# VARIABLES
# window_icon = PhotoImage('C:\\Users\\SALISU\\Documents\\Workspace\\Projects\\one.jpg');window.iconphoto(True,window_icon)
menu = Menu(window,);window.config(menu=menu)
file_menu = Menu(menu,tearoff=0)
edit_menu = Menu(menu,tearoff=0)
about_menu = Menu(menu,tearoff=0)
text_area = Text(window, font=("verdana",18), width=38)
scrollBar= Scrollbar(window)

#under file menu
menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='Open',command = Open)
file_menu.add_command(label='New',command = New)
file_menu.add_command(label='Save',command =Save)
file_menu.add_command(label='Quit', command = Quit)

# under editing
menu.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label='Cut', command = Cut)
edit_menu.add_command(label='Copy', command = Copy)
edit_menu.add_command(label='Paste', command = Paste)

# under about, just messagebox

menu.add_cascade(label='Help',menu=about_menu)
about_menu.add_command(label='License', command=Help)
about_menu.add_command(label='About version',command=Help)

# scroll bar
scrollBar.config(command=text_area.yview);text_area.config(yscrollcommand=scrollBar.set)

# packing center
text_area.pack(side= LEFT)
scrollBar.pack(side = RIGHT, fill = BOTH)

window.mainloop()