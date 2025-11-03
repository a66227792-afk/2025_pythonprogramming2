import tkinter as tk
def login():
    id1 = id_entry.get()
    name = name_entry.get()

    stu = Student(id1, name)

    if stu in students:
        resultlabel.config(text=f"{stu.name}학생 로그인 성공 !", fg="blue")
    else:
        resultlabel.config(text="등록되지 않은 학번입니다.", fg="red")
    name_entry.delete(0,tk.END)
    id_entry.delete(0, tk.END)


root = tk.Tk()
root.title("중간고사 5번")
root.geometry("250x150")

class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.stu_id == other.stu_id
    

students = [Student("202501", "김민수"), Student("202502", "이수정"), Student("202503", "박지훈")]

tk.Label(root, text="학번").grid(row=0)
tk.Label(root, text="이름").grid(row=1)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

loginbutton = tk.Button(root, text="로그인",command=login)
quitbutton = tk.Button(root, text="취소", command=root.quit)

loginbutton.grid(row=3, column=0, sticky=tk.W, pady=4)
quitbutton.grid(row=3, column=1, sticky=tk.W, pady=4)

resultlabel = tk.Label(root)
resultlabel.grid(row=4, pady=5)

root.mainloop()