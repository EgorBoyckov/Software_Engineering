import math
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
def P(a,b,c):
    x =(a + b + c) / 2
    return math.sqrt(x * (x - a) * (x - b) * (x - c))
MAX = P(max(one),max(two),max(three))
MIN = P(min(one),min(two),min(three))
print(MAX)
print(MIN)
