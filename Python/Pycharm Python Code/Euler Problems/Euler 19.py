import calendar as c
i = 0

c.setfirstweekday(c.MONDAY)

def adaptMonth(month, year):
    if month == 11 or month == 4 or month == 6 or month == 9:
        return 30
    elif month == 2 and c.isleap(year) is True:
        return 29
    elif month == 2 and c.isleap(year) is False:
        return 28
    else:
        return 31

for y in range(1901,2001):
    for m in range(1,13):
        limit = adaptMonth(m,y)
        for d in range(1,limit+1):
            if d == 1 and c.weekday(y,m,d) == 6:
                i = i + 1

print(i)