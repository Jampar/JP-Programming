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


def solve(matrix):

    #Create empty array of the same shape of passed matrix
    tc = np.zeros(matrix.shape,dtype=int)

    #Set start value.
    tc[0][0] = matrix[0][0]

    #Fill row
    for i in range(0,tc.shape[0]):
        tc[0][i] = matrix[0][i] + tc[0][i-1]


    #Fill left column down
    for j in range(1,tc.shape[1]):
        tc[j][0] = matrix[j][0] + tc[j-1][0]

    #Loop through filling in the total cost of each term in the matrix.
    for x in range(1,tc.shape[0]):
        for y in range(1,tc.shape[1]):
                tc[x][y] = matrix[x][y] + min(tc[x-1][y],tc[x][y-1])

    #Return final value.
    return tc[tc.shape[0]-1,tc.shape[1]-1]


matrix = load_matrix(matrix_path)
cost = solve(matrix)
print(cost)