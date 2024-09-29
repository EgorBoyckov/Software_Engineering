def main (*args):
    x = max(args)
    y = sum(args)
    return y / x + 1
if __name__ == "__main__":
    print(main(12,-43,12,56,888,13))