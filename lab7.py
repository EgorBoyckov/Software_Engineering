lines = ['one', 'two', 'three']
with open ('test.txt', 'w') as file:
    for line in lines:
        file.write('\nCycle run ' + line)
    print('Готово')