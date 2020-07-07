import tkinter as tk


# class userAccounts:
#     def __init__(self):
#         self.

root = tk.Tk()
root.title("The Weather Forecast App")
root.geometry('1280x720')
frame = tk.Frame(root, bg="#1c1b1b", width=500, height=500)
frame.pack()
# bgImgFile = tk.PhotoImage(file='CloudsBg.gif')
# imgLabel = tk.Label(frame, image=bgImgFile)
# imgLabel.pack()
btn = tk.Button(root, bg='#00ff85')
btn.pack()
root.mainloop()
