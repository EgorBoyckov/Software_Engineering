def countW(file):

    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.count('\n') + 1
    words = len(text.split())
    letters = sum(1 for char in text if char.isalpha())
    print(lines)
    print(words)
    print(letters)

countW('13.txt')