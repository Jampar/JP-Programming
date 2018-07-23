def d(n): # Sum of Proper Divisors
    divisors = []
    for i in range(1,round(n/2)+1):
        if n % i == 0:
            divisors.append(i)

    for x in range(0,divisors.__len__()):
        if divisors[x] == n:
            divisors.remove(x)

    s = sum(divisors)
    return s

amiNums = []

for a in range(0,10001):
    b = d(a)
    if a !=b:
        if d(b) == a:
            amiNums.append(a)
            amiNums.append(b)

amiNums = list(set(amiNums))
print(sum(amiNums))