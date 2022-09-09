from tkinter import *


class User:

    def __init__(self,name):
        self.name = name
        self.followers = 0
        self.following = 0

    def viewed(self,user):
        self.following += 1
        user.followers += 1


user1 = User(name="salisu")
user2 = User(name="salim")
user1.viewed(user2)
print(user2.followers)


window = Tk()
window.geometry("600x600")
window.config(bg="black")
input_field = Entry(window, font=("Arial", 23))
input_field.pack()

follow_btn = Button(window, text="follow", font=("arial",21), bg="purple",command=quit)
follow_btn.pack()



window.mainloop()
