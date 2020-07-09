# Imports:
import tkinter as tk
from PIL import Image, ImageTk
import json


# Lists & Variables:
inputEntries = []
loginInfo = {}
compLoginInfo = {}


# Classes:
class addButtons():
    def __init__(self, master, text, width, rely,
                 relx=0.5, height=1, command=None):
        self.master = master
        self.text = text
        self.width = width
        self.height = height
        self.rely = rely
        self.relx = relx
        self.command = command

    def createButton(self):
        button = tk.Button(self.master, text=self.text,
                           width=self.width, height=self.height,
                           bg='#e3d6d6', command=self.command)
        button.place(relx=self.relx, rely=self.rely, anchor=tk.CENTER)


# Functions:
def writeJson(data, filename='loginData.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def saveFile():
    global compLoginInfo
    with open('loginData.json') as jsonFile:
        data = json.load(jsonFile)
        temp = data['userLoginData']
        temp.append(loginInfo)
    writeJson(data)


def login():
    fileData = json.load(open('loginData.json', 'r'))
    allUsers = fileData['userLoginData']
    for user in allUsers:
        realUsername = user.get('Username')
        realPassword = user.get('Password')
        compUsername = compLoginInfo.get('Username')
        compPassword = compLoginInfo.get('Password')
        if realUsername == compUsername and realPassword == compPassword:
            print('logged in')


def loginButtonClicked():
    loginWindow = tk.Toplevel(root)
    loginWindow.grab_set()
    loginWindow.title('Login')
    loginWindow.geometry('400x550')
    loginWindow.resizable(0, 0)
    labelUser = tk.Label(loginWindow, text='username',
                         font=('Calibre', '15'))
    labelUser.place(relx=0.3, rely=0.45, anchor=tk.CENTER)
    labelPass = tk.Label(loginWindow, text='password',
                         font=('Calibre', '15'))
    labelPass.place(relx=0.3, rely=0.55, anchor=tk.CENTER)
    usernameInput = tk.Entry(loginWindow)
    usernameInput.place(relx=0.65, rely=0.45, anchor=tk.CENTER)
    passwordInput = tk.Entry(loginWindow)
    passwordInput.place(relx=0.65, rely=0.55, anchor=tk.CENTER)
    inputEntries.append(usernameInput)
    inputEntries.append(passwordInput)
    Loginbtn = addButtons(loginWindow, 'Login', 10, 0.65,
                          command=getLoginInput)
    Loginbtn.createButton()


def getLoginInput():
    global compLoginInfo
    username = inputEntries[0].get()
    password = inputEntries[1].get()
    compLoginInfo.update(Username=username, Password=password)
    print(compLoginInfo)
    login()


def Quit():
    root.destroy()


def confirmDialog():
    quitDialog = tk.Toplevel(root)
    quitDialog.grab_set()
    quitDialog.title('Quit Confirmation')
    quitDialog.geometry('300x90')

    def cancelQuit():
        quitDialog.destroy()
    askLabel = tk.Label(quitDialog, text='Are you sure you want to exit?')
    askLabel.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    nobtn = tk.Button(quitDialog, text='Cancel', width=7, command=cancelQuit)
    nobtn.place(relx=0.35, rely=0.65, anchor=tk.CENTER)
    yesbtn = tk.Button(quitDialog, text='Exit', width=7, command=Quit)
    yesbtn.place(relx=0.65, rely=0.65, anchor=tk.CENTER)


# Initial Window Creation:
root = tk.Tk()
root.title('The Weather Forecast App')
screenWidth = root.winfo_screenwidth()
screenHeight = (root.winfo_screenheight() - 25)
root.geometry('{}x{}'.format(screenWidth, screenHeight))
# root.maxsize(screenWidth, screenHeight)
root.resizable(0, 0)

# Assigning Background Image
bgImage = ImageTk.PhotoImage(Image.open('CloudsBg.gif'))

# Creating Canvas:
bgCanvas = tk.Canvas(root, bg='#15adc2')
bgCanvas.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
bgCanvas.create_image(450, 250, image=bgImage)
bgCanvas.create_text(675, 200, anchor=tk.CENTER, font=(
    'Calibre', '28'), text='Weather Forecast - Login')

# Creating Buttons:
btn1 = addButtons(bgCanvas, 'Login', 20, 0.45, command=loginButtonClicked)
btn2 = addButtons(bgCanvas, 'Sign Up', 20, 0.5)
btn3 = addButtons(bgCanvas, 'Continue Without Sign-In', 20, 0.55)
btn4 = addButtons(bgCanvas, 'Quit', 10, 0.977,
                  relx=0.96, command=confirmDialog)
btn1.createButton()
btn2.createButton()
btn3.createButton()
btn4.createButton()

root.mainloop()
