import math as m
complete = False
m = 0
lengths = []
limit = 100000000
while not complete:

    m += 1
    l =0
    for n in range(1,m):
            a = 2 * m * n
            b = m**2 - n**2
            c = m**2 + n**2

            l = a+b+c
            if l == 120:
                print(a, b, c)

    if m >= limit:
        complete = True