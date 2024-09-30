from datetime import datetime as dt, timedelta as td
def main():
    n = int(input())
    t = dt.today()
    r = t + td(days=n)
    print(f"Через {n} дней будет {r.date()}." 
            f"день недели {r.isoweekday()}")
if __name__ == "__main__":
    main()