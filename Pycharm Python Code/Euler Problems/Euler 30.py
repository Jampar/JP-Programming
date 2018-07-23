n = 1
power = 5
x = 0
while True:

    n += 1
    numSplit = [(i) for i in str(n)]
    total = 0


    for s in numSplit:
        total += int(s) ** power


    if total == n:
        print(n)
        x+=n
        print(x)
        print("")



