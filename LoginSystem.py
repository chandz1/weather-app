import tkinter as tk
from PIL import Image, ImageTk


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
                           height=self.height, bg=self.bgcolor)
        button.place(relx=self.relx, rely=self.rely, anchor=tk.CENTER)


# Initial Window Creation:
root = tk.Tk()
root.title('The Weather Forecast App')
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('{}x{}'.format(screenWidth, screenHeight))
root.maxsize(screenWidth, screenHeight)

# Assigning Background Image
bgImage = ImageTk.PhotoImage(Image.open('CloudsBg.gif'))

# Creating Canvas:
bgCanvas = tk.Canvas(root, bg='#15adc2')
bgCanvas.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
bgCanvas.create_image(450, 250, image=bgImage)
bgCanvas.create_text(678, 200, anchor=tk.CENTER, font=(
    'Ariel', '28'), text='Weather Forecast - Login')

# Creating Buttons:
btn1 = addButtons('Sign-In', 20, rely=0.45)
btn2 = addButtons('Sign-Up', 20, rely=0.5)
btn3 = addButtons('Continue Without Sign-In', 20, rely=0.55)
btn1.createButton()
btn2.createButton()
btn3.createButton()


root.mainloop()
