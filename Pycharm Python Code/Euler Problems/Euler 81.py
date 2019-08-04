import numpy as np
import matplotlib.pyplot as plt
import time as t
import math

start = t.time()

class Node:

    coordinate = (0,0)
    cost = 0

    def __init__(self,coord):
        self.coordinate = coord
        self.cost = self.FCost()

    def GCost(self):
        deltaX = self.coordinate[0] - startCoord[0]
        deltaY = self.coordinate[1] - startCoord[1]
        dist = math.sqrt(((deltaX*deltaX)+(deltaY*deltaY)))
        return dist

    def HCost(self):
        deltaX = self.coordinate[0] - endCoord[0]
        deltaY = self.coordinate[1] - endCoord[1]
        dist = math.sqrt(((deltaX * deltaX) + (deltaY * deltaY)))
        return dist

    def FCost(self):
        return (self.GCost() + self.HCost())

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

class MatrixSolver:

    path = []

    def generate_nodes(self,matrix):

        nodeGrid = []

        for x in range(0, matrix.shape[0]):

            nodeRow = []

            for y in range(0, matrix.shape[1]):

                node = Node((x, y))
                nodeRow.append(node)

            nodeGrid.append(nodeRow)

        return np.array(nodeGrid)

    def extract_biases(self,nodes):
        biases = []

        for nodeRow in nodes:
            biasRow = []

            for node in nodeRow:
                biasRow.append(node.cost)

            biases.append(biasRow)

        return np.array(biases)
    def extract_coords(self,nodes):
        coords = []

        for nodeRow in nodes:
            coordRow = []

            for node in nodeRow:
                coordRow.append(node.coordinate)
            coords.append(coordRow)

        return np.asanyarray(coords)

    def normalise_matrix(self,m):
        A = np.amax(m)
        B = np.amin(m)

        a = 10
        b = 1

        new_matrix = []
        for row in m:
            new_row = []

            for term in row:
                x = term
                value = a + (x-A)*(b-a)/(B-A)

                new_row.append(value)

            new_matrix.append(new_row)

        return np.array(new_matrix)

    def find_best_step(self,node,m):

        self.path.append(node.coordinate)

        down_node = Node((node.coordinate[0], (node.coordinate[1] + 1)))
        right_node = Node(((node.coordinate[0] + 1), node.coordinate[1]))

        if(right_node.coordinate == endNode.coordinate or down_node.coordinate == endNode.coordinate):
            self.path.append(endNode.coordinate)
            return

        if(m[down_node.coordinate[0],down_node.coordinate[1]] > m[right_node.coordinate[0],right_node.coordinate[1]] or down_node.coordinate[1] == m.shape[1]-1):
            self.find_best_step(right_node,m)
        else:
            self.find_best_step(down_node,m)

    def find_path(self,matrix):
        print("")
        self.find_best_step(startNode,matrix)
        return self.path

    def lookup_coords(self,path,matrix):
        values = []
        i = 0
        row = []
        for step in path:
            values.append(matrix[step[0]][step[1]])

        return np.array(values)

    def Solve(self,matrix):
        n = self.generate_nodes(matrix)

        orig_matrix = matrix

        biases = self.normalise_matrix(self.extract_biases(n))
        matrix = self.normalise_matrix(matrix)
        coords = self.extract_coords(n)

        #offset_matrix = (matrix) + (biases*10)
        print(matrix)
        path = self.find_path(matrix)
        matrix_values = self.lookup_coords(path,orig_matrix)
        print(matrix_values)
        return sum(matrix_values)



MATRIX_PATH = "D:\Documents\GitHub\JP-Programming\Pycharm Python Code\Euler Problems\EulerResources\matrix.txt"
TEST_PATH = "D:\Documents\GitHub\JP-Programming\Pycharm Python Code\Euler Problems\EulerResources//testMat"

endCoord = (0,0)
startCoord = (79,79)

startNode = Node(startCoord)
endNode = Node(endCoord)

util = MatrixUtil()
m = util.read_file(MATRIX_PATH)

solver = MatrixSolver()
sum = solver.Solve(m)
print(sum)

end = t.time()
print("Time Taken = "+ str(end - start))