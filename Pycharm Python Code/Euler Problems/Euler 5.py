import time as t

maxRange = 17
def IsFactor(fac,num):
    if num % fac == 0:
        return True
    else:
        return  False

n = 2520
fact = False
startTime = t.time()
while fact == False:

    n = n + 1
    fact = True

    for x in range (1,maxRange+1):

        if IsFactor(x , n) != True:
            fact = False
            break

    if fact == True:
        print("answer: ", n)
        endTime = t.time()
        print("")
        print("Time Taken:" , endTime - startTime)