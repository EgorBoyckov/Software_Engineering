a = input()

def count_num(a):
    
    x ={}
    for i in range(9):
        n = a.count(str(i))
        x [i] = n
    x = sorted(x.items(), key = lambda item: item[1], reverse =True)
    return x[:3]
print(count_num(a))