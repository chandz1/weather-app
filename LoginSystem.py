# Imports:
import tkinter as tk
from PIL import Image, ImageTk
import json
import time


# Lists & Variables:
inputEntries = []
loginInfo = {}
compLoginInfo = {}
loggedIn = False
guest = False


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
def startRootWindow(windowWidth=None, windowHeight=None):
    global root
    root = tk.Tk()
    root.title('The Weather Forecast App')
    screenWidth = root.winfo_screenwidth()
    screenHeight = (root.winfo_screenheight() - 25)
    if windowWidth is None and windowHeight is None:
        root.geometry('{}x{}'.format(screenWidth, screenHeight))
    else:
        root.geometry('{}x{}'.format(windowWidth, windowHeight))
    root.resizable(0, 0)


def createCanvas():
    global root
    global bgCanvas
    global bgImage
    bgImage = ImageTk.PhotoImage(Image.open('CloudsBg.gif'))
    bgCanvas = tk.Canvas(root, bg='#15adc2')
    bgCanvas.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    bgCanvas.create_image(450, 250, image=bgImage)


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


def loginButtonClicked():
    global root
    global loginWindow
    loginWindow = tk.Toplevel(root)
    loginWindow.grab_set()
    loginWindow.title('Login')
    loginWindow.geometry('400x200')
    loginWindow.resizable(0, 0)
    labelUser = tk.Label(loginWindow, text='Username',
                         font=('Calibre', '14'))
    labelUser.place(relx=0.25, rely=0.3, anchor=tk.CENTER)
    labelPass = tk.Label(loginWindow, text='Password',
                         font=('Calibre', '14'))
    labelPass.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
    usernameInput = tk.Entry(loginWindow)
    usernameInput.place(relx=0.65, rely=0.3, anchor=tk.CENTER)
    passwordInput = tk.Entry(loginWindow, show='*')
    passwordInput.place(relx=0.65, rely=0.5, anchor=tk.CENTER)
    inputEntries.append(usernameInput)
    inputEntries.append(passwordInput)
    Loginbtn = addButtons(loginWindow, 'Login', 10, 0.75,
                          command=getLoginInput)
    Loginbtn.createButton()


def getLoginInput():
    global compLoginInfo
    username = inputEntries[0].get()
    password = inputEntries[1].get()
    compLoginInfo.update(Username=username, Password=password)
    print(compLoginInfo)
    login()


def login():
    global loggedIn
    global loginWindow
    fileData = json.load(open('loginData.json', 'r'))
    allUsers = fileData['userLoginData']
    for user in allUsers:
        realUsername = user.get('Username')
        realPassword = user.get('Password')
        compUsername = compLoginInfo.get('Username')
        compUsername = compUsername.lower()
        compPassword = compLoginInfo.get('Password')
        if realUsername == compUsername and realPassword == compPassword:
            global failedLabel
            try:
                failedLabel.destroy()
            except Exception:
                pass
            loggedIn = True
            loginWindow.destroy()
            loggedInPopUp()
        else:
            failedLabel = tk.Label(
                loginWindow, text='Incorrect username or password.')
            failedLabel.place(relx=0.5, rely=0.15, anchor=tk.CENTER)


def loggedInPopUp():
    global root
    loggedInPopUp = tk.Toplevel(root)
    loggedInPopUp.title('Logged In')
    loggedInPopUp.geometry('300x100')
    loggedInPopUp.resizable(0, 0)
    loggedInLabel = tk.Label(
        loggedInPopUp, text='You have successfully been logged in.')
    loggedInLabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    okBtn = addButtons(loggedInPopUp, 'OK', 3, 0.7,
                       command=lambda: Quit(root))
    okBtn.createButton()


def signinButtonClicked():
    global root
    global signupWindow
    signupWindow = tk.Toplevel(root)
    signupWindow.grab_set()
    signupWindow.title('Sign Up')
    signupWindow.geometry('400x200')
    signupWindow.resizable(0, 0)


def continueWithoutSignIn():
    global guest
    Quit(root)
    guest = True


def Quit(window):
    window.destroy()


def confirmDialog(window):
    quitDialog = tk.Toplevel(window)
    quitDialog.grab_set()
    quitDialog.title('Quit Confirmation')
    quitDialog.geometry('300x90')

    def cancelQuit():
        quitDialog.destroy()
    askLabel = tk.Label(quitDialog, text='Are you sure you want to exit?')
    askLabel.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    nobtn = tk.Button(quitDialog, text='Cancel', width=7, command=cancelQuit)
    nobtn.place(relx=0.35, rely=0.65, anchor=tk.CENTER)
    yesbtn = tk.Button(quitDialog, text='Exit', width=7,
                       command=lambda: Quit(root))
    yesbtn.place(relx=0.65, rely=0.65, anchor=tk.CENTER)


def primaryWindow():
    createCanvas()
    bgCanvas.create_text(675, 200, anchor=tk.CENTER, font=(
        'Calibre', '28'), text='Weather Forecast - Login')

    btn1 = addButtons(bgCanvas, 'Login', 20, 0.45, command=loginButtonClicked)
    btn2 = addButtons(bgCanvas, 'Sign Up', 20, 0.5,
                      command=signinButtonClicked)
    btn3 = addButtons(bgCanvas, 'Continue Without Sign-In',
                      20, 0.55, command=continueWithoutSignIn)
    btn4 = addButtons(bgCanvas, 'Quit', 10, 0.977,
                      relx=0.96, command=lambda: confirmDialog(root))
    btn1.createButton()
    btn2.createButton()
    btn3.createButton()
    btn4.createButton()

    root.mainloop()


def mainInterface():
    createCanvas()

    root.mainloop()


# Initial Log-In Window:
startRootWindow()
primaryWindow()

# Main Interface:
if loggedIn is True or guest is True:
    time.sleep(2)
    startRootWindow()
    mainInterface()
