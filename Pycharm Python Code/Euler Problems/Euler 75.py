import numpy as np
import  time

first = time.time()

L = 0
m = 1
targetLength = 1500000

primitives = []

while L <= targetLength:

    for n in range(1,m):

        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        L = a+b+c

        if L <= targetLength:
            primitives.append(sorted([a,b,c]))

    m += 1

triples = []
divTrip = []
dTriples = []
mTriples = []


for p in range(0,primitives.__len__()):

    #Adding the primitive to the triple list.
    triples.append(primitives[p])

    if primitives[p][2] % 2 == 0:
        divTrip = [int(i * 0.5) for i in primitives[p]]
        dTriples.append(sorted(divTrip))

    multi = 2
    pLength = 0

    while pLength <= targetLength:

        mulTrip = [i * multi for i in primitives[p]]
        pLength = sum(mulTrip)

        if pLength <= targetLength:
            mTriples.append(mulTrip)

        multi += 1


triples = triples + dTriples + mTriples
triples = np.array(triples)
triples = np.unique(triples, axis=0).tolist()

print(len(triples))

last = time.time()
print("Time Taken:", last - first,"secs")