import numpy as np
import  time
from collections import Counter

first = time.time()
targetLength = 10000000

def generate_primitives(limit):

    L = 0
    m = 1
    primitives = []
    i = 0
    while L <= limit:

        for n in range(1,m):

            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            L = a+b+c

            if L <= 1500000 and not a % 2 == 0:
                primitives.append(sorted([a,b,c]))

        m += 1

    return primitives

def generate_nonPrimitives(primitives):
    triples = []
    divTrip = []
    dTriples = []
    mTriples = []

    for p in range(0, primitives.__len__()):

        # Adding the primitive to the triple list.
        triples.append(primitives[p])

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

primitives = generate_primitives(targetLength)
non_Primitives = generate_nonPrimitives(primitives)

triples = primitives + non_Primitives
triples = np.array(triples)
#triples = np.unique(triples, axis=0)

print(triples)

last = time.time()
print("Time Taken:", last - first,"secs")