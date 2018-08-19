import time
import math
import random

start = time.time()


def B(n):

    t = random.randint(1,n)

    L ,H= 1,n
    g = -1
    c = 0

    while g != t:
        g = math.floor((L + H) / 2)

        if g > t:
            H = g-1

        if g < t:
            L = g + 1

        if g == t:
           continue

        c += 1


    return c


if __name__ == '__main__':
    for i in range(0,1000):
        b = B(6)
        if b != 0:
            print(b)

end = time.time()
print("Time Taken", end - start)
