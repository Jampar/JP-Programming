import time
start = time.time()
import numpy as np
from sklearn import svm

def load_training_data(filename):

    import csv

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        labels = []
        data = []

        for row in reader:

            row = [x for x in row if x is not '']
            row = [round(float(x)) for x in row]

            if len(row) == 7:
                labels.append(int(row[0]))
                data.append(row[1:])

    return np.array(labels), np.array(data)


Y = load_training_data("train.csv")[0]
X = load_training_data("train.csv")[1]

classifer = svm.SVC(kernel='linear')
classifer.fit(X,Y)

finish = time.time()
print("Time Taken = ", finish-start)