import math as m

complete = False
iterator = 0
uninterrupt = 0

def FacDigitSum(n):
    digits = [int(k) for k in str(n)]

    total = 0
    for d in digits:
        total += m.factorial(int(d))

    return total

while not complete:

    if iterator == FacDigitSum(iterator):
        uninterrupt = 0
        print(iterator)

    if uninterrupt == 1000000:
        complete = True

    uninterrupt += 1
    iterator += 1