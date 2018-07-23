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

x = 0
y = 0
while x < 10001:
    y = y+1
    if FindPrimes(y) == True:
        x = x + 1

print(y)
