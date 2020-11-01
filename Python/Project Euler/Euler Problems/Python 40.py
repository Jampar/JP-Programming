lim = 1000000
i = 1

conc = ""
while i <= lim:
    conc += str(i)
    i+=1


num = int(conc[0]) * int(conc[9]) * int(conc[99]) * int(conc[999])*int(conc[9999])*int(conc[99999])*int(conc[999999])
print(num)