s = input()
g = ["а", "е", "і", "о", "u"]
if (s.startswith('The') and s.endswith('end')):
    print("начинается  предложение с The и заканчивается  на end")
s = s.lower()
c = 0
for i in s:
    if(i in g):
        c+=1
s = s.replace('ugly', 'beauty')
print(len(s))
print(s)