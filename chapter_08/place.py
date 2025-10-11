from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text="버튼1", fg="white", bg="red")
button1.place(x=0, y=0)
button2 = Button(root, text="버튼2", fg="black", bg="green")
button2.place(x=30, y=30)
button3 = Button(root, text="버튼3", fg="white", bg="blue")
button3.place(x=60,y=60)

root.mainloop()