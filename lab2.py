# Определение класса Car, представляющего автомобиль
class Car:
    # Инициализация объекта класса Car с атрибутами make и model
    def __init__(self, make, model):
        self.make = make  # Марка автомобиля
        self.model = model  # Модель автомобиля

    # Метод drive, который выводит сообщение о том, что автомобиль едет
    def drive(self):
        print(f"Driving the {self.make} {self.model}")  # Вывод информации о марке и модели автомобиля

# Создание объекта класса Car с маркой "mak" и моделью "III"
my_car = Car("mak", "III")
# Вызов метода drive для объекта my_car
my_car.drive()
