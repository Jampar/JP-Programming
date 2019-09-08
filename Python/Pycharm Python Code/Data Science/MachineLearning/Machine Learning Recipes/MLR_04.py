from sklearn import datasets

# COLLECT TRAINING DATA
iris = datasets.load_iris()

print(iris)

X = iris.data #input FEATURES
y = iris.target #output LABELS

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= .5) #splits the data so some can be used for testing 50%

# TRAIN CLASSIFIER
from sklearn.neighbors import KNeighborsClassifier

# my_classifier = tree.DecisionTreeClassifier() #replaced with Kneighbor
my_classifier = KNeighborsClassifier()
my_classifier.fit(X_train, y_train)

# MAKE PREDICTIONS

predictions = my_classifier.predict(X_test)

# CHECK ACCURACY
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))