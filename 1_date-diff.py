# '''
# The task is to count the number of days till feature release
# '''

from datetime import date

def main():
    day, month = map(int, input().split())              # feature release date
    cday, cmonth, cyear = map(int, input().split())     # current date
    if month < cmonth:
        year = cyear + 1
    else:
        year = cyear
    cdate = date(cyear, cmonth, cday)
    fdate = date(year, month, day)
    diff = fdate - cdate
    print(diff.days)
    return
    
if __name__ == "__main__":
    main()