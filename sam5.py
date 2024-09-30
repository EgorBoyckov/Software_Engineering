import math
def F(a, b, c):
    x = (a+b+c)/2
    result = math.sqrt(x*(x-a)*(x-b)*(x-c))
    return result

