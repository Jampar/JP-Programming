from PIL import Image
import glob
import numpy as np
import os
from sklearn import tree

imageRes = 600,600

def format_image(image):


    image = image.resize(imageRes,Image.ANTIALIAS)

    return image


def load_image(img_path):

    print("Loading:",img_path)

    img = Image.open(img_path,"r")
    img.load()

    img = format_image(img)

    img = np.array(img,dtype="int32")

    img = img[:,:,0]

    img = img.ravel()

    return img.tolist()


def load_images(path):

    labels = []
    features = []

    for file in os.listdir(path):

        dir = os.path.join(path, file)

        for sub_file in os.listdir(dir):

            current = os.path.join(dir, sub_file)

            img_data = load_image(current)
            features.append(img_data)


        for image in os.listdir(dir):
            labels.append(file[:len(file)-1])

    return features,labels


reload = input("Does the data need to be reloaded?")

if reload == "y" or os.path.isfile("data") == False:
    data = load_images("E:\Documents\Pycharm Python Code\MachineLearning\Scikit-Learn\Image Classification\Images")
    print("Data loaded")

    features_text = open("features","w")
    labels_text = open("labels","w")

    features_text.write(data[0])
    labels_text.write(data[1])

    features_text.close()
    labels_text.close()

    print("Data Saved")

features_text = open("features","r")
labels_text = open("labels","r")

features = features_text.read()
labels = labels_text.read()

if len(labels) <= 0 or len(features) <= 0:
    print("No Training Data Found!")
else:
    clf = tree.DecisionTreeClassifier()
    clf.fit(features,labels)

    predict_file = input("Path to new example file: ")

    example_file = load_image(predict_file)
    example_file = [example_file]

    print(clf.predict(example_file))