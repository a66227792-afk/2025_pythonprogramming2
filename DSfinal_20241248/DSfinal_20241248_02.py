import tkinter as tk

class Person:
    def __init__(self, name: str):
        self.name = name

class HobbyPerson(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.hobbies = []  # has-a: 수강 과목 리스트

    def add_hobby(self, hobby: str):
        if hobby not in self.hobbies:
            self.hobbies.append(hobby)

    def clear_hobbies(self):
        self.hobbies.clear()

root = tk.Tk()
root.title("문제 2")
root.geometry("380x280")

person = HobbyPerson("김덕성") #객체 생성
title = tk.Label(root, text=f"이름: {person.name}", font=("맑은 고딕", 11, "bold"))
title.pack(pady=6)

frm = tk.Frame(root)
frm.pack(pady=8, anchor="center")

selection_hobby = tk.StringVar(value=0)

# Checkbutton 3개
cb1 = tk.Radiobutton(frm, text="Python",      variable =selection_hobby, value="game")
cb2 = tk.Radiobutton(frm, text="AI",          variable=selection_hobby, value="read")
cb3 = tk.Radiobutton(frm, text="DataScience", variable=selection_hobby, value="pt")

cb1.grid(row=0, column=0, padx=8, pady=4)
cb2.grid(row=0, column=1, padx=8, pady=4)
cb3.grid(row=0, column=2, padx=8, pady=4)

# 결과 표시 라벨
result = tk.StringVar(value="취미를 선택하고 [등록하기]를 누르세요.")
lb = tk.Label(root, textvariable=result, wraplength=340, justify="left")
lb.pack(pady=8)

# 동작 함수들
def register():# 현재 체크 상태를 기준으로 과목 리스트 갱신
    value = selection_hobby.get()
    if value=="game":
        person.add_hobby("게임")
    if value =="read":
        person.add_hobby("독서")
    if value=="pt":
        person.add_hobby("운동")
    result.set(f"현재 선택된 취미 : {" ".join(person.hobbies)}")
    

def reset_all():
    person.clear_hobbies()
    selection_hobby.set(0)
    result.set("모든 선택을 해제했습니다.")

# 버튼 영역
btn_frame = tk.Frame(root)
btn_frame.pack(pady=6)

tk.Button(btn_frame, text="등록하기", command=register).pack(side="left", padx=8)
tk.Button(btn_frame, text="초기화",   command=reset_all).pack(side="left", padx=8)

root.mainloop()