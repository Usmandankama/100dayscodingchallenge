import re,time,json,random,socket,smtplib,threading,requests
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
from tkinter import messagebox
from email.message import EmailMessage
# from concurrent.futures import ThreadPoolExecutor


class Home:

    def __init__(self):

        self.window = Tk()  
        self.window.geometry("450x400")
        self.window.resizable(0,0)
    
        self.bg = PhotoImage(file = "p.png")
        
        self.canvas1 = Canvas( self.window, width = 400, height = 400)
        self.canvas1.pack(fill = "both", expand = True)
        self.canvas1.create_image( 0, 0, image = self.bg,anchor = "nw")

        self.label1 = Label(self.canvas1, text='Choose from below options', font=("Arial", 13, 'normal') ,bg=self._from_rgb((247,247,247)))

        self.label2 = Label(self.canvas1, text='Welcome to our newsletter app', font=("Arial", 20, 'bold'),bg=self._from_rgb((247,247,247)))
        self.label2.pack()
        self.label1.pack(pady=(30,0))

        self.frame = Frame(self.canvas1, bg=self._from_rgb((247,247,247)))
        self.frame.pack()

        self.login_btn = Button(self.frame, text='Login', bg='blue', fg='white', relief=FLAT, activebackground='blue', activeforeground='white', font=('Arial', 19), command=self._login_)
        self.login_btn.grid(row=0, column=0, padx=(0,20), pady=(30,0))

        self.sign_up_btn = Button(self.frame, text='Sign up', bg='blue', fg='white', relief=FLAT, activebackground='blue', activeforeground='white', font=("Arial", 19), command=self._sign_up)
        self.sign_up_btn.grid(row=0, column=1, padx=(20,0), pady=(30,0))


        self.window.mainloop()

    def _from_rgb(self,rgb):

        return "#%02x%02x%02x" % rgb
    
    def _sign_up(self):
       SignUp()
    
    def _login_(self):
        self.window.destroy()
        Login()


class SignUp:


