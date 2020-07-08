from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('The Weather Forecast App')
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('{}x{}'.format(screenWidth, screenHeight))
root.maxsize(screenWidth, screenHeight)
bgImage = ImageTk.PhotoImage(Image.open('CloudsBg.gif'))
bgCanvas = Canvas(root, bg='#15adc2')
bgCanvas.pack(expand=True, fill=BOTH, side=TOP)
bgCanvas.create_image(450, 250, image=bgImage)
bgCanvas.create_text(150, 150, text='Weather Forecast - Login')
# Header.config(font=('Ariel', '20'))
# Header.pack(side=TOP, expand=True)
btn1 = Button(bgCanvas, text='Login', bg="#e3d6d6", width=20)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
# btn2 = Button(bgCanvas, text='Create Account', bg="#e3d6d6", width=20)
# btn2.pack(side=TOP)
# btn3 = Button(bgCanvas, text='Continue Without Sign-In', bg="#e3d6d6",
#               width=20)
# btn3.pack(side=TOP)

root.mainloop()
