def V(arr, a):
    flag = True
    if a in arr:
        for i in range(len(arr)):
            if arr[i] == a and flag:
                start = i
                flag =False
            elif arr[i] ==a and flag == False:
                end = i+1
                break
            elif arr[i] == arr[-1]:end = i+1
    else: return ()
    return arr[start:end]
print(V((1, 2, 3), 8))
print(V((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(V((1, 2, 8, 5, 1, 2, 9), 8))