def sumNumber(a,b):
    try:
        return a + b
    except TypeError:
        return ("Неподходящий тип данных. Ожидалось число")
if __name__ == "__main__":
    print(sumNumber(2,"2"))
    print(sumNumber(21,19))