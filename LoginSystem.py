import tkinter as tk
from PIL import Image, ImageTk


# Classes:
class addButtons(tk.Canvas):
    def __init__(self, text, width, rely, relx=0.5, height=1,
                 bgcolor='#e3d6d6', command=None):
        super().__init__()
        self.text = text
        self.width = width
        self.height = height
        self.rely = rely
        self.relx = relx
        self.bgcolor = bgcolor
        self.command = command

    def createButton(self):
        button = tk.Button(bgCanvas, text=self.text, width=self.width,
                           height=self.height, bg=self.bgcolor,
                           command=self.command)
        button.place(relx=self.relx, rely=self.rely, anchor=tk.CENTER)


# Functions:
def loginButtonClicked(root):
    pass


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


def Quit():
    root.destroy()


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
bgCanvas.create_text(678, 200, anchor=tk.CENTER, font=(
    'Calibre', '28'), text='Weather Forecast - Login')

# Creating Buttons:
btn1 = addButtons('Sign-In', 20, 0.45)
btn2 = addButtons('Sign-Up', 20, 0.5)
btn3 = addButtons('Continue Without Sign-In', 20, 0.55)
btn4 = addButtons('Quit', 10, 0.977, relx=0.96, command=confirmDialog)
btn1.createButton()
btn2.createButton()
btn3.createButton()
btn4.createButton()


root.mainloop()
