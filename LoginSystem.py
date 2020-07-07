import tkinter as tk
import tkinter


root = tkinter.Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
canvasProp = {'width': screenWidth, 'height': screenHeight, 'bg': '#e4b119'}
root.geometry(f'{screenWidth}x{screenHeight}')
root.maxsize(screenWidth, screenHeight)
# canvas = tkinter.Canvas(root, cnf=canvasProp).pack()
frame = tkinter.Frame(root, bg="black", width=500,
                      height=500).grid(padx=50, pady=125)
# frame.pack(expand=True)


root.mainloop()
