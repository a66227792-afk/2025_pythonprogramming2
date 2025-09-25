from tkinter import *

root =Tk()
photo = PhotoImage(file=r"D:\python2_2025\2025_pythonprogramming2\chapter_08\dog.gif")
label= Label(root, image=photo)
label.pack()
root.mainloop()
