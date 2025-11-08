from tkinter import *

class Animal:
    def speak(self):
        return ""
class Dog(Animal):
    def speak(self):
        return "멍멍!"
class Cat(Animal):
    def speak(self):
        return "야옹!"
class Duck(Animal):
    def speak(self):
        return "꽥꽥!"

def make_sound(animal:Animal): #animal은 Animal클래스 객체 
    sound = animal.speak()
    label.config(text=sound)

    
root = Tk()
root.title("동물 소리 듣기")
root.geometry("360x180")
root.resizable(False, False) 
Label(root, text="동물 버튼을 눌러 소리를 들어보세요.").pack(pady=(12,6))

butFrame = Frame(root)
butFrame.pack(pady=4)

Button(butFrame, text="강아지", command=lambda:make_sound(Dog())).pack(side=LEFT, padx=5)
Button(butFrame, text="고양이", command=lambda:make_sound(Cat())).pack(side=LEFT, padx=5)
Button(butFrame, text="오리", command=lambda:make_sound(Duck())).pack(side=LEFT, padx=5)
label = Label(root, text="(여기에 울음소리가 나옵니다)", font=("맑은 고딕", 14, "bold"))
label.pack(pady=16)

root.mainloop()