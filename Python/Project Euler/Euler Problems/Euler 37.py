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


def all_primes(lista):
    """Check if all numbers in `lista` are primes."""
    return all(is_prime(n) for n in lista)

complete = False
i = 8
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
        variation.sort(key=int)

        if all_primes(variation):
            truncPrimes.append(i)

    variation.clear()

    if len(truncPrimes) == 11:
        complete = True

    i += 1

print(truncPrimes)
print(sum(truncPrimes))
