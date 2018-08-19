import time
start = time.time()
import numpy as np


def load_training_data(filename):

    import csv

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        labels = []
        data = []

        for row in reader:

            if row [2] == 'male':
                row[2] = 0
            else:
                row[2] = 1


            row = [round(float(x)) for x in row]
            row = [x for x in row if x is not '']

            if len(row) == 7:
                labels.append(int(row[0]))
                data.append(row[1:])

    return np.array(labels), np.array(data)


Y = load_training_data("train.csv")[0]
X = load_training_data("train.csv")[1]

from sklearn.neighbors import KNeighborsClassifier

classifer = KNeighborsClassifier()
classifer.fit(X,Y)

finish = time.time()
print("Time Taken = ", finish-start)