class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"메뉴 : {self.name}, 가격 : {self.price}원"
class DeliveryFood(Food):
    def __init__(self, name, price, delivery_free):
        super().__init__(name, price)
        self.delivery_free = delivery_free
    def __str__(self):
        total_price = self.delivery_free + self.price
        return f"메뉴 : {self.name}, 총 가격 : {total_price}원(배달비 포함)"
class Order:
    def __init__(self):
        self.foods = []
    def add_food(self, food):
        self.foods.append(food)
    def show_order(self):
        print("===주문 내역===")
        for f in self.foods:
            print(f)

f1 = Food("김밥", 3000)
f2 = DeliveryFood("짜장면", 6000, 2000)

order = Order()
order.add_food(f1)
order.add_food(f2)
order.show_order()