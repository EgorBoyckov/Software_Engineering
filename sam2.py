class Animal:
    def __init__(self,name, zzz):
        self.name = name
        self.zzz = zzz
    def sayName(self):
        print(f"Меня ховут {self.name}")
    def sound(self):
        print(self.zzz)
    def go(self):
        print("топ топ")
M = Animal("Корова","муму")
M.sayName()
M.sound()
M.go()