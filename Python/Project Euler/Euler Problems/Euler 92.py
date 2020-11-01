import numpy as np
import time as t

start = t.time()
chain = []
count = 0

def number_to_digit(n):
    d = [int(d) for d in str(n)]
    return d

def square_digits(d):
    s = [int(i)**2 for i in d]
    return s

def next_number(n):
    return sum(square_digits(number_to_digit(n)))

def produce_chain(s):
    n = next_number(s)
    if(n == 1 or n== 89):
        chain.append(n)
        chain.clear()
        return n
    else:
        chain.append(n)
        return produce_chain(n)

x = 0
for i in range(1,10000001):
    if produce_chain(i) == 89:
        x+=1
print(x)

end = t.time()
print("Time Take: %s" %(str(end-start)))
