def func(name, age, comp = 'unnamed'):
    print(f"Имя: {name}. Возраст: {age}. Место работы: {comp}.")

user1 = ("Вася", 12)
func(*user1)

user2 = ("Егор", 21, "Yandex")
func(*user2)