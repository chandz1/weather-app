import tkinter as tk


root = tk.Tk()
root.title('The Weather Forecast App')
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('{}x{}'.format(screenWidth, screenHeight))
root.maxsize(screenWidth, screenHeight)
frame = tk.Frame(root, bg="#0e95ec", padx=200, pady=200)
frame.pack(expand=True)
Header = tk.Label(frame, text='Weather Forecast - Login', bg='#0e95ec')
Header.config(font=('Ariel', '20'))
Header.grid()
btn1 = tk.Button(frame, text='Login', bg="#e3d6d6", width=20)
btn1.grid(padx=5, pady=5, row=1, column=0)
btn2 = tk.Button(frame, text='Create Account', bg="#e3d6d6", width=20)
btn2.grid(padx=5, pady=5, row=2, column=0)
btn3 = tk.Button(frame, text='Continue Without Sign-In', bg="#e3d6d6",
                 width=20)
btn3.grid(padx=5, pady=5, row=3, column=0)

root.mainloop()
