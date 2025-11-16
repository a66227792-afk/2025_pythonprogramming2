import math
from tkinter import *

class Shape:
    def __init__(self, x,y):
        self.x = x 
        self.y= y
    def area(self):
        raise NotImplementedError
    def perimeter(self):
        raise NotImplementedError
    def draw(self, canvas):
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.w+self.x, self.y+self.h, fill="tomato")
class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x,y)
        self.r = r
    def area(self):
        return self.r**2*math.pi
    def perimeter(self):
        return self.r*2*math.pi
    def draw(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill="skyblue")

root = Tk()
root.title("문제3")
canvas = Canvas(root, width=300, height=220, bg="white")
canvas.pack(pady=6)

var = StringVar(value="rect")
info = StringVar(value="도형을 선택하고 그리기를 누르세요")
Label(root, textvariable=info).pack()

frame = Frame(root)
frame.pack(pady=6, anchor="center")
Radiobutton(frame, text="사각형", variable=var, value="rect").pack(side="left", padx=6)
Radiobutton(frame, text="원", variable=var, value="circle").pack(side="left", padx=6)

def draw_shape():
    canvas.delete("all")
    if var.get() == "rect":
        s = Rectangle(50,50,100,60)
    else:
        s = Circle(150,110,40)
    s.draw(canvas)
    info.set(f"면적 = {s.area():.2f}, 둘레 : {s.perimeter():.2f}")
Button(root, text="그리기", command=draw_shape).pack(pady=6)

root.mainloop()