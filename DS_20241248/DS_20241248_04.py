import tkinter as tk

def draw():
    select = choice.get()

    canvas.delete("all")

    if select == "rectangle":
        canvas.create_rectangle(100,100,200,200,fill = "red")
    elif select == "oval":
        canvas.create_oval(100,100,200,200,fill="blue")
    elif select == "text":
        canvas.create_text(200,200, text="Hello Duksung", fill="blue", font=("Helvetica", 20, "bold italic"))
    
root =tk.Tk()
root.title("중간고사 4번")
root.geometry("400x400")

canvas = tk.Canvas(root, bg="white")
canvas.pack()

choice = tk.StringVar()

tk.Radiobutton(root, text="사각형", variable=choice, value="rectangle").pack(side="left", padx=20)
tk.Radiobutton(root, text="원", variable=choice, value="oval").pack(side="left", padx=20)
tk.Radiobutton(root, text="텍스트", variable=choice, value="text").pack(side="left", padx=20)

tk.Button(root, text="그리기", command=draw).pack()

root.mainloop()
