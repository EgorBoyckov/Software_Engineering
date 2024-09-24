x= 4
while(-12 < x <=256):
    if (x % 2 == 0 ):
        x*=2
    elif(x > 30):
        x//=2
        x+=2
    else: x+=13
    print(x)