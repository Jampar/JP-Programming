#a < b < c
#a + b + c = 1000

for a in range(0,1000):
    print(a)
    for b in range(0,1000):
        for c in range(0,1000):
            if a**2 + b**2 == c**2:
                if a+b+c == 1000:
                    if a<b<c:
                        print(a, "", b, "", c)
                        print(a*b*c)
                        print("")

