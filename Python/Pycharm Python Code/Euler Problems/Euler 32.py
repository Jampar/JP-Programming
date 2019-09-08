
def checkPan(n):
    checker = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nSplit = [int(d) for d in str(n)]

    isPan = False


    if len(str(n)) == len(checker):


        for check in checker:
            if check in nSplit:
                isPan = True
            else:
                isPan = False
                break

    return  isPan

def remove_duplicates(x):
    a = []
    for i in x:
        if i not in a:
            a.append(i)
    return a



panDigits = []
panId = []

for multiplier in range(0,5000):
    for multiplicand in range (0,500):
        product = multiplier * multiplicand


        sumStr = str(multiplier)+str(multiplicand)+str(product)

        if(checkPan(int(sumStr))):
            panDigits.append(product)

panDigits = remove_duplicates(panDigits)
print(panDigits)
print(sum(panDigits))



