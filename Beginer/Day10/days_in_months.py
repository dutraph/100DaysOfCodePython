def is_leap(_year):
    if _year % 4 == 0:
        if _year % 100 == 0:
            if _year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(_year, _month):
    if _month > 12 or _month < 1:
        return "invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(_year) and _month == 2:
        return 29
    else:
        return month_days[_month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)