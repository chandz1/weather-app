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
class TopLevel():
    def __init__(self, title, geometry):
        self.title = title
        self.geometry = geometry

    def createTopLevel(self, master):
        global topLevel
        topLevel = tk.Toplevel(master)
        topLevel.grab_set()
        topLevel.title(self.title)
        topLevel.geometry(self.geometry)
        topLevel.resizable(0, 0)

    # def addWidgets(self, master):


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
    loginWindow = TopLevel('Login', '400x200')
    loginWindow.createTopLevel(root)
    labelUser = tk.Label(topLevel, text='Username',
                         font=('Calibre', '14'))
    labelUser.place(relx=0.25, rely=0.3, anchor=tk.CENTER)
    labelPass = tk.Label(topLevel, text='Password',
                         font=('Calibre', '14'))
    labelPass.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
    usernameInput = tk.Entry(topLevel)
    usernameInput.place(relx=0.65, rely=0.3, anchor=tk.CENTER)
    passwordInput = tk.Entry(topLevel, show='*')
    passwordInput.place(relx=0.65, rely=0.5, anchor=tk.CENTER)
    inputEntries.append(usernameInput)
    inputEntries.append(passwordInput)
    Loginbtn = addButtons(topLevel, 'Login', 10, 0.75,
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
            topLevel.destroy()
            loggedInPopUp()
        else:
            failedLabel = tk.Label(
                topLevel, text='Incorrect username or password.')
            failedLabel.place(relx=0.5, rely=0.15, anchor=tk.CENTER)


def loggedInPopUp():
    loggedInPopUp = TopLevel('Logged In', '300x100')
    loggedInPopUp.createTopLevel(root)
    loggedInLabel = tk.Label(
        topLevel, text='You have successfully been logged in.')
    loggedInLabel.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    okBtn = addButtons(topLevel, 'OK', 3, 0.7,
                       command=lambda: Quit(root))
    okBtn.createButton()


def signinButtonClicked():
    signupWindow = TopLevel('Sign Up', '400x200')
    signupWindow.createTopLevel(root)


def continueWithoutSignIn():
    global guest
    Quit(root)
    guest = True


def Quit(window):
    window.destroy()


def confirmDialog(window):
    quitDialog = TopLevel('Quit Confirmation', '300x90')
    quitDialog.createTopLevel(window)

    def cancelQuit():
        topLevel.destroy()
    askLabel = tk.Label(topLevel, text='Are you sure you want to exit?')
    askLabel.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    nobtn = tk.Button(topLevel, text='Cancel', width=7, command=cancelQuit)
    nobtn.place(relx=0.35, rely=0.65, anchor=tk.CENTER)
    yesbtn = tk.Button(topLevel, text='Exit', width=7,
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
