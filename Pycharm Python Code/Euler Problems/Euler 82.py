import numpy as np

matrix_path = "C:/Users\james\Documents\GitHub\JP\JP-Programming\Pycharm Python Code\Project Euler Dependencies\matrix"
test_path = "C:/Users\james\Documents\GitHub\JP\JP-Programming\Pycharm Python Code\Project Euler Dependencies/test.txt"

def load_matrix(path):
    matrix_raw = open(path)

    matrix = list()
    for row_raw in matrix_raw:
        split_row = row_raw.split(",")

        row = list()
        for term in split_row:
            term = int(term)
            row.append(term)

        matrix.append(row)

    return np.array(matrix)


def solve(matrix,start):

    #Create empty array of the same shape of passed matrix
    tc = np.zeros(matrix.shape,dtype=int)

    #Set start value.
    tc[start[0]][start[1]] = matrix[start[0]][start[1]]

    #Fill row right
    for i in range(start[1],tc.shape[0]):
        tc[start[0]][i] = matrix[start[0]][i] + tc[start[0]][i-1]

    #Fill left column down
    for j in range(start[0],tc.shape[1]):
        tc[j][start[1]] = matrix[j][start[1]] + tc[j-1][start[1]]

    print(tc)

    #Loop through filling in the total cost of each term in the matrix.
    for x in range(1,tc.shape[0]):
        for y in range(1,tc.shape[1]):
                tc[x][y] = matrix[x][y] + min(tc[x-1][y],tc[x][y-1])

    #Return final value.
    return tc[tc.shape[0]-1,tc.shape[1]-1]


matrix = load_matrix(test_path)
cost = solve(matrix,[2,0])
print(cost)