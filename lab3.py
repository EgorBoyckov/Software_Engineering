# Определение класса Car, представляющего обычный автомобиль
class Car:
    # Инициализация объекта класса Car с атрибутами make и model
    def __init__(self, make, model):
        self.make = make  # Марка автомобиля
        self.model = model  # Модель автомобиля

    # Метод drive, который выводит сообщение о том, что автомобиль едет
    def drive(self):
        print(f"Driving the {self.make} {self.model}")  # Вывод информации о марке и модели автомобиля

# Определение класса ElectricCar, который наследует класс Car
class ElectricCar(Car):
    # Инициализация объекта класса ElectricCar с дополнительным атрибутом battery_capacity
    def __init__(self, make, model, battery_capacity):
        # Вызов конструктора базового класса Car для инициализации make и model
        super().__init__(make, model)
        self.battery_capacity = battery_capacity  # Емкость батареи в киловатт-часах (kWh)

    # Метод charge, который выводит сообщение о зарядке электромобиля
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")  # Вывод информации о процессе зарядки

# Создание объекта класса ElectricCar с маркой "mak", моделью "IV" и емкостью батареи 111 kWh
my_electric_car = ElectricCar("mak", "IV", 111)
# Вызов метода drive для объекта my_electric_car
my_electric_car.drive()
# Вызов метода charge для объекта my_electric_car
my_electric_car.charge()
