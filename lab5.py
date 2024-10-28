class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width # Ширина
        self.height = height # Высота

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius # Радиус

    def area(self):
        return 3.14 * self.radius * self.radius

arr = [Rectangle(12,67), Circle(41)]
for elem in arr:
    print(elem.area())