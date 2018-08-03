from fractions import Fraction

def simplifyFraction (n,d):
    fract = Fraction(n,d)
    simFract = str(fract)
    simFract = simFract.split("/")
    return simFract

fractions = []

for n in range (10,100):
    for d in range(10,100):

        print(n)

        #Splitting the numerator and denominator.
        nSplit = [int(z) for z in str(n)]
        dSplit = [int(s) for s in str(d)]

        if not nSplit.__contains__(0) and not dSplit.__contains__(0):

            #Removing common values in numerator and denominator.
            for n in nSplit:
                if n in dSplit and n != 0:
                    dSplit.remove(n)
                    nSplit.remove(n)

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
            #print(simplFract)

            if simNumer == simplFract[0] and simDenom == simplFract[1]:
                fractions.append(str(n," / ",d))

print(fractions)