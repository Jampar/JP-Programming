nums = []
p = 0
maxRange = 100

for i in range(1,maxRange+1):
    nums.append(i)

for x in range(0,nums.__len__()):

    n = nums[x]**2
    p = p+n


t = sum(nums)
t = t **2

print(t - p)