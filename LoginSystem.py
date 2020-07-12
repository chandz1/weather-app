# Imports:
import tkinter as tk
from PIL import Image, ImageTk
import json
import time


# Lists & Variables:
input_entries = []
login_info = {}
comparitive_info = {}
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

    # def addWidgets(self, master):


class AddButtons():
    def __init__(self, master, text, width, rely,
                 command=None, relx=0.5, height=1, font=None):
        self.master = master
        self.text = text
        self.width = width
        self.height = height
        self.rely = rely
        self.relx = relx
        self.command = command
        self.font = font

    def create_buttons(self):
        button = tk.Button(self.master, text=self.text,
                           width=self.width, height=self.height,
                           bg='#e3d6d6', command=self.command,
                           font=self.font)
        button.place(relx=self.relx, rely=self.rely, anchor=tk.CENTER)


# Functions:
def start_root_window(window_width=None, window_height=None,
                      window_title='The Weather Forecast App'):
    global root
    root = tk.Tk()
    root.title(window_title)
    screen_width = root.winfo_screenwidth()
    screen_height = (root.winfo_screenheight() - 25)
    if window_width is None and window_height is None:
        root.geometry('{}x{}'.format(screen_width, screen_height))
    else:
        root.geometry('{}x{}'.format(window_width, window_height))
    root.resizable(False, False)


def create_canvas():
    global root
    global bg_canvas
    global bg_image
    bg_image = ImageTk.PhotoImage(Image.open('CloudsBg.gif'))
    bg_canvas = tk.Canvas(root, bg='#15adc2')
    bg_canvas.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    bg_canvas.create_image(450, 250, image=bg_image)


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
    input_entries.clear()
    input_entries.append(username_input)
    input_entries.append(password_input)
    forgot_password = AddButtons(
        top_level, 'Forgot password?', 12, 0.7, forgot_passkey, 0.25)
    forgot_password.create_buttons()
    login_btn = AddButtons(top_level, 'Login', 10, 0.7,
                           get_login_input, 0.65)
    login_btn.create_buttons()


def get_login_input():
    global comparitive_info
    username = input_entries[0].get()
    password = input_entries[1].get()
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
                quit(incorrect_label)
            except Exception:
                pass
            logged_in = True
            completeLabel = tk.Label(
                top_level, text='You have been logged in.', fg='green')
            completeLabel.place(relx=0.5, rely=0.125, anchor=tk.CENTER)
            top_level.update_idletasks()
            time.sleep(1.5)
            quit(root)
        else:
            incorrect_label = tk.Label(
                top_level, text='Incorrect username or password.', fg='red')
            incorrect_label.place(relx=0.5, rely=0.125, anchor=tk.CENTER)


def forgot_passkey():
    reset_window = tk.Toplevel(root)
    reset_window.grab_set()
    reset_window.title('Reset Password')
    reset_window.geometry('300x200')
    reset_window.resizable(False, False)


def signin_clicked():
    signup_window = TopLevel('Sign Up', '400x300')
    signup_window.create_toplevel(root)


def guest_login():
    global guest
    time.sleep(0.25)
    quit(root)
    guest = True


def quit(*window):
    for instance in window:
        instance.destroy()


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


def primary_window():
    create_canvas()
    bg_canvas.create_text(675, 200, anchor=tk.CENTER, font=(
        'Calibre', '28'), text='Weather Forecast - Login')

    btn1 = AddButtons(bg_canvas, 'Login', 20, 0.45,
                      command=login_clicked)
    btn2 = AddButtons(bg_canvas, 'Sign Up', 20, 0.5,
                      command=signin_clicked)
    btn3 = AddButtons(bg_canvas, 'Continue Without Sign-In',
                      20, 0.55, command=guest_login)
    btn4 = AddButtons(bg_canvas, 'Quit', 10, 0.977,
                      lambda: confirm_dialog(root), 0.96)
    btn1.create_buttons()
    btn2.create_buttons()
    btn3.create_buttons()
    btn4.create_buttons()

    root.mainloop()


def main_interface():
    create_canvas()

    root.mainloop()


# Initial Log-In Window:
start_root_window()
primary_window()

# Main Interface:
if logged_in is True or guest is True:
    time.sleep(1)
    start_root_window()
    main_interface()
