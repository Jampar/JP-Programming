import math as m

def FindPrimes(n):
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

primes = 0
bestprimes= 0
besta = 0
bestb = 0

for a in range(-1000,1001):
    print(a)

    for b in range(-1000, 1001):

        primes = 0
        for n in range(0,100):
            num = m.pow(n,2)+a*n+b

            if FindPrimes(num) == True:
                primes = primes+ 1
            else:
                break

        if primes > bestprimes:
            bestprimes = primes
            print(bestprimes)
            besta = a
            bestb = b

print(besta*bestb)
