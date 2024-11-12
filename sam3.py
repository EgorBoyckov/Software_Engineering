def sumNumber(a,b):
    try:
        return a + b
    except TypeError as e:
        print(e)
        print("Неподходящий тип данных. Ожидалось число")
if __name__ == "__main__":
    sumNumber(2,"2")
    sumNumber(21,19)