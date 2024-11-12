class ZeroInputException(Exception):
    pass
def readFile(F):
    try:
        with open (F , "r") as file:
            data = file.read()
            if data == "":
                raise ZeroInputException("Пустой файл")
            print(data)
    except ZeroInputException as e:
        print(e)

if __name__ == '__main__':
    readFile("input1.txt")
    readFile("input2.txt")

