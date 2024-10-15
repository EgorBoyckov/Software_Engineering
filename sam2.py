def del_num(arr, num):
    s =[]
    flag = True
    for i in range(len(arr)):
        if arr[i] == num and flag:
            flag =False
        else:
            s.append(arr[i])
    return tuple(s)

print(del_num((1, 2, 3), 1))
print(del_num((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(del_num((2, 4, 6, 6, 4, 2), 9))