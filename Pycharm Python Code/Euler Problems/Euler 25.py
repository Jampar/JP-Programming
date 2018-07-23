import math as m
Found = False
i = 0
a = 0
b = 1
show = 0
fibs = []

while Found != True:
    show = a + b
    a = b
    b = show
    i += 1

    fibs.append(show)

    if str(show).__len__() >= 1000:
        print(fibs.__len__())
        Found = True
