import numpy as np
import matplotlib.pyplot as plt
import sys

class MatrixUtil:

    def read_file(self,file_path):
        f = open(file_path, 'r')
        lines = f.readlines()

        matrix = []

        i = 0
        for line in lines:

            if i != len(lines) - 1:
                line = line[:-1]

            line = str(line).split(",")
            results = [int(i) for i in line]

            matrix.append(results)
            i += 1

        matrix = np.array(matrix)
        return matrix
    def map_matrix(self,matrix):
        plt.imshow(matrix, cmap='copper', interpolation='nearest')
        plt.show()

R = 5
C = 5
def minCost(cost, m, n):
    # Instead of following line, we can use int tc[m+1][n+1] or
    # dynamically allocate memoery to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(C)] for x in range(R)]

    tc[0][0] = cost[0][0]

    # Initialize first column of total cost(tc) array
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cost[i][0]

        # Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cost[0][j]

        # Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j], tc[i][j - 1]) + cost[i][j]

    print(np.array(tc))
    return tc[m][n]


TEST_PATH = "D:\Documents\GitHub\JP-Programming\Pycharm Python Code\Euler Problems\EulerResources//testMat"
MATRIX_PATH = "D:\Documents\GitHub\JP-Programming\Pycharm Python Code\Euler Problems\EulerResources\matrix.txt"

util = MatrixUtil()
matrix = util.read_file(TEST_PATH)
print(minCost(matrix,4,4))