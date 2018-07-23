import math as m
def SumOfDigits(n):
    sNum = str(n)
    digits = [int(i)for i in sNum]
    return sum(digits)

fNum = m.factorial(100)
print(SumOfDigits(fNum))