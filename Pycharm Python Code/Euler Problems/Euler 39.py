def generate_squares(lim):
    sqrs = []

    for i in range(1,lim+1):
        sqrs.append(i**2)

    return sqrs


sqrs = generate_squares(10)
print(sqrs)