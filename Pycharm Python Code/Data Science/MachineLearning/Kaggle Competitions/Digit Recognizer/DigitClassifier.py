from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

X,Y = train.loc[:,train.columns != 'label'],train['label']

clf = KNeighborsClassifier()
print("Inst Clf")
clf.fit(X,Y)
print("Fitted")
test = np.array(test)
results = clf.predict(test)
pd.DataFrame(results).to_csv()