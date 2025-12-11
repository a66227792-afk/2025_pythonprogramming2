from tkinter import *
import random 

class DrawbleShape:
    def __init__(self, canvas):
        self.canvas = canvas
    def draw(self):
        pass
class Square(DrawbleShape):
    def __init__(self, canvas, x, y, size):
        super().__init__(canvas)
        self.x = x
        self.y = y
        self.size = size
    def draw(self):
        self.canvas.create_rectangle(self.x, self.y, self.x+self.size, self.y+self.size)
class Circle(DrawbleShape):
    def __init__(self, canvas, x, y, radius):
        super().__init__(canvas)
        self.x = x
        self.y = y
        self.r = radius
    def draw(self):
        self.canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)

def add_rect():
    x = random.randint(50, 250)
    y = random.randint(50, 200)
    size = random.randint(10,50)
    s = Square(canvas, x, y, size)
    shapes.append(s)
def add_circle():
    x = random.randint(50, 250)
    y = random.randint(50, 200)
    radius = random.randint(10,50)
    c = Circle(canvas, x, y, radius)
    shapes.append(c)
def all_draw():
    for shape in shapes:
        shape.draw()
    

root = Tk()
root.title("문제1")
shapes = []

frame = Frame(root)
frame.pack(pady=8)
canvas = Canvas(frame, width=400, height=300)
canvas.pack(side="right")

result=StringVar(value="생성된 도형 목록")
result_label = Label(frame, textvariable=result)
result_label.pack(side="left")

ftn_frame = Frame(root)
ftn_frame.pack(pady=8)

Button(ftn_frame, text="사각형 추가", command=add_rect).pack(padx=6, side="left")
Button(ftn_frame, text="원 추가 추가", command=add_circle).pack(padx=6,  side="left")
Button(ftn_frame, text="모두 그리기", command=all_draw).pack(padx=6,  side="left")

root.mainloop()