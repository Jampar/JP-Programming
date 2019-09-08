from fractions import Fraction

def simplifyFraction (n,d):

    fract = Fraction(n,d)
    simFract = str(fract)
    simFract = simFract.split("/")

    sintFract = []

    for n in simFract:
        sintFract.append(int(n))

    return sintFract

def removeCommonValues(a):

        nSplit = [int(n) for n in str(a[0])]
        dSplit = [int(d) for d in str(a[1])]

        for digit in nSplit:
            if dSplit.__contains__(digit):
                nSplit.remove(digit)
                dSplit.remove(digit)

        fraction=[]

        fraction.append(int(''.join(str(x) for x in nSplit)))
        fraction.append(int(''.join(str(x) for x in dSplit)))


        return fraction

simpleFractions = []
rawFractions = []
insimFractions = []
correctFractions = []

for n in range (10,101):

    for d in range(10,101):

        if n % 10 != 0 or d % 10 != 0:
            if n/d < 1:
                fraction = simplifyFraction(n,d)
                simpleFractions.append(fraction)

                rawFractions.append([n,d])

for r in rawFractions:
    frac = removeCommonValues(r)
    insimFractions.append(frac)

for f in range(0,simpleFractions.__len__()):
    if simpleFractions[f] == insimFractions[f] and insimFractions[f] != rawFractions[f]:
        correctFractions.append(rawFractions[f])

print(correctFractions)

totalNProduct = 1
totalDProduct = 1

for fract in correctFractions:
    totalNProduct *= fract[0]
    totalDProduct *= fract[1]

totalNProduct *= 4
totalDProduct *= 8

print(Fraction(totalNProduct,totalDProduct))