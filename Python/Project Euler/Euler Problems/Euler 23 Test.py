def d(n): # Sum of Proper Divisors

    divisors = []

    for i in range(1,round(n/2)+1):
        if n % i == 0:
            divisors.append(i)

    divisors =list(set(divisors))

    s = sum(divisors)
    return s

n = 1
x = 0
abunNums = []
limit = 28124

answers = []

for a in range(0,limit*2 + 1):
    answers.append(0)

print("Answers Filled")


while n <= limit:

    n+=1
    #Abundant Num
    if d(n) > n:
        abunNums.append(n)

print("Abundant Nums Made")

print(abunNums)

for n1 in range(len(abunNums)):

    for n2 in range(len(abunNums)):

        ans = abunNums[n1] + abunNums[n2]

        #if(abunNums[n1] <= 24):
         #   print(abunNums[n1], " + " ,abunNums[n2], " = ", ans)

        answers[ans] = 1

print("Answers Made")

placeTotal = 0

for i in range(len((answers))):
    if answers[i] == 0:
        if i < limit:
            print(i)
            placeTotal +=i

print(placeTotal)

