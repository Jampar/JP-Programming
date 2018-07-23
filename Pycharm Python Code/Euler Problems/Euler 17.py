units = []
units.append("")
units.append("one")
units.append("two")
units.append("three")
units.append("four")
units.append("five")
units.append("six")
units.append("seven")
units.append("eight")
units.append("nine")

teens = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

tens = []
tens.append("")
tens.append("ten")
tens.append("twenty")
tens.append("thirty")
tens.append("forty")
tens.append("fifty")
tens.append("sixty")
tens.append("seventy")
tens.append("eighty")
tens.append("ninety")

totalLength = 0
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):

            if a > 0:
                if c == 0 and b ==0:
                    totalLength = totalLength + len(units[a])+len("hundred")
                else:
                    totalLength = totalLength + len(units[a])+len("hundred")+len("and")

                print(units[a],"hundred","and")

            if b == 1 and b <= 2:

                if c == 0:
                    totalLength= totalLength + len(tens[1])
                    print(tens[1])
                if c >= 1:
                    totalLength = totalLength + len(teens[c-1])
                    print(teens[c-1])

            else:
                totalLength = totalLength + len(tens[b])
                totalLength = totalLength + len(units[c])
                print(tens[b])
                print(units[c])
                print("")

totalLength = totalLength + len("onethousand")

print(totalLength)
