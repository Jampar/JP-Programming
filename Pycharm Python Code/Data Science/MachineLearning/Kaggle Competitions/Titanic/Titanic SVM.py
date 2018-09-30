import time
start = time.time()

import numpy as np
import pandas as pd
from sklearn import svm

def load_training_data(filename):

    import csv

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        labels = []
        data = []

        for row in reader:

            row = [round(float(x)) for x in row]

            if len(row) == 6:
                labels.append(int(row[0]))
                data.append(row[1:])

    return np.array(labels), np.array(data)


Y = load_training_data("train.csv")[0]
X = load_training_data("train.csv")[1]

test = load_training_data("test.csv")[1]
ids = load_training_data("test.csv")[0]

classifer = svm.SVC(kernel='rbf')
classifer.fit(X,Y)

results = []

for t in range(len(test)):
    result = int(classifer.predict([test[t]]))
    results.append([ids[t],result])


df = pd.DataFrame(np.array(results))
df.to_csv("results.csv",header=["PassengerId","Survived"],index=None)

finish = time.time()
print("Time Taken = ", finish-start)