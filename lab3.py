class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value): #Установка значения атрибута
        self._value = value

    def get_value(self): #Получение значения атрибута
        return self._value

    def del_value(self): #Удаление атрибута
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

example = MyClass(30)
print(example.get_value())
example.set_value(50)
print(example.get_value())
example.set_value(100)
print(example.get_value())
example.del_value()
# вызов удалёного атрибута
print(example.get_value())
