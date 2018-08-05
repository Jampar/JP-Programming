def is_prime(n):
    if n == 0:
        return False
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


complete = False
i = 3797
truncPrimes = []
variation = []

while not complete:
    varsPrime = False

    if is_prime(i):
        for n in range(0,len(str(i))):
            variation.append(str(i)[n:])
            variation.append(str(i)[:n])

        variation = list(filter(None, variation))
        variation = [int(x) for x in variation]
        print(variation)

    if (is_prime(item) for item in variation):
        truncPrimes.append(i)

    if len(truncPrimes) == 11:
        complete = True

    variation.clear()
    i += 1

print(sum(truncPrimes))
