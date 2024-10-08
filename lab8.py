from random  import randint
def list_Rand():
    a = [randint(1,100)*randint(3,10)]
    return a
if __name__ == "__main__":
    result =[]
    for i in range(1,5):
        result.append(list_Rand())
    print(result)