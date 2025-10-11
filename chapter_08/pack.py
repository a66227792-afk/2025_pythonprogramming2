from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text="버튼1", fg="white", bg ="red")
button2 = Button(root, text="버튼2", fg ="black", bg="green")
button3 = Button(root, text="버튼3", fg ="white", bg ="blue")
button1.pack()
button2.pack()
button3.pack()

root.mainloop()