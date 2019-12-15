import datetime


def dayofyear():
    year = input('please input the number of year: ')
    month = input('please input the number of month: ')
    day = input('please input the number of day: ')
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    print(date1)
    date2 = datetime.date(year=int(year), month=1, day=1)
    print(date2)
    days = (date1-date2).days + 1
    return days


if __name__ == '__main__':
    print(dayofyear())

