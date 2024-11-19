def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

c = 1
for i in fib(222):
    print(c, i)
    c += 1