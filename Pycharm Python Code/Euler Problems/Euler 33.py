from fractions import Fraction

def simplifyFraction (n,d):
    fract = Fraction(n,d)
    simFract = str(fract)
    simFract = simFract.split("/")
    return simFract

fractions = []

for n in range (10,100):

    for d in range(10,100):

        numer = n
        denom = d

        #Splitting the numerator and denominator.
        nSplit = [int(z) for z in str(numer)]
        dSplit = [int(s) for s in str(denom)]

        if not nSplit.__contains__(0) and not dSplit.__contains__(0):

            #Removing common values in numerator and denominator.
            for k in nSplit:
                if k in dSplit and k != 0:
                    dSplit.remove(k)
                    nSplit.remove(k)

            #Place a 1 in the fraction where there is no number.
            if len(nSplit) == 0:
                nSplit.append(1)

            if len(dSplit) == 0:
                nSplit.append(1)

            #Join the split numer and deno to form simplified numbers.
            simNumer = ''.join(str(v) for v in nSplit)
            simDenom = ''.join(str(v) for v in dSplit)

            #Casts the joined numbers to ints
            simNumer = int(simNumer)
            simDenom = int(simDenom)

            simplFract = simplifyFraction(n,d)
            if len(simplFract) == 2:
                if simNumer == int(simplFract[0]) and simDenom == int(simplFract[1]):
                    if n/d <1:
                        if len(str(n)) == 2 and len(str(d)) == 2:
                            fractions.append(str(n)+" / "+str(d))
print(len(fractions))
print(fractions)