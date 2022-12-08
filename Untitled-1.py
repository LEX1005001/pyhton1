# класс Машина
class Car:
    # конструктор класс
    def __init__(
        self,
        number: str, # номер машины
        color: str,  # цвет машины
        wheels: int  # кол-во колёс
    ):
        self.number = number # номер машины
        self.color  = color  # цвет машины
        self.wheels = wheels # кол-во колёс

        self.distance = 0    # пробег машины

    def move(self):
        self.distance += 1
        print(f"{self.number} distance: {self.distance} km")

    # функция перекраски машины
    def repaint(self, color: str):
        self.color = color

car1 = Car("A125AB", "red", 4)
car2 = Car("H255AH", "black", 6)

print(car1.color)
car1.repaint("yellow")
print(car1.color)