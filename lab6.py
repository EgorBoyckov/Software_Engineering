def main(**kwargs):
    for i, j in kwargs.items():
        print(i, mean(j))
def mean(d):
    return sum(d) / float(len(d))

if __name__ == "__main__":
    main(a=[1,2,3],y=[45,-2,0])