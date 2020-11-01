x = 0
y = 0
z = 0

PalinDromes = [0]

answers = [0]

for x in range(1,10):
    for y in range(0,10):
        for z in range(0, 10):

            tn = x +(10*y)+(100*z)+(1000*z)+(10000* y) + (100000 * x)

            PalinDromes.append(tn)

for i in reversed(range(0,PalinDromes.__len__())):

    for f in reversed(range(100,1000)):

        if PalinDromes[i] % f == 0 and (PalinDromes[i] / f)/ 100 > 0 and (PalinDromes[i] / f)/ 100 < 10:

            answers.append(PalinDromes[i])

print(max(answers))