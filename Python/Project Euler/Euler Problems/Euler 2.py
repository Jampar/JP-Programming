import math as m

i = 1

Seq = []
Even = []

Phi = (1 + m.sqrt(5))/2
phi = (1 - m.sqrt(5))/2

#Generates a Fibonacci Sequence
def GenerateSequence(n):

    a = (Phi ** n - (phi)**n) / m.sqrt(5)
    return round(a)

#Finds all values of the fibonacci sequence that are less than 4000000
while GenerateSequence(i) < 4000000:

    Seq.append(GenerateSequence(i))
    i = i + 1

x = 0

#Finds all fibonacci values that are < 4000000 and even.
while x < Seq.__len__():

    if Seq[x] % 2 == 0:

        Even.append(Seq[x])

    x = x + 1

print(Even)
t = sum(Even)
print(t)






