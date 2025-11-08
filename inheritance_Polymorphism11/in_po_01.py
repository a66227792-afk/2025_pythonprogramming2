class Car:
    def __init__(self, speed):
        self.speed = speed
    def get_speed(self):
        return f"현재 속도 : {self.speed}km/h"
class SportsCar(Car):
    def __init__(self, speed, turbo):
        super().__init__(speed)
        self.turbo = turbo
    def get_speed(self):
        if self.turbo:
            return (f"현재 속도 : {self.speed}km/h (터보 ON)")
        else:
            return (f"현재 속도 : {self.speed}km/h (터보 OFF)")

car1 = Car(80)
print(car1.get_speed())

sports1 = SportsCar(150, True)
print(sports1.get_speed())

sports2 = SportsCar(120, False)
print(sports2.get_speed())