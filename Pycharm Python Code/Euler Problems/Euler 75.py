import numpy as np
import time
from collections import Counter

first = time.time()
loopLength = 10000000


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
    while L <= limit:

        for n in range(1, m):
            if oppParity(m, n) and gcd(m, n) == 1:

                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                L = a + b + c

                if L <= 1500000 and not a % 2 == 0:
                    primitives.append(sorted([a, b, c]))

        m += 1

    return primitives


def generate_nonPrimitives(primitives):
    triples = []
    divTrip = []
    dTriples = []
    mTriples = []

    for p in range(0, primitives.__len__()):


        if primitives[p][2] % 2 == 0:
            divTrip = [int(i * 0.5) for i in primitives[p]]
            dTriples.append(sorted(divTrip))

        multi = 2
        pLength = 0

        while pLength <= 1500000:

            mulTrip = [i * multi for i in primitives[p]]
            pLength = sum(mulTrip)

            if pLength <= 1500000:
                mTriples.append(mulTrip)

            multi += 1
    return mTriples + dTriples


def generate_triples():
    primitives = generate_primitives(loopLength)
    non_Primitives = generate_nonPrimitives(primitives)

    triples = primitives + non_Primitives
    triples = np.array(triples)

    return triples


def perimeter_list(triple):
    perimeters = []
    for t in triple:
        perimeters.append(sum(t))

    return perimeters


triples = generate_triples()
perimeters = perimeter_list(triples)

C = Counter(perimeters)

perimeters = [[k, ] * v for k, v in C.items()]

uniPerim = []
for P in perimeters:
    if len(P)== 1 :
        uniPerim.append(P[0])

print(len(uniPerim))

last = time.time()
print("Time Taken:", last - first, "secs")
