# Imports:
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import smtplib
import SendMail
import json
import time


# Lists & Variables:
login_entries = []
signup_entries = []
login_info = {}
comparitive_info = {}
signup_comp = {}
pass_check = {}
logged_in = False
guest = False


# Classes:
class TopLevel():
    def __init__(self, title, geometry):
        self.title = title
        self.geometry = geometry

    def create_toplevel(self, master):
        global top_level
        top_level = tk.Toplevel(master)
        top_level.grab_set()
        top_level.title(self.title)
        top_level.geometry(self.geometry)
        top_level.resizable(False, False)


class AddButtons():
    def __init__(self, master, text, width, command=None, height=1, font=None):
        self.master = master
        self.text = text
        self.width = width
        self.height = height
        self.command = command
        self.font = font

    def create_buttons(self, rely=0.5, relx=0.5, image=None, bd=1):
        button = tk.Button(self.master, text=self.text,
                           width=self.width, height=self.height,
                           bg='#e3d6d6', command=self.command,
                           font=self.font, image=image, bd=bd)
        button.place(relx=relx, rely=rely, anchor=tk.CENTER)


class AddCanvas():
    def __init__(self, master, width=None, height=None):
        self.master = master
        self.width = width
        self.height = height

    def create_canvas(self, rely=None, relx=None, image=None, side=tk.TOP):
        global canvas
        canvas = tk.Canvas(self.master, width=self.width,
                           height=self.height)
        canvas.pack(expand=True, fill=tk.BOTH, side=side)
        if image is not None:
            canvas.create_image(
                screen_width / 2, screen_height / 2, image=image)


# Functions:
def quit(*window):
    for instance in window:
        instance.destroy()


def start_root_window(window_width=None, window_height=None, window_title='The Weather Forecast App'):
    global root
    global screen_width
    global screen_height
    root = tk.Tk()
    root.title(window_title)
    root.attributes('-fullscreen', True)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # if window_width is None and window_height is None:
    #     root.geometry('{}x{}'.format(screen_width, screen_height))
    # else:
    #     root.geometry('{}x{}'.format(window_width, window_height))
    # root.resizable(False, False)


