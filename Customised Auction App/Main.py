#from tkinter import *
import tkinter
import customtkinter
from tkinter import messagebox, ttk


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


window = customtkinter.CTk()
window.geometry('600x300')
window.title('Bidding system')


class Bidders:

    item = {
        "Sarcophagus":20000,
        "Ancient war helmet":15000,
        "Bugatti chiron":50000,
        "Solar panel":100000
    }
    values_list = [n for n in item]

    def __init__(self, main):

        self.bid_amount = customtkinter.CTkLabel(main, text='')
        self.bid_amount.place(x=0,y=0)

        self.firstFrame = customtkinter.CTkFrame(main)
        self.firstFrame.pack(pady=65)

        self.num_of_bidders = customtkinter.CTkLabel(self.firstFrame, text='Bid on item',)
        self.num_of_bidders.pack(pady=20)

        self.cb = customtkinter.CTkComboBox(self.firstFrame, width=300, values=Bidders.values_list)
        self.cb.set('Bid on')
        self.cb.pack(padx=50)

        self.submit = customtkinter.CTkButton(self.firstFrame, text='Submit', width=100, command=self.num_of_bid)
        self.submit.pack(pady=20)

        self.secondFrame = customtkinter.CTkFrame(main)

        self.title = customtkinter.CTkLabel(self.secondFrame, text="Insert bidder's infos")
        self.title.grid(row=0 , column=1, pady=30)

        self.name = customtkinter.CTkEntry(self.secondFrame, width=120,)
        self.name.bind("<Return>", self.focus_bid)
        self.name.grid(row=1, column=0, padx=30)
        self.name.insert(0, 'Name')

        self.bid = customtkinter.CTkEntry(self.secondFrame, width=100, show="*", relief='solid')
        self.bid.bind("<Return>", self.focus_submit )
        self.bid.grid(row=1, column=2, padx=30)
        self.bid.insert(0, 'Bid')

        self.add = customtkinter.CTkButton(self.secondFrame, width=100,  text='Add', command=self.get_values)
        self.add.grid(row=3, column=1)

        self.check = customtkinter.CTkButton(self.secondFrame, width=130, text='Check', command=self.check_winner)
        self.check.grid(row=4, column=2,pady=20)

        self.thirdFrame =customtkinter.CTkFrame(main,)

        self.bidder_name = ''
        self.bidder_bid = 0
        self.num_bid = 0
        self.all_bidders = {}

    def get_values(self):
        try:
            self.bidder_name = self.name.get().title()
            self.bidder_bid = int(self.bid.get())
            __ = {self.bidder_name:self.bidder_bid}
            self.all_bidders.update(__)
            self.name.delete(0, 'end')
            self.bid.delete(0, 'end')
        except ValueError:
            messagebox.showerror(message="Bid has to be a number", title='Error')

    
            
    def focus_bid(self, event): # Changes the cursor focus to bid entry box
        self.bid.focus()
        return("break")
    
    def focus_submit(self,event): # Changes the focus back to the name entry box and also submit the bidder
        self.get_values()
        self.name.focus()
        return("break")

    def check_winner(self):
        try:
            winning_bid = self.num_bid
            for key in self.all_bidders:
                l = customtkinter.CTkLabel(window, text=f'{key} {self.all_bidders[key]}', )
                l.pack()
                if self.all_bidders[key] > winning_bid:
                    winning_bid = self.all_bidders[key]
                    winner = key
            thirdFrame = customtkinter.CTkFrame(window)
            l = customtkinter.CTkLabel(thirdFrame, text=f"{winner.title()} won", fg_color='Green', )
            thirdFrame.pack()
            l.pack(pady=30, padx=30)

            self.secondFrame.destroy()
        except UnboundLocalError:
            messagebox.showerror(message='No bidder has been passed', title='Error')

    def num_of_bid(self):
        try:
            _ = [n for n in Bidders.item]
            if not(self.cb.get() in _):
                raise ValueError()
            for key in _:
                if key == self.cb.get():
                    self.num_bid += Bidders.item[key]
            self.bid_amount.configure(text=f'bid:{self.num_bid}')
            self.firstFrame.destroy()
            window.geometry('800x300')
            self.secondFrame.pack(pady=50)
        except ValueError:
            messagebox.showerror(message='Unavailable item', title='Error')

Bidders(window)

window.mainloop()
