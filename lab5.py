# Определение базового класса Shape, представляющего общую форму
class Shape:
    # Метод area, который должен быть определён в подклассах
    def area(self):
        pass  # Пустой метод, который переопределяется в дочерних классах

# Определение класса Rectangle, наследующего Shape
class Rectangle(Shape):
    # Инициализация объекта класса Rectangle с параметрами ширины и высоты
    def __init__(self, width, height):
        self.width = width    # Ширина прямоугольника
        self.height = height  # Высота прямоугольника

    # Переопределение метода area для вычисления площади прямоугольника
    def area(self):
        return self.width * self.height  # Площадь прямоугольника = ширина * высота

# Определение класса Circle, наследующего Shape
class Circle(Shape):
    # Инициализация объекта класса Circle с параметром радиуса
    def __init__(self, radius):
        self.radius = radius  # Радиус круга

    # Переопределение метода area для вычисления площади круга
    def area(self):
        return 3.14 * self.radius * self.radius  # Площадь круга = π * радиус^2

# Создание списка фигур, содержащего экземпляры Rectangle и Circle
arr = [Rectangle(12, 67), Circle(41)]

# Перебор элементов списка и вывод площади каждой фигуры
for elem in arr:
    print(elem.area())  # Вызов метода area для каждого объекта в списке
