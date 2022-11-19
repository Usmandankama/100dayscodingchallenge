import re
import json
import time
import random
import smtplib
from tkinter import *
from tkinter import ttk
from threading import Thread
from tkinter import messagebox
from email.message import EmailMessage
from concurrent.futures import ThreadPoolExecutor


class GUI:



    def __init__(self):

        self.root = Tk()
        self.root.title('GUI')
        self.root.geometry('300x450')
        self.root.resizable(0, 0)
        self.root.config(bg='white')

        # Frames
        self.top_frame = Frame(self.root, bg='white')
        self.top_frame.pack()
        self.mid_frame = Frame(self.root, bg='white')

        self.bottom_frame = Frame(self.root, bg='white')

        # widgets
        self.top_label = Label(self.top_frame, text='Newsletter subscription', font=('Arial', 10, 'bold'), bg='white')
        self.top_label.pack()

        self.email_label = Label(self.root, text='email', bg='white', font=('Arial', 12, 'bold'), )
        self.email_label.place(x=55, y=46)
        self.email_field = Entry(self.top_frame, width=20, font=('Arial', 13), relief=SOLID, )
        self.email_field.pack(pady=(50, 0))
        self.email_field.bind('<Return>', self.focus_pwd)

        self.pwd_label = Label(self.root, text='password', bg='white', font=('Arial', 12, 'bold'))
        self.pwd_label.place(x=55, y=95)
        self.pwd_field = Entry(self.top_frame, width=20, font=('Arial', 13), relief=SOLID, show='*')
        self.pwd_field.pack(pady=(25, 0))
        self.pwd_field.bind('<Return>', self.focus_user)

        self.user_label = Label(self.root, text='username', bg='white', font=('Arial', 12, 'bold'))
        self.user_label.place(x=55, y=143)
        self.user_field = Entry(self.top_frame, width=20, font=('Arial', 13), relief=SOLID, )
        self.user_field.pack(pady=(25, 0))
        self.user_field.bind('<Return>', self.enter)

        val = ['Daily', 'Weekly', 'Monthly']
        self.frequency = ttk.Combobox(self.top_frame, values=val, width=18, font=('Arial', 13))
        self.frequency.set('Frequency')
        self.frequency.pack(pady=(20, 0))

        val1 = ['Business', 'Technology', 'Music', 'Politics', 'Crypto']
        self.preference = ttk.Combobox(self.top_frame, values=val1, width=18, font=('Arial', 13))
        self.preference.set('Preferences')
        self.preference.pack(pady=(20, 0))

        var = IntVar()

        self.terms_agree = ttk.Radiobutton(self.top_frame, text='I agree with terms and condition', variable=var, value=1)
        self.terms_agree.pack(pady=(20, 0))
        self.terms_disagree = ttk.Radiobutton(self.top_frame, text='No i do not agree', variable=var, value=0)
        self.terms_disagree.pack(padx=(0, 0))

        self.submit_btn = Button(self.top_frame, text='Submit', bg='blue', fg='white', font=('Arial', 13, 'bold'), relief=FLAT,
                            activebackground='blue', activeforeground='white', command=self.submit)
        self.submit_btn.pack(pady=(20, 0))
        self.show_terms = Label(self.top_frame, text='You have to accept the terms and conditions', fg='red',
                           font=('Arial', 10, 'bold'))

        self.pin_label = Label(self.mid_frame, text='Please check your mail for a code we just sent.', font=('Arial', 9, 'bold'),
                          bg='white')
        self.pin_label.pack()
        self.otp_field = Entry(self.mid_frame, font=('Arial', 13, 'bold'), relief=SOLID, bd=2, width=20)
        self.otp_field.bind('<Return>', self.confirm)
        self.otp_field.pack(pady=(40, 0))
        self.confirm_otp_btn = Button(self.mid_frame, text='Confirm', bg='blue', fg='white', font=('Arial', 13, 'bold'),
                                 relief=FLAT, activebackground='blue', activeforeground='white', command=self.confirm_otp)
        self.confirm_otp_btn.pack(pady=(20, 0))
        self.invalid_otp = Label(self.mid_frame, text='Invalid OTP number...please check your mail', fg='red',
                            font=('Arial', 10, 'bold'), bg='white')
        self.resend_mail = Button(self.mid_frame, text='resend code', relief=FLAT, bg='white', fg='blue',
                             font=('Calibri', 10, 'italic'), command=self.resend_otp)

        self.successful = Label(self.bottom_frame, text='Successfully subscribed to our services', bg='white', font=('Arial', 12))
        self.successful.pack()
        self.close_btn = Button(self.bottom_frame, text='close', bg='red', fg='white', relief=SOLID, font=('Arial', 16, 'bold'),
                           command=self.close)


        self.pin_ = 0

        self.close_btn.pack(pady=(40, 0))
        self.root.mainloop()

        
    
    def close(self):
        quit()


    def focus_pwd(self,event):
        self.pwd_field.focus()
        return 'break'


    def focus_user(self,event):
        self.user_field.focus()
        return 'break'
    

    def confirm(self,event):
        self.confirm_otp()


    def enter(self,event):
        self.submit()

    def send_otp(self):
        list_of_otp = [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) for _ in range(6)]
        self.pin = int(''.join(str(x) for x in list_of_otp))
        # self.pin_ += self.pin

        to_add = str(self.user_mail)
        msg = EmailMessage()
        msg['From'] = '19slsusman@gmail.com'
        msg['Subject'] = 'OTP code'
        msg.set_content(f'Your one time pin is: {self.pin}')

        conn = smtplib.SMTP_SSL('smtp.gmail.com', port=465)
        conn.login('19slsusman@gmail.com', 'vpjoiwuhhxdtxxre')
        msg['To'] = to_add
        conn.send_message(msg)

    def submit(self):
        try:

            email_pattern_ = re.compile(pattern=r'[A-Za-z0-9.-]+@[a-zA-Z]+\.(com|net|org|io|ng|edu|ie|.)$')
            email_field = self.email_field.get().strip()
            email_match = email_pattern_.fullmatch(email_field)


            with open('users.json', 'r') as file:
                content = json.load(file)
                list_of_usernames = [key for key in content]
                list_of_emails = [value['Email'] for key,value in content.items()]

            pwd_field = self.pwd_field.get()
            username_pattern = re.compile(pattern=r'[A-Za-z0-9.-]+')
            user_field= self.user_field.get()
            username_field = user_field.strip()
            username_match = username_pattern.fullmatch(username_field)

            pref = self.preference.get()
            freq = self.frequency.get()

            self.user_mail = email_field
            self.user_password = pwd_field
            self.user_name = user_field
            self.user_pref = pref
            self.user_freq = freq

            get_terms = self.terms_agree.state()
            if not (email_match is None):
                if not (email_field in list_of_emails):
                    if not(' ' in [x for x in pwd_field]):
                        if len(pwd_field) > 8:
                            if not(' ' in [x for x in user_field]):
                                if freq != 'Frequency':
                                    if pref != 'Preferences':
                                        if len(user_field) > 5:
                                            if not(username_match is None):
                                                if not (user_field in list_of_usernames):
                                                    if len(get_terms) == 2:
                                                        self.send_otp()

                                                        self.user_label.destroy()
                                                        self.email_label.destroy()
                                                        self.pwd_label.destroy()
                                                        self.top_frame.destroy()
                                                        self.mid_frame.pack()
                                                        self.otp_field.focus()
                                                        self.root.geometry('300x250')

                                                    else:
                                                        self.show_terms.pack()
                                                else:
                                                    messagebox.showinfo(message='Username is taken')
                                            else:
                                                messagebox.showinfo(message='Invalid username character(s)')
                                        else:
                                            messagebox.showinfo(message='Username is taken or too short')
                                    else:
                                        messagebox.showinfo(message='Choose your preference please')
                                else:
                                    messagebox.showinfo(message='Choose frequency please')
                            else:
                                messagebox.showinfo(message='Invalid username (remove spaces please)')
                        else:
                            self.pwd_field.delete(0, END)
                            messagebox.showinfo(message='Make sure password is long enough')
                    else:
                        messagebox.showinfo(message='Password cannot contain spaces')
                else:
                    self.email_field.delete(0, END)
                    messagebox.showinfo(message='Email is already registered')
            else:
                messagebox.showinfo(message='Invalid email')

        except FileNotFoundError:
            ent = {}
            with open('users.json', 'w') as file:
                json.dump(ent, file)
                pass
            self.submit()

        finally:
            pass

    def confirm_otp(self):
        if str(self.otp_field.get()) == str(self.pin):
            self.mid_frame.destroy()
            self.bottom_frame.pack()

            with open('users.json', 'r') as file:
                content = json.load(file)
            
            new_user = {f"{self.user_name}":{"Email":f"{self.user_mail}","Password":f"{self.user_password}","Preference":f"{self.user_pref}","Frequency":f"{self.user_freq}"}}
            content.update(new_user)
            with open('users.json', 'w') as new_file:
                json.dump(content, new_file, indent=4)

        else:
            self.resend_mail.pack(pady=(10,0))
            self.invalid_otp.pack(pady=(15,0))
    
    def resend_otp(self):
        self.send_otp()
        self.resend_mail['state'] = 'disabled'


if __name__ == '__main__':
    GUI()

