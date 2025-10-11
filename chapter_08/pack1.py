from tkinter import *

root = Tk()
root.geometry("300x100")

button1 = Button(root, text="버튼1", fg ="white", bg="red")
button2 = Button(root, text="버튼2", fg="black", bg ="green")
button3 = Button(root, text="버튼3", fg="white", bg="blue")

button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="left")

root.mainloop()