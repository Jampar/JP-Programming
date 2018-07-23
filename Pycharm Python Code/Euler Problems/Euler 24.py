import itertools

a = '0123456789'
k = 10
perms = []

for p in itertools.permutations(a, k):
    perms.append(int("".join(p)))

perms.sort()

for i in range(0,perms.__len__()):
    if i == 999999:
        print (perms[i])