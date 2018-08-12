import time as t
import numpy as np

start = t.time()

targetPerimeter = 100000000


def oppParity(m, n):
    if (m % 2 == 0 and not n % 2 == 0) or (n % 2 == 0 and not m % 2 == 0):
        return True
    else:
        return False


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_primitives(limit):
    L = 0
    m = 1
    primitives = []
    i = 0
    c = 0

    while c < targetPerimeter:

        for n in range(1, m):
            if oppParity(m, n) and gcd(m, n) == 1:

                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                L = a + b + c

                if L < targetPerimeter:
                    primitives.append([L, a, b, c])

        m += 1

    return primitives


def find_d(triples):
    dList = []
    for t in triples:
        dList.append(t[1] - t[2])

    return dList


def find_c(triples):
    cList = []
    for t in triples:
        cList.append(t[3])

    return cList


def generate_nonPrimitives(primitives):
    triples = []
    mTriples = []

    for p in range(0, primitives.__len__()):

        multi = 2
        pLength = 0

        while pLength < targetPerimeter:

            mulTrip = [i * multi for i in primitives[p]]
            pLength = sum(mulTrip)

            if pLength < targetPerimeter:
                mTriples.append(mulTrip)

            multi += 1

    return mTriples


prims = generate_primitives(100000000)
prims.sort()

diffs = find_d(prims)
cList = find_c(prims)

sqrList = []

for i in range(0, cList.__len__()):
    if cList[i] % diffs[i] == 0:
        sqrList.append(prims[i])

newSqrs = []
for s in sqrList:
    s.remove(s[0])
    newSqrs.append(s)

print(len(generate_nonPrimitives(newSqrs)+newSqrs))

end = t.time()

print("Time Taken = ", end - start)
