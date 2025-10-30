import tkinter as tk
def draw_rectangle():
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 150, 150, fill="red")
def draw_oval():
    canvas.delete("all")
    canvas.create_oval(200,80, 300, 180, fill="blue")
def draw_image():
    global img
    canvas.delete("all")
    canvas.create_image(5,5, anchor=tk.NW, image=img)
def draw_delete():
    canvas.delete("all")

root = tk.Tk()
root.title("중간고사 7번")
root.geometry("420x440")

img = tk.PhotoImage(file="duksung.png")

canvas = tk.Canvas(root, width=400, height=320, bg="white")
canvas.pack()

frame = tk.Frame(root)
frame.pack()

shape_var = tk.IntVar()
shape_var.set(1)
rectbutton = tk.Button(frame, text="사각형", command=draw_rectangle)
ovalbutton = tk.Button(frame, text="원", command=draw_oval)
imagebutton = tk.Button(frame, text="그림", command=draw_image)
deletebutton = tk.Button(frame, text="지우기", command=draw_delete)

rectbutton.pack(side=tk.LEFT, padx=10)
ovalbutton.pack(side=tk.LEFT, padx=10)
imagebutton.pack(side=tk.LEFT, padx=10)
deletebutton.pack(side=tk.LEFT, padx=10)

tk.Label(root, text="버튼을 눌러 도형을 선택하세요.").pack(pady=4)

root.mainloop()