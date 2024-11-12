import time
def decorFib(func):
    def apper(*a,**k):
        start = time.time()
        r = func(*a,**k)
        end = time.time()
        resultTime = end - start
        print("\n время выполнения"+ str(resultTime))
        return r
    return apper

@decorFib
def fibonacci():
    fib1 = fib2 = 1

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end = ' ')

if __name__ == '__main__':
    fibonacci()