# Variables initialization
    def __init__(self):
        try:
            # Root tweaks
            self.root = Tk()
            self.root.title('SignUp')
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

            val1 = ['Business', 'Politics', 'Crypto', 'Sport']
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
            self.otp_field.bind("<Return>", self.confirm_on_keyboard)
            self.otp_field.pack(pady=(40, 0))
            self.confirm_otp_btn = Button(self.mid_frame, text='Confirm', bg='blue', fg='white', font=('Arial', 13, 'bold'),
                                    relief=FLAT, activebackground='blue', activeforeground='white', command=self.confirm_otp)
            self.confirm_otp_btn.pack(pady=(20, 0))
            self.invalid_otp = Label(self.mid_frame, text=' ', fg='red',
                                font=('Arial', 10, 'bold'), bg='white')
            self.invalid_otp.pack(pady=(10,0))
            self.wait_seconds = 30
            self.show_timer = Label(self.mid_frame, text=f'Request pin in {self.wait_seconds} seconds',font=('Arial', 10, 'bold'), bg='white')
            self.resend_mail = Button(self.mid_frame, text='resend code', relief=FLAT, bg='white', fg='blue',
                                font=('Calibri', 10, 'italic'), command=threading.Thread(target=self.resend_wait).start)

            self.successful = Label(self.bottom_frame, text='Successfully subscribed to our services', bg='white', font=('Arial', 12))
            self.successful.pack()
            self.close_btn = Button(self.bottom_frame, text='close', bg='red', fg='white', relief=SOLID, font=('Arial', 16, 'bold'),
                            command=self.close)


            self.pin_ = 0

            self.close_btn.pack(pady=(40, 0))
            self.root.mainloop()

        except RuntimeError:
            pass

    def focus_pwd(self,event):
        self.pwd_field.focus()
        return 'break'


    def focus_user(self,event):
        self.user_field.focus()
        return 'break'

    def enter(self,event):
        self.submit()

    def send_otp(self):
        try: 
            list_of_otp = [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) for _ in range(6)]
            self.pin = int(''.join(str(x) for x in list_of_otp))

            to_add = str(self.user_mail)
            msg = EmailMessage()
            msg['From'] = '19slsusman@gmail.com'
            msg['Subject'] = 'OTP code'
            msg.set_content(f'Your one time pin is: {self.pin}')

            conn = smtplib.SMTP_SSL('smtp.gmail.com', port=465)
            conn.login('19slsusman@gmail.com', 'vpjoiwuhhxdtxxre')
            msg['To'] = to_add
            conn.send_message(msg)
        except socket.gaierror:
            self.ask = messagebox.showerror(message='Please connect to the internet and try again')
            if self.ask == 'ok':
                quit()
        except TimeoutError:
            messagebox.showerror(message='Request timed out please try again later')

    def submit(self):
        try:

            email_pattern_ = re.compile(pattern=r'[A-Za-z0-9.-]+@(gmail|yahoo|aol|outlook)\.(com|net|org|io|ng|edu|ie)$')
            email_field = self.email_field.get().strip()
            email_match = email_pattern_.fullmatch(email_field)


            with open('users.json', 'r') as file:
                content = json.load(file)
                list_of_usernames = [value['Username'] for key,value in content.items()]
                list_of_emails = [key for key in content]

            pwd_field = self.pwd_field.get()
            username_pattern = re.compile(pattern=r'[A-Za-z0-9._-]+')
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
                                                        threading.Thread(target=self.send_otp).start()

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
            
            new_user = {f"{self.user_mail}":{"Username":f"{self.user_name}","Password":f"{self.user_password}","Preference":f"{self.user_pref}","Frequency":f"{self.user_freq}"}}
            content.update(new_user)
            with open('users.json', 'w') as new_file:
                json.dump(content, new_file, indent=4)

            try: 
                to_add = str(self.user_mail)
                msg = EmailMessage()
                msg['From'] = '19slsusman@gmail.com'
                msg['Subject'] = 'Newsletter'
                msg.set_content(f'You have successfully subscribed to this newsletter\nYou are going to receive a mail related to {self.user_pref.lower()}...{self.user_freq.lower()}\n\n\nThank you for chosing our services')

                conn = smtplib.SMTP_SSL('smtp.gmail.com', port=465)
                conn.login('19slsusman@gmail.com', 'vpjoiwuhhxdtxxre')
                msg['To'] = to_add
                conn.send_message(msg)
            except socket.gaierror:
                self.ask = messagebox.showerror(message='Please connect to the internet and try again')
                if self.ask == 'ok':
                    quit()

        else:
            self.resend_mail.pack(pady=(10,0))
            self.invalid_otp.config(text='Invalid OTP number...please check your mail')

            def cancel_errr():
                time.sleep(10)
                self.invalid_otp.config(text=' ')
            
            threading.Thread(target=cancel_errr).start()
    
    def confirm_on_keyboard(self,event):
        self.confirm_otp()
        
    def resend_wait(self):
        threading.Thread(target=self.send_otp).start()
        self.resend_mail['state'] = 'disabled'
        self.show_timer.config(fg='black')
        self.show_timer.pack(pady=(5, 0))

        def reduce_timer():
            try:
                while True:
                    if self.wait_seconds != 0:
                        time.sleep(1)
                        self.wait_seconds -= 1
                        self.show_timer.config(text=f'Request pin in {self.wait_seconds} seconds')
                    else:
                        self.show_timer.config(text=' ')
                        self.resend_mail['state'] = 'normal'
                        break
            except Exception as error:
                pass


        threading.Thread(target=reduce_timer).start()

    def close(self):
        quit()
    


