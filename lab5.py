def main(**kwargs):
    for  i in kwargs.items():
        print(i[0], i[1])

if __name__ == "__main__":
    main(a=[1,2,3],y=[45,-2,0])