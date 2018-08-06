def sieve(limit):
    bools = []
    primes = []

    # generate a list of booleans all set to True initially
    # the list is indexed from 2 to limit representing all numbers
    # e.g. [True, True, True, True] = [2, 3, 4, 5]
    for i in range(1, limit):
        bools.append(True)

    # loop from 2 to limit setting the composite numbers to False
    # we start from 2 because we know 1 is not a prime number
    for i in range(2, limit):
        if bools[i - 2]:
            for j in range(i * 2, limit + 1, i):
                bools[j - 2] = False

    # now generate the list of primes only where
    # there is a True value in the bools list
    for p in range(0, len(bools)):
        if (bools[p]):
            primes.append(p + 2)

    return primes

coinValues = sieve(1000)
amount = 100

combinations = [0] * (amount + 1)
combinations[0] = 1

for coin in coinValues:
    for i in range(1,combinations.__len__()):
        if i >= coin:
            combinations[i] += combinations[i-coin]

for c in range(0,len(combinations)):
    if combinations[c] > 5000:
        print(combinations[c])
        print(c)
        break
