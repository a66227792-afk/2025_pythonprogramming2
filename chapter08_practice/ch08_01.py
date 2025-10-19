import tkinter as tk
import random

class MovingshapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving shape App")
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.shape = self.canvas.create_oval(100,100,200,200, fill="blue")

        self.root.bind('<Up>', self.move_up)
        self.root.bind('<Down>', self.move_down)
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)

        self.canvas.bind('<B1-Motion>', self.change_color)
    
    def move_shape(self, dx, dy):
        self.canvas.move(self.shape, dx, dy)

    def move_up(self, event):
        self.move_shape(0,-10)
    def move_down(self, event):
        self.move_shape(0,10)
    def move_left(self, event):
        self.move_shape(-10,0)
    def move_right(self, event):
        self.move_shape(10,0)   
    
    def change_color(self, event):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        color = random.choice(colors)
        self.canvas.itemconfig(self.shape, fill=color)

root = tk.Tk()
app = MovingshapeApp(root)
root.mainloop()
