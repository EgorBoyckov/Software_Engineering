#Создание класса Car
class Car:
    #Метод инициализации класса
    def __init__(self, make, model):
        #Присваивание параметров make и model атрибутам экземпляра
        self.make = make
        self.model = model

#Создание экземпляра класса Car с производителем mak и моделью III
car = Car("mak", "III")