global result

def tr():
    a = float(input())
    b = float(input())
    global result
    result = 0.5 * a * b
def per():
    a = float(input())
    b = float(input())
    global result
    result =  a * b

x = input()
if x == "1":
    per()
elif x =="2":
    tr()
print(result)