def mathAnimal(f):
    with open(f, "r", encoding="utf-8") as f:
        t = f.read()
        w = t.split()
        collection = {}
        for i in w:
            if i in collection:
                    collection[i] += 1
            else:
                    collection[i] = 1
    return max(collection)
print(mathAnimal("15.txt"))