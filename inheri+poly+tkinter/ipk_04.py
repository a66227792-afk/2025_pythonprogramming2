from tkinter import *

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes = []
    def enrollCourse(self, subject):
        if subject not in self.classes:
            self.classes.append(subject)
    def clearCourse(self):
        self.classes.clear()

root = Tk()
root.title("문제4")
root.geometry("380x280")

stu = Student("홍길동")
title = Label(root, text=f"학생 : {stu.name}", font=("맑은 고딕", 11))
title.pack(pady=6)

frame = Frame(root)
frame.pack(pady=8, anchor="center")

var_py = IntVar(value=0)
var_ai = IntVar(value=0)
var_ds = IntVar(value=0)

cb1 = Checkbutton(frame, text="python", variable=var_py)
cb2 = Checkbutton(frame, text="ai", variable=var_ai)
cb3 = Checkbutton(frame, text="datascience", variable=var_ds)

cb1.grid(row=0, column=0, padx=8, pady=4)
cb2.grid(row=0, column=1, padx=8, pady=4)
cb3.grid(row=0, column=2, padx=8, pady=4)

result = StringVar(value="과목을 선택하고 [등록하기]를 누르세요.")
lb = Label(root, textvariable=result, wraplength=340, justify="left")
lb.pack(pady=8)

btn_frame = Frame(root)
btn_frame.pack(pady=6)
def register_courses():
    stu.clearCourse()
    if var_py.get():
        stu.enrollCourse("python")
    if var_ai.get():
        stu.enrollCourse("ai")
    if var_ds.get():
        stu.enrollCourse("datascience")
    if stu.classes:
        result.set(f"등록된 과목 : {', '.join(stu.classes)}")
    else:
        result.set("선택된 과목이 없습니다.")
def reset_all():
    var_py.set(0)
    var_ai.set(0)
    var_ds.set(0)
    stu.clearCourse()
    result.set("모든 선택을 해제했습니다.")

Button(btn_frame, text="등록하기", command=register_courses).pack(side="left", padx=8)
Button(btn_frame, text="초기화", command=reset_all).pack(side="left", padx=8)

root.mainloop()