def banWords(text,banlist):
    text = text.lower()
    for i in banlist:
        text = text.replace(i,len(i)*"*")
    return text
test = 'Hello, world! Python IS the programming language of thE future. My EMAIL is....\nPYTHON is awesome!!!!'
with open("14.txt", "r") as f:
    ban= f.read().strip().split()
print(banWords(test,ban))