import matplotlib.pyplot as plt

def R(h,s):
    return ((100*h)** 2/3)*(s**1/3)

def g(h,s):
    return 20*h + 2000*s

s = 5000
for h in range(-200,200):
        plt.plot([h], [R(h,s)], 'ro')
        print(g(h,s))

plt.show()
