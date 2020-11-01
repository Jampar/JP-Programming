data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

rowArray = data.splitlines()

intRowHolder = []
intRowArray = []
runningTotal = []
runningTotalHolder = []

#Converts data to int 2d array.
for i in range(0, rowArray.__len__()):

    sRowArray = rowArray[i].split()
    intRowHolder = [int(i)for i in sRowArray]
    row = intRowHolder.__len__()
    intRowArray.append(intRowHolder)

row = row
col = row

runningTotalHolder = intRowArray[row - 1].copy()
for x in reversed(range(0, row)):

    for y in (range(0, col -1)):

        if y < col:
            currentNum = runningTotalHolder[y]
            forwardNum = runningTotalHolder[y+1]
            topNum = intRowArray[x-1][y]

            print("",topNum)
            print(currentNum,forwardNum)

            calNum1 = topNum + currentNum
            calNum2 = topNum + forwardNum
            print("")

            if calNum1 > calNum2:
                runningTotalHolder[y] = calNum1
                print(currentNum,"+",topNum,"=",calNum1)
                print(runningTotalHolder)

            else:
                runningTotalHolder[y] = calNum2
                print(forwardNum,"+",topNum,"=",calNum2)
                print(runningTotalHolder)


            print("")

            col = x

