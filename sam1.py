class Animal:
    def __init__(self,name, zzz):
        self.name = name
        self.zzz = zzz
    def sayName(self):
        print(f"Меня ховут {self.name}")
    def sound(self):
        print(self.zzz)
M = Animal("Корова","муму")
M.sayName()
M.sound()