import pandas as pd
import numpy as np
from sklearn import neighbors
from sklearn.preprocessing import Imputer

pd.set_option('display.max_columns', None)

def load_data(filename):

    #Load the csv file into a Dataframe
    data = pd.read_csv(filename, index_col=0)

    #Converting from hex to dec
    data["idhogar"] = [int(h,16)for h in data["idhogar"]]

    #Encoding the 3 columns which are dtype "object"
    data["dependency"] = pd.to_numeric(data["dependency"].replace({"no": 0, "yes":1}))
    data["edjefe"] = pd.to_numeric(data["edjefe"].replace({"no": 0, "yes":1}))
    data["edjefa"] = pd.to_numeric(data["edjefa"].replace({"no": 0, "yes":1}))


    headers = list(data.head(0))

    #Instantiate an object of class Imputer.
    imputer = Imputer(strategy='mean')

    #Fitting the imputer with the current data.
    imputer.fit(np.array(data))

    #Predicting the missing values and applying the headers to the new Dataframe made by this.
    data = pd.DataFrame(imputer.transform(np.array(data)),columns = headers,index=None)

    return data

train = load_data("all/train.csv")
test = load_data("all/test.csv")

Y = np.array(train['Target'])
train = train.drop('Target',axis = 1)
X = np.array(train)

clf = neighbors.KNeighborsClassifier()
print("Start Fit")
clf.fit(X,Y)
print("Finish Fit")


#Predicting the targets and getting the ids to fit in the csv.
targets = pd.DataFrame(clf.predict(np.array(test)),columns=["Target"]).values
ids = pd.read_csv("all/test.csv", index_col=0).index.get_values()

#Converting float targets to ints
targets = [int(t) for t in targets]

#Creating the submission csv file
results = pd.DataFrame()
results.insert(0,"Id",ids)
results.insert(1,"Target",targets)

#The submission file
results.to_csv("Submission.csv",index=False)
print("Finished")

