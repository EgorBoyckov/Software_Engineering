with open("test.txt", "a+") as f:
    f.write("\n Super man")
with open("test.txt", "r") as f:
    print(f.readlines())