from fractions import Fraction

fractions = []

for n in range (10,100):
    print("*************************************************************************************************************")

    print(n)
    print("")

    for d in range(10,100):

        numer = n
        denom = d

        nSplit = [int(z) for z in str(n)]
        dSplit = [int(s) for s in str(d)]


        for n in nSplit:
            if n in dSplit and n != 0:
                dSplit.remove(n)
                nSplit.remove(n)

        if len(nSplit) == 0:
            nSplit.append(1)

        if len(dSplit) == 0:
            nSplit.append(1)


        simNumer = ''.join(str(v) for v in nSplit)
        simDenom = ''.join(str(v) for v in dSplit)

        simNumer = int(simNumer)
        simDenom = int(simDenom)

        fract = str(Fraction(numer, denom)).split("/")

        print(str(n) + "/" + str(d))
        print(str(simNumer) + "/" + str(simDenom))
        print(fract)
        print("")

        if(len(fract) == 2):
            if int(fract[0]) == simNumer and int(fract[1]) == simDenom:
               fractions.append(fract)

print(fractions)
#hello james