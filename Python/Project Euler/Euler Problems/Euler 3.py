target = 600851475143
primes = []

def IsPrime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
        # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

limit = 7000

for i in range(1,limit):
    if target % i == 0 :
         if IsPrime(i) == True:
            primes.append(i)
            print("Primes",primes)

c = primes[0] * primes[1] * primes[2]* primes[3]

print("Primes Multiplies: ", c)