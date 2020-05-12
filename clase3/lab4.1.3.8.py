def isYearLeap(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def daysInMonth(year, month):
    if month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return None


def dayOfYear(year, month, day):
    days = day
    cont = 1
    while cont < month:
        days += daysInMonth(year, cont)
        cont += 1

    return days


print(dayOfYear(2000, 2, 20))
