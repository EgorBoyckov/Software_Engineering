def super(s1,s2):
    if s1 > s2:
        print(f"Чистое Супермножество {s1}")
    elif s2 > s1:
        print(f"Чистое Супермножество {s2}")
    elif s1 == s2:
        print("Множества равны")
    else:
        print("Супермножества нет")

if __name__ == "__main__":
    super({2,34,51,1},{2,1,5,6,7})