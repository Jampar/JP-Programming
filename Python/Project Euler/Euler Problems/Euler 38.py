import time as t

start = t.time()

def has_all_digits(x):
    chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = True

    for c in chars:
        if c in str(x):
            continue
        else:
            result = False
            break
    return result


def generate_multiple_list(n):
    multiples = []

    for i in range(1, n+1):
        multiples.append(i)

    return multiples


current_max = 0
for i in range(0,1000):
    multiples = generate_multiple_list(i)
    for j in range(0,10000):
        num = ''

        for m in multiples:
            num += str(j*m)

        if has_all_digits(num) and len(num)<10:
            if int(num) > current_max:
                current_max = int(num)
                print(current_max)


end = t.time()

print("Finished in:", str(end - start), 's')