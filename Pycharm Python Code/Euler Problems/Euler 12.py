import math

def CheckNumFactor(n):

    FacNum = 0
    m = int(math.sqrt(n))

    for i in range(1,m + 1):
        if n % i == 0:
            FacNum += 1

    FacNum = FacNum * 2

    return FacNum

found = False
t = 0
x = 0
while found == False:
    if CheckNumFactor(t) >=500:
        found = True
        print(t)

    x += 1
    t += x
