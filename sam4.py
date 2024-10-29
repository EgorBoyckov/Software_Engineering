class Animal:
    def __init__(self,name, zzz):
        self._name = name
        self.__zzz = zzz
    def sayName(self):
        print(f"Меня ховут {self._name}")
    def sound(self):
        print(self.__zzz)
    def go(self):
        print("топ топ")
class dog(Animal):
    def __init__(self,name,zzz):
        super().__init__(name,zzz)
        
M = Animal("Корова","муму")
D = dog("Собака", "гав гав")
D.sound()