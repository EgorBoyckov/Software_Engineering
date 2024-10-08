a = [1, 1, 3, 3, 1]
b = [5, 5, 5, 5, 5, 5, 5]
c = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
def F(lst):
    R = set()
    for number in lst:
        count = lst.count(number)
        if count > 1:
            R.add(str(number) * count)
            for i in range(2, count):
                R.add(str(number) * i)
        R.add(number)
    return R
print(F(a))
print(F(b))
print(F(c))