def write_json(data, filename='loginData.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def save_file():
    global comparitive_info
    with open('loginData.json') as json_file:
        data = json.load(json_file)
        temp = data['userLoginData']
        temp.append(login_info)
    write_json(data)


def login_clicked():
    global login_window
    login_window = TopLevel('Login', '400x175')
    login_window.create_toplevel(root)

    label_user = tk.Label(top_level, text='Username',
                          font=('Calibre', '14'))
    label_user.place(relx=0.25, rely=0.25, anchor=tk.CENTER)

    label_pass = tk.Label(top_level, text='Password',
                          font=('Calibre', '14'))
    label_pass.place(relx=0.25, rely=0.45, anchor=tk.CENTER)

    username_input = tk.Entry(top_level)
    username_input.place(relx=0.65, rely=0.25, anchor=tk.CENTER)

    password_input = tk.Entry(top_level, show='*')
    password_input.place(relx=0.65, rely=0.45, anchor=tk.CENTER)

    login_entries.clear()
    login_entries.append(username_input)
    login_entries.append(password_input)

    forgot_password = AddButtons(
        top_level, 'Forgot password?', 12, forgot_passkey)
    forgot_password.create_buttons(0.7, 0.25)

    login_btn = AddButtons(top_level, 'Login', 10, get_login_input)
    login_btn.create_buttons(0.7, 0.65)


def get_login_input():
    global comparitive_info
    username = login_entries[0].get()
    password = login_entries[1].get()
    comparitive_info.update(Username=username, Password=password)
    print(comparitive_info)
    login()


def login():
    global logged_in
    file_data = json.load(open('loginData.json', 'r'))
    all_users = file_data['userLoginData']
    for user in all_users:
        real_username = user.get('Username')
        real_password = user.get('Password')
        comp_username = comparitive_info.get('Username')
        comp_username = comp_username.lower()
        comp_password = comparitive_info.get('Password')
        if real_username == comp_username and real_password == comp_password:
            global incorrect_label
            try:
                incorrect_label.destroy()
            except Exception:
                pass
            logged_in = True
            completeLabel = tk.Label(
                top_level, text='You Have Been Logged In.', fg='green')
            completeLabel.place(relx=0.5, rely=0.125, anchor=tk.CENTER)
            top_level.update_idletasks()
            time.sleep(1.5)
            quit(root)
        else:
            incorrect_label = tk.Label(
                top_level, text='Incorrect Username Or Password.', fg='red')
            incorrect_label.place(relx=0.5, rely=0.125, anchor=tk.CENTER)


def forgot_passkey():
    reset_window = tk.Toplevel(root)
    reset_window.grab_set()
    reset_window.title('Reset Password')
    reset_window.geometry('300x200')
    reset_window.resizable(False, False)


def signup():
    signup_window = TopLevel('Sign Up', '400x325')
    signup_window.create_toplevel(root)

    username_label = tk.Label(
        top_level, text="Username:", font=('Calibre', '12'))
    username_label.place(relx=0.175, rely=0.075, anchor=tk.CENTER)

    new_user_input = tk.Entry(top_level)
    new_user_input.place(relx=0.5, rely=0.155, anchor=tk.CENTER, width=350)

    email_label = tk.Label(top_level, text="Email:", font=('Calibre', '12'))
    email_label.place(relx=0.12, rely=0.23, anchor=tk.CENTER)

    new_email_input = tk.Entry(top_level)
    new_email_input.place(relx=0.5, rely=0.305, anchor=tk.CENTER, width=350)

    password_label = tk.Label(
        top_level, text="Password:", font=('Calibre', '12'))
    password_label.place(relx=0.16, rely=0.38, anchor=tk.CENTER)

    new_passkey_input = tk.Entry(top_level)
    new_passkey_input.place(relx=0.5, rely=0.455, anchor=tk.CENTER, width=350)

    retype_pass_label = tk.Label(
        top_level, text="Confirm Password:", font=('Calibre', '12'))
    retype_pass_label.place(relx=0.25, rely=0.53, anchor=tk.CENTER)

    retype_pass_input = tk.Entry(top_level)
    retype_pass_input.place(relx=0.5, rely=0.605, anchor=tk.CENTER, width=350)

    signup_entries.clear()
    signup_entries.append(new_user_input)
    signup_entries.append(new_email_input)
    signup_entries.append(new_passkey_input)
    signup_entries.append(retype_pass_input)

    signup_button = AddButtons(
        top_level, 'Create an account', 20, get_signup_input)
    signup_button.create_buttons(0.8)


def get_signup_input():
    global signup_comp
    username = signup_entries[0].get()
    mailid = signup_entries[1].get()
    check_pass = signup_entries[2].get()
    confirm_pass = signup_entries[3].get()
    signup_comp.update(Username=username, MailId=mailid)
    pass_check.update(Password=check_pass, ConfirmPassword=confirm_pass)
    print(signup_comp)
    print(pass_check)
    signup_clicked()


def signup_clicked():
    global no_mailid
    global bad_mailid
    global same_mailid
    login_data = json.load(open('loginData.json', 'r'))
    all_users = login_data['userLoginData']
    for user in all_users:
        existing_username = user.get('Username')
        existing_mail = user.get('MailId')
        comp_username = signup_comp.get('Username')
        comp_username = comp_username.lower()
        comp_mailid = signup_comp.get('MailId')
        comp_mailid = comp_mailid.lower()
        comp_pass = pass_check.get('Password')
        comp_confirm_pass = pass_check.get('ConfirmPassword')
        if comp_mailid != existing_mail:
            if comp_mailid != '':
                if comp_username != existing_username:
                    if comp_pass == comp_confirm_pass:
                        try:
                            SendMail.new_mail = comp_mailid
                            message = SendMail.mail_sent_message
                            SendMail.sendMail()

                            verification_window = TopLevel(
                                'Enter Verification Code', '300x200')
                            verification_window.create_toplevel(root)

                            mail_sent = tk.Label(
                                top_level, text=message, font=('Calibre', '12'))
                            mail_sent.place(relx=0.5, rely=0.3,
                                            anchor=tk.CENTER)

                        except smtplib.SMTPRecipientsRefused:
                            error_exception()
                            bad_mailid = tk.Label(
                                top_level, text='Invalid MailId!', font=('Calibre', '10'), fg='red')
                            bad_mailid.place(
                                relx=0.78, rely=0.235, anchor=tk.CENTER)
                            # print('invalid MailId')

                        except smtplib.socket.gaierror:
                            messagebox.showwarning(
                                title='Internet Connection Error',
                                message='Check You Internet Connection.')
                            # print('Check your internet connection.')
            else:
                error_exception()
                no_mailid = tk.Label(top_level, text='Enter a Mail-Id!',
                                     font=('Calibre', '10'), fg='red')
                no_mailid.place(relx=0.81, rely=0.235, anchor=tk.CENTER)
        else:
            error_exception()
            same_mailid = tk.Label(top_level, text='Mail-Id in use!',
                                   font=('Calibre', '10'), fg='red')
            same_mailid.place(relx=0.81, rely=0.235, anchor=tk.CENTER)


def error_exception():
    try:
        bad_mailid.destroy()
    except Exception:
        pass
    try:
        same_mailid.destroy()
    except Exception:
        pass
    try:
        no_mailid.destroy()
    except Exception:
        pass


def guest_login():
    global guest
    time.sleep(0.25)
    quit(root)
    guest = True


def confirm_dialog(window):
    quit_dialog = TopLevel('Quit Confirmation', '300x90')
    quit_dialog.create_toplevel(window)

    def cancel_quit():
        quit(top_level)
    ask_label = tk.Label(top_level, text='Are you sure you want to exit?')
    ask_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    no_btn = tk.Button(top_level, text='Cancel', width=7, command=cancel_quit)
    no_btn.place(relx=0.35, rely=0.65, anchor=tk.CENTER)
    yes_btn = tk.Button(top_level, text='Exit', width=7,
                        command=lambda: quit(root))
    yes_btn.place(relx=0.65, rely=0.65, anchor=tk.CENTER)


def search_input():
    pass


def primary_window():
    bg_image = ImageTk.PhotoImage(Image.open('CloudsBg.gif'))
    bg = AddCanvas(root)
    bg.create_canvas(image=bg_image)
    canvas.create_text(screen_width / 2, screen_height / 4, anchor=tk.CENTER, font=(
        'Calibre', '28'), text='Weather Forecast - Login')

    btn1 = AddButtons(canvas, 'Login', 20,
                      command=login_clicked)
    btn2 = AddButtons(canvas, 'Sign Up', 20,
                      command=signup)
    btn3 = AddButtons(canvas, 'Continue Without Sign-In',
                      20, command=guest_login)
    btn4 = AddButtons(canvas, 'Quit', 10,
                      lambda: confirm_dialog(root))
    btn1.create_buttons(0.45)
    btn2.create_buttons(0.5)
    btn3.create_buttons(0.55)
    btn4.create_buttons(0.977, 0.96)

    root.mainloop()


def main_interface():
    bg_image = ImageTk.PhotoImage(Image.open('CloudsBg.gif'))
    bg = AddCanvas(root)
    bg.create_canvas(image=bg_image)
    title_bar_height = (root.winfo_screenheight() // 21)
    menu_bar_height = screen_height - title_bar_height
    menu_bar_width = screen_width // 26
    title_bar = tk.Canvas(canvas, width=screen_width, height=40, bd=0)
    title_bar.pack(side=tk.TOP)
    logo = ImageTk.PhotoImage(Image.open('Logo.png'))
    logo_button = tk.Button(title_bar, image=logo, bd=0)
    logo_button.place(relx=0.015, rely=0.5, anchor=tk.CENTER)
    title_bar.create_text(screen_width / 4, 20, anchor=tk.CENTER, font=(
        'Calibre', '14'), text='The Weather Forecast App')
    search_bar = tk.Entry(title_bar, font=("Calibre", '22'), width=17)
    search_bar.place(relx=0.895, rely=0.1, anchor=tk.N)
    search_image = ImageTk.PhotoImage(Image.open('SearchButton.png'))
    search_button = tk.Button(
        title_bar, image=search_image, bd=0, command=search_input)
    search_button.place(relx=0.78, rely=0.5, anchor=tk.CENTER)
    menu_bar = tk.Canvas(canvas, height=menu_bar_height,
                         width=menu_bar_width)
    menu_bar.pack(side=tk.LEFT)
    signout_button = AddButtons(
        menu_bar, text='', width=5, height=2)
    signout_button.create_buttons(0.8, bd=0)
    settings_button = AddButtons(
        menu_bar, text='', width=5, height=2)
    settings_button.create_buttons(0.94, bd=0)



    root.mainloop()


# Initial Log-In Window:
start_root_window()
primary_window()

# Main Interface:
if logged_in is True or guest is True:
    time.sleep(1)
    start_root_window()
    main_interface()