class Login:


    def __init__(self):

        # Root tweaks
        self.root = Tk()
        self.root.title('Login Page')
        self.root.geometry('400x200')
        self.root.resizable(0, 0)
        self.root.config(bg='white')

        self.frame = Frame(self.root, bg='white')
        self.frame.pack(pady=(35,0))

        self.bg = PhotoImage(file = "p.png")

        self.frame1 = Frame(self.root, bg='white')
        self.frame1.pack()

        home_ico = PhotoImage(file = "Home_icon.png")

        self.back = Button(self.root, image=home_ico, font=("impact", 19,'bold'), fg='blue', bg='white', relief=FLAT, activebackground='white', activeforeground='blue', command=self.back_)
        self.back.place(x=0,y=0)

        self.email_label = Label(self.frame, text='Email:', font=("Arial", 13 ), bg='white')
        self.email_label.grid(row=0, column=0, padx=(0,10))

        self.email_field = Entry(self.frame, width=20, font=("Arial", 13), relief=SOLID, fg='grey')
        self.email_field.bind("<Return>", self.focus_next)
        self.email_field.grid(row=0, column=1)

        self.pass_label = Label(self.frame, text='Password:', font=("Arial", 13 ), bg='white')
        self.pass_label.grid(row=1, column=0, padx=(0,10), pady=(15,0))

        self.pass_field = Entry(self.frame, width=20, font=("Arial", 13), relief=SOLID, fg='grey',show='*')
        self.pass_field.bind("<Return>", self.submit_login)
        self.pass_field.grid(row=1, column=1, pady=(15,0))

        self.login_btn = Button(self.frame1, text='Login', width=7, font=("Arial",13,'bold'), relief=FLAT, bg='blue', fg='white', activebackground='blue', activeforeground='white', command=self.Auth)
        self.login_btn.pack(padx=(50,0), pady=(15,0))
        self.admin_ = Button(self.frame1, text='Login as Administrator', bg='white', fg='blue', relief=FLAT, font=('Arial',13), highlightthickness=0\
            ,activebackground='white', activeforeground='blue',command=self.login_admin)
        self.admin_.pack(pady=(10,0), padx=(30,0))

        self.frame2 = Frame(self.root,bg='white')
        self.info_label = Label(self.frame2, text='Click to send mail to all clients', font=('Arial',13), bg='white')
        self.info_label.pack(pady=(10,0))
        self.send_all = Button(self.frame2, text='Send to all', bg='blue', fg='white', width=11, font=('Arial', 12), relief=FLAT, activebackground='blue', activeforeground='white', command=self.send_to_all)
        self.send_all.pack(pady=(40,0))
        self.quitt = Label(self.frame2, text='Program will quit in 5 seconds', font=('Arial',13), bg='white')
        self.root.mainloop()

    def focus_next(self,event):
            self.pass_field.focus()
            return 'break'

    def submit_login(self,event):
        self.Auth()

    def Auth(self):
        try:
            email_field_text = self.email_field.get()
            pass_field_text = self.pass_field.get()

            with open('users.json', 'r') as file:
                content = json.load(file)
                list_of_emails = [key for key in content]


            if email_field_text in list_of_emails:
                if pass_field_text == content[email_field_text]['Password']:
                    username = content[email_field_text]['Username']
                    messagebox.showinfo(message=f'Successfully logged in as {username.title()}')
                else:
                    messagebox.showerror(message='Wrong password')
                    self.pass_field.delete(0,END)
            else:
                messagebox.showerror(message='Email is not registred.')

        except FileNotFoundError:
            messagebox.showerror(message='Our server is under maintenance at the moment, please try again later')
    
    def login_admin(self):
        try:
            pass_field_text = self.pass_field.get()

            email_pattern_ = re.compile(pattern=r'[A-Za-z0-9.-]+@(gmail|yahoo|aol|outlook)\.(com|net|org|io|ng|edu|ie)$')
            email_field_text = self.email_field.get().strip()
            email_match = email_pattern_.fullmatch(email_field_text)

            if (email_match is not None):
                if len(pass_field_text) >= 8:
                    self.frame1.destroy()
                    self.frame.destroy()
                    self.back.destroy()
                    self.root.title('Logged in as admin')
                    self.frame2.pack()
            
        except Exception as e:
            print('pass')

    def send_to_all(self):
        General().solve()
        self.send_all.config(state='disabled', bg='white')

        def quittin():
            self.quitt.pack(pady=(10,0))
            time.sleep(5)
            self.root.destroy()
        
        threading.Thread(target=quittin).start()

    def back_(self):
        self.root.destroy()
        Home()



# POLITICS ________________________________________________________________________________
def politics()->tuple:
    politics_html_file = requests.get(url='https://www.nta.ng/').text

    pol_soup = BeautifulSoup(politics_html_file, 'html.parser')
    pol_soup.prettify()
    header_element = pol_soup.find('h3', class_='item-title')
    link = header_element.find_all('a', href=True)
    for a in link:
        title = a.text
        url = a.get("href")

    # span_element = soup.find('p', class_='item-snippet')
    span_element = pol_soup.select_one(selector='.item-snippet')
    body = span_element.span.text

    return (title, body, url)



# BUSINESS______________________________________________________________________________________

def business()->tuple:
    business_html_file = requests.get(url='https://businessday.ng/').text
    b_soup = BeautifulSoup(business_html_file, 'lxml')
    recent_list = b_soup.find('div', class_='row-1')



    news_header = recent_list.find('h3', class_='title')
    bdy = recent_list.find('div', class_='post-summary')

    title = news_header.a.getText()
    url = news_header.a.get('href')
    body = bdy.getText()

    return (title.strip(), body.strip(), url)

