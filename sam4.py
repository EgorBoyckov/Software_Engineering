x = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
y = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
z = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
def F(a):
    i =0
    while i < len(a):
        if  a[i] == 2:
            a.pop(i)
            i-=1
        elif a[i] == 3:
            a[i] = 4
        i+=1
    return a
print(F(x))
print(F(y))
print(F(z))
