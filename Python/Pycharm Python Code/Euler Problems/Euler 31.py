coinValues = [1,2,5]
amount = 12

combinations = [0] * (amount + 1)
combinations[0] = 1

for coin in coinValues:
    for i in range(1,combinations.__len__()):
        if i >= coin:
            print(combinations)
            combinations[i] += combinations[i-coin]

print(combinations)

