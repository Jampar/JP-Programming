import math as m
def FormNextNum(n):
    s = str(n)
    t = 0

    digits = [int(digit) for digit in s]

    for d in digits:
        n = d**2
        t += n
    print(t)
    return t

n1 = 0
n2 = 0
num = 0
for i in range(2,10000001):
    print("______________________________________________")
    print(i)
    while num != 1 or num != 89:
        if num == 0:
            num = FormNextNum(i)
        else:
            num = FormNextNum(num)
        if num == 89:
            n1 +=1
            break
        elif num == 1:
            n2 +=1
            break

print(n1)


