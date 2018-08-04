from collections import deque


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def shift(list):
    new_list = []

    for i in list:
        new_list.insert(len(new_list)-1, i)

    return new_list

def FindAllRotations(n):
    rots = []

    digits = [int(k) for k in str(n)]

    for d in range(0,len(digits)):
        digits = shift(digits)
        rots.append(int(''.join(str(x) for x in digits)))

    return  rots

complete = False
i = 0
p = 0
primeChain = True

cirPrimes = []

while not complete:

    cirPrimes.append(i)

    if i == 1000000:
        complete = True

    rot = FindAllRotations(i)

    for n in rot:

        if not is_prime(n):
            if cirPrimes.__contains__(i):
                cirPrimes.remove(i)


    i+=1

print(len(cirPrimes))