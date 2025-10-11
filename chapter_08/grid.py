from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text="버튼1", fg ="white", bg="red")
button2 = Button(root, text="버튼2", fg="black", bg ="green")
button3 = Button(root, text="버튼3", fg="white", bg="blue")
button4 = Button(root, text="버튼4", fg="red", bg="yellow")

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)

root.mainloop()