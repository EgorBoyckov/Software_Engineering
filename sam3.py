import datetime as dt, time
def main():
    for i in range(5):
        print(dt.datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)
if __name__ == "__main__":
    main()