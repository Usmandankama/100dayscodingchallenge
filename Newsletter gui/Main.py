import re
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def close():
    quit()


def focus_pwd(event):
    Game.pwd_field.focus()

def focus_user(event):
    Game.user_field.focus()
    return 'break'

def enter(event):
    submit()

def submit():
    credit = 0
    try:

        email_pattern_ = re.compile(pattern=r'[A-Za-z0-9.-]+@[a-zA-Z]+\.(com|net|org|io|ng|edu|ie|.)$')
        email_field = Game.email_field.get()
        email_match = email_pattern_.fullmatch(email_field)

        with open('users.json', 'r') as file:
            content = json.load(file)
            list_of_registered = [email for email in content]
            list_of_usernames = [content[email] for email in content]

        pwd_field = Game.pwd_field.get()
        user_filed = Game.user_field.get()

        pref = Game.preference.get()
        freq = Game.frequency.get()
        get_terms = Game.terms_agree.state()
        if not(email_match is None):
            if not(email_field in list_of_registered):
                if len(pwd_field) > 8:
                    if freq != 'Frequency':
                        if pref != 'Preferences':
                            if len(user_filed) > 5:
                                if not(user_filed in list_of_usernames):
                                    if len(get_terms) == 2:
                                        Game.show_terms.destroy()
                                        Game.top_frame.destroy()
                                        Game.email_label.destroy()
                                        Game.pwd_label.destroy()
                                        Game.user_label.destroy()
                                        Game.bottom_frame.pack()
                                        Game.successful.pack()
                                        Game.close_btn.pack(pady=(40, 0))
                                        Game.window.geometry('300x300')
                                    else:
                                        Game.show_terms.pack()
                                else:
                                    messagebox.showinfo(message='Username is taken')
                            else:
                                messagebox.showinfo(message='Username is taken or too short')
                        else:
                            messagebox.showinfo(message='Choose your preference please')
                    else:
                        messagebox.showinfo(message='Choose frequency please')
                else:
                    Game.pwd_field.delete(0,END)
                    messagebox.showinfo(message='Make sure password is long enough')
            else:
                Game.email_field.destroy()
                messagebox.showinfo(message='Email is already registered')
        else:
            messagebox.showinfo(message='Invalid email')

        new_user = {f"{email_field}": f"{user_filed}"}
        content.update(new_user)
        with open('users.json','w') as new_file:
            json.dump(content, new_file, indent=4)

    except KeyError as err:
        print(err)
    except FileNotFoundError:
        ent = {}
        with open('users.json','w') as file:
            json.dump(ent,file)
            pass
        submit()

    finally:
        pass


class Game:
    window = Tk()
    window.geometry('300x450')
    window.title('GUI')
    window.config(bg='white')

    # Frames
    top_frame = Frame(window, bg='white')
    top_frame.pack()

    bottom_frame = Frame(window, bg='white')

    # widgets
    top_label = Label(top_frame, text='Newsletter subscription', font=('Arial',10,'bold'),bg='white')
    top_label.pack()

    email_label = Label(window, text='email', bg='white', font=('Arial',12,'bold'),)
    email_label.place(x=55,y=46)
    email_field = Entry(top_frame, width=20, font=('Arial', 13), relief=SOLID, )
    email_field.pack(pady=(50,0))
    email_field.bind('<Return>', focus_pwd)

    pwd_label = Label(window, text='password', bg='white', font=('Arial', 12,'bold'))
    pwd_label.place(x=55,y=95)
    pwd_field = Entry(top_frame, width=20, font=('Arial', 13), relief=SOLID, show='*')
    pwd_field.pack(pady=(25, 0))
    pwd_field.bind('<Return>', focus_user)

    user_label = Label(window, text='username', bg='white', font=('Arial', 12,'bold'))
    user_label.place(x=55,y=143)
    user_field = Entry(top_frame, width=20, font=('Arial', 13), relief=SOLID,)
    user_field.pack(pady=(25, 0))
    user_field.bind('<Return>', enter)

    val = ['Daily','Weekly','Monthly']
    frequency = ttk.Combobox(top_frame, values=val, width=18, font=('Arial', 13))
    frequency.set('Frequency')
    frequency.pack(pady=(20,0))

    val1 = ['Business','Technology','Music','Politics','Crypto']
    preference = ttk.Combobox(top_frame, values=val1, width=18, font=('Arial', 13))
    preference.set('Preferences')
    preference.pack(pady=(20,0))

    var = IntVar()

    terms_agree = ttk.Radiobutton(top_frame, text='I agree with terms and condition', variable=var, value=1)
    terms_agree.pack(pady=(20,0))
    terms_disagree = ttk.Radiobutton(top_frame, text='No i do not agree', variable=var, value=0)
    terms_disagree.pack(padx=(0,0))

    submit_btn = Button(top_frame, text='Submit', bg='blue', fg='white', font=('Arial', 13,'bold'), command=submit, relief=FLAT, activebackground='blue',activeforeground='white')
    submit_btn.pack(pady=(20,0))
    show_terms = Label(top_frame, text='You have to accept the terms and conditions', fg='red', font=('Arial', 10, 'bold'))

    successful = Label(bottom_frame, text='Successfully subscribed to our services', bg='white', font=('Arial',12))
    close_btn = Button(bottom_frame, text='close', bg='red', fg='white', relief=SOLID, font=('Arial',16,'bold'), command=close)


Game()
def auto_focus():
    Game.email_field.focus()
auto_focus()

Game.window.mainloop()
