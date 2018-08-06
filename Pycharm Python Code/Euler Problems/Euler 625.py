import matplotlib.pyplot as plt

def gcd(u, v):

    # simple cases (termination)
    if (u == v):
        return u;

    if (u == 0):
        return v;

    if (v == 0):
        return u;

    # look for factors of 2
    if (~u & 1): # u is even

        if (v & 1): # v is odd
            return gcd(u >> 1, v);
        else: # both u and v are even
            return gcd(u >> 1, v >> 1) << 1;


    if (~v & 1): # u is odd, v is even
        return gcd(u, v >> 1);

    # reduce larger argument
    if (u > v):
        return gcd((u - v) >> 1, v);

    return gcd((v - u) >> 1, u);



N = 15
x = 0
prevJ = 0

s = [0]

for j in range(1, N + 1):
    s.append(0)
    for i in range(1, j + 1):
        z = gcd(i, j)

        if z != j:
            s[j] += z

    print(j,s[j])

plt.plot(s)
plt.show()