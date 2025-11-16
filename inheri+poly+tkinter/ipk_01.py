from tkinter import *

class Vehicle:
    def __init__(self, name):
        self.name = name
    def drive(self):
        pass
class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."
class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."


car1 = Car("car1")
truck1 = Truck("truck1")

def show_car():
    result.set(car1.drive())
def show_truck():
    result.set(truck1.drive())

root = Tk()
root.geometry("400x300")
root.title("문제1")

Label(root, text="버튼을 눌러보세요.", font=("맑은 고딕", 11)).pack(pady=10)
frame = Frame(root)
frame.pack(pady=10)
Button(frame, text="자동차 주행", command=show_car).pack(side="left", padx=10)
Button(frame, text="트럭 주행", command=show_truck).pack(side="left", padx=10)
result = StringVar()
result_label = Label(root, textvariable=result, font=('맑은 고딕', 11))
result_label.pack(pady=10)

root.mainloop()