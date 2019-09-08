import decimal as dec

dec.getcontext().prec = 3000
bigLength = 0
bigd = 0
for d in range(2,1001):
    num = str(dec.Decimal(1)/dec.Decimal(d))
    num = num[10:]
    search = num[:5]
    if num.find(search,1) != -1:
        length = num.find(search,1)
        if length > bigLength:
            bigLength = length
            bigd = d

print(bigLength)
print(bigd)