# SPORTS _______________________________________________________________________________________________

def sport()->tuple:
    sp_html_file = requests.get(url='https://www.skysports.com/').text
    sp_soup = BeautifulSoup(sp_html_file, 'lxml')

    recent_one = sp_soup.find('h3', class_="sdc-site-tile__headline")

    title = recent_one.span.getText()
    url = 'https://www.skysports.com'+recent_one.a.get('href')

    new_response = requests.get(url).text
    sp_new_soup = BeautifulSoup(new_response, 'lxml')
    sp_headline_body = sp_new_soup.find('p', class_='sdc-article-header__sub-title sdc-site-component-header--h2')

    body = url

    return (title, body, url)


# CRYPTO______________________________________________________________________________________________

def crypto():
    crpto_html_file = requests.get(url='https://www.binance.com/en/news/top').text

    crpto_soup = BeautifulSoup(crpto_html_file, 'lxml')
    rec = crpto_soup.find('div', class_='css-1i9bvdl')
    title = rec.find('div', class_='css-yvdj0q').getText()
    body =  rec.find('div', class_='css-15z93by').getText()
    url =  'https://www.binance.com/en/new/top?'+rec.find('a').get('href')

    return (title, body, url)


class General:

    def __init__(self) -> None:

        self.user_mail = ''
        self.username = ''
        self.send_message()



    def send_message(self):
        try:
            with open('users.json') as file:
                db = json.load(file)
            list_of_biz = [email for email,items in db.items() if items['Preference'] == 'Business']
            list_of_pol = [email for email,items in db.items() if items['Preference'] == 'Politics']
            list_of_sp = [email for email,items in db.items() if items['Preference']=='Sport']
            list_of_crpto = [email for email,items in db.items() if items['Preference']=='Crypto']

            self.bizStr = ','.join(str(x) for x in list_of_biz)
            self.polStr = ','.join(str(x) for x in list_of_pol)
            self.spStr = ','.join(str(x) for x in list_of_sp)
            self.crptoStr = ','.join(str(x) for x in list_of_crpto)

        except Exception as e:
            print(e)

    def solve(self):
        if len(self.bizStr) != 0:
            threading.Thread(target=self.send_biz).start()
        if len(self.polStr) != 0:
            threading.Thread(target=self.send_pol).start()
        if len(self.spStr) != 0:
            threading.Thread(target=self.send_sp).start()
        if len(self.crptoStr) != 0:
            threading.Thread(target=self.send_crpto).start()

    def connection(self,message):
        mymail = '19slsusman@gmail.com'
        conn = smtplib.SMTP_SSL('smtp.gmail.com', port=465)

        conn.login(user=mymail, password='vpjoiwuhhxdtxxre')
        conn.send_message(msg=message)

    def send_biz(self):
        biz_title, biz_body, biz_url = business()

        msg = EmailMessage()
        msg['From'] = '19slsusman@gmail.com'
        msg['Subject'] = 'Business update'
        msg.set_content(f'Title: {biz_title}\n\n\n{biz_body}\nSource: {biz_url}\n\n~sls~')
        msg['To'] = self.bizStr
        self.connection(msg)

    def send_pol(self):
        pol_title, pol_body, pol_url = politics()

        msg = EmailMessage()
        msg['From'] = '19slsusman@gmail.com'
        msg['Subject'] = 'Politics update'
        msg.set_content(f'Title: {pol_title}\n\n\n{pol_body}\nSource: {pol_url}\n\n~sls~')
        msg['To'] = self.polStr
        self.connection(msg)
    
    def send_sp(self):
        sp_title, sp_body, sp_url = sport()

        msg = EmailMessage()
        msg['From'] = '19slsusman@gmail.com'
        msg['Subject'] = 'Sports update'
        msg.set_content(f'Title: {sp_title}\n\n\n{sp_body}\nSource: {sp_url}\n\n~sls~')
        msg['To'] = self.spStr
        self.connection(msg)

    def send_crpto(self):
        crpto_title, crpto_body, crpto_url = crypto()

        msg = EmailMessage()
        msg['From'] = '19slsusman@gmail.com'
        msg['Subject'] = 'Crypto update'
        msg.set_content(f'Title: {crpto_title}\n\n\n{crpto_body}\nSource: {crpto_url}\n\n~sls~')
        msg['To'] = self.crptoStr
        self.connection(msg)


if __name__ == '__main__':
    Home()
