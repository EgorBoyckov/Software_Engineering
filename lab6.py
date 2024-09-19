s = "Егор"
x = input()
for i in s:
    if i == x:
        print (f"символ {x} есть в строке")
        break
else:
    print("нету в строке")