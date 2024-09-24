array = [1,2,3,4,5,6,7,8]
flag =False
for i in array:
    if (i % 2 == 0):
        flag = True
if(flag == True):
    print("Есть чётные")
else: print("Нету")