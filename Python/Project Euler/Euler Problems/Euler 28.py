seqLength = 501
start = 2

Narray = []
Tvalue = 0

#TL
for n in range(start-1,seqLength+1):

    N = (4*n**2 -6*n +3)
    Narray.append(N)

print(Narray)

Tvalue = Tvalue + sum(Narray)
Narray.clear()

#TR
for n in range(start,seqLength+1):

    N = (4*n**2 -4*n +1)
    Narray.append(N)

print(Narray)

Tvalue = Tvalue + sum(Narray)
Narray.clear()

#BL
for n in range(start,seqLength+1):

    N = (4*n**2 -8*n + 5)
    Narray.append(N)

print(Narray)

Tvalue = Tvalue + sum(Narray)
Narray.clear()

#BR
for n in range(start,seqLength+1):

    N = (4*n**2 -10*n + 7)
    Narray.append(N)

print(Narray)

Tvalue = Tvalue + sum(Narray)
Narray.clear()

print(Tvalue)