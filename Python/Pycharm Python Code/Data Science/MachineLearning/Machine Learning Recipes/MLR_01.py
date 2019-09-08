from sklearn import tree
from sklearn import datasets


features = [[150,1],[140,1],[170,0],[180,0]]
labels = [1,1,0,0]

clf = tree.DecisionTreeClassifier()
clf.fit(features,labels)

print(clf.predict([[140,1]]))