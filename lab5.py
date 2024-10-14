def func(tpl):
    for elem in tpl:
        if not isinstance(elem, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(func((1,3,5,24,113)))
    print(func((5,32,1,4, '2', 3)))