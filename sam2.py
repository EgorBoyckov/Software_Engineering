import random

def dice():
    a = random.randint(1,6)
    print(a)
    if 5 == a or a == 6:
        print("Вы победили")
    elif 3 == a or a == 4:
        print("Переброс")
        dice()
    else: print("Вы проиграли")

if __name__ == "__main__":
    dice()