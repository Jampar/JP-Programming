def generate_pandigital(n):
    lst = [int(i) for i in range(1,n+1)]
    result = []
    for i in range(0,n):
        split_num = [[lst[0]],[lst[1:]]]

        for j in split_num[1]:
            for k in range(0,len(j)):
                full_num = [lst[0]]+j
                result.append(int("".join(map(str, full_num))))
                j = move_list_left(j)

        lst = move_list_left(lst)

    return result

def move_list_left(lst):
    return lst[1:] + [lst[0]]

import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

pans = []
for i in range(1,4):
    nums = generate_pandigital(i)
    pans.append(nums)

flat_pans = [item for sublist in pans for item in sublist]
print(flat_pans)
