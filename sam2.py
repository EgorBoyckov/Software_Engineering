while True:
    print ("1 ввести данные о расходах 2 вывести данные о расходах")
    i = int(input())
    if i == 1:
        with open("buget.txt", 'a', encoding = 'utf-8') as f:
            f.write(input()+"\n")
    elif i ==2:
        with open('buget.txt', 'r', encoding = 'utf-8') as file:
            for line in file:
                print(line)