x = int(input())
if 0 <= x <= 10:
    if 0 <= x <= 3:
        print("от 0 до 3 включительно")
    elif 3 < x < 6:
        print("от 3 до 6")
    elif 6 <= x <= 10:
        print("от 6 до 10 включительно")
else:
    print('стоп')