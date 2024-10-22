def analys(F):
    with open(F,"r",encoding="utf-8") as f:
            t = f.read()
            w = t.split()
            count = len(w)
            collection = {}
            for i in w:
                i = i.lower()
                if i in collection:
                    collection[i] += 1
                else:
                    collection[i] = 1

            V = ""
            count_L = 0
            for i, y in collection.items():
                if y > count_L:
                    count_L = y
                    V = i

            print(count , V ,  count_L)
            return 0
print(analys("text.txt"))
