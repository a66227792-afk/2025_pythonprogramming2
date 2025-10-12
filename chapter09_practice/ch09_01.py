class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f'{self.name}가 짖고 있습니다!')

dog1 = Dog('바둑이', 3)
dog2 = Dog('멍멍이', 5)

dog1.bark()
dog2.bark()


        