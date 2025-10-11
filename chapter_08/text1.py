from tkinter import *

def display_text():
    text = text_weight.get("1.0", END)
    print("입력된 정보:")
    print(text)

root = Tk()

#텍스트 위젯 
text_weight = Text(root, width=60, height=10)
text_weight.pack()

button = Button(root, text="출력", command = display_text)
button.pack()

root.mainloop()