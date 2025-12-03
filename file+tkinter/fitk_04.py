from tkinter import *

# 1. Vehicle 상속 구조 정의
class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("drive()는 자식 클래스에서 구현해야 합니다.")

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."

# 2. 파일 처리 함수
def append_log(message):
    with open("drive_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def clear_log_file():
    with open("drive_log.txt", "w", encoding="utf-8") as f:
        pass 

# 3. Tkinter GUI
root = Tk()
root.title("문제4")
root.geometry("400x320")

Label(root, text="차량 이름을 입력하세요:").pack(pady=5)

# 차량 이름 입력 Entry
name_entry = Entry(root, width=20)
name_entry.pack(pady=5)

result_label = Label(root, text="결과가 여기에 표시됩니다.")
result_label.pack(pady=10)

# 4. 버튼 이벤트 함수
def drive_car():
    name = name_entry.get().strip()
    if name == "":
        name = "이름없음"

    car = Car(name)  
    message = car.drive()
    append_log(message)
    result_label.config(text=message)

def drive_truck():
    name = name_entry.get().strip()
    if name == "":
        name = "이름없음"

    truck = Truck(name)  
    message = truck.drive()
    append_log(message)
    result_label.config(text=message)

def clear_log():
    clear_log_file()
    result_label.config(text="로그 파일을 비웠습니다.")

# 버튼 프레임
frame = Frame(root)
frame.pack(pady=15)

Button(frame, text="자동차 주행", width=15, command=drive_car).pack(pady=3)
Button(frame, text="트럭 주행", width=15, command=drive_truck).pack(pady=3)
Button(frame, text="로그 비우기", width=15, command=clear_log).pack(pady=3)

root.mainloop()
