import os

import pandas as pd
from sklearn.utils import shuffle


class Inputter:

    root_labels = None
    path = ""

    def __init__(self,root_path):
        self.path = root_path
        self.root_labels = self.get_data_root_labels(path=root_path)


    #Load data from the 3 sources: 0 = test, 1 = train, 2 = val
    def load_data(self,source):

        # Filter out misc files
        for label in self.root_labels:
            if label[:-(len(label) - 1)] == '.':
                self.root_labels.remove(label)

        # Get train dir name
        train_label = self.root_labels[source]

        # Conc to get path
        training_path = self.path + '/' + train_label

        # Get the list of labels in that dataset.
        label_list = os.listdir(training_path)
        # Number of labels in the dataset.
        label_count = len(label_list)

        # Filter out misc files
        for label in label_list:
            if label[:-(len(label) - 1)] == '.':
                label_list.remove(label)

        images = []
        labels = []
        #Loop through labels
        for label in label_list:

            #Path to that labels image dir
            path = training_path + '/' + label
            #Get the list of image names
            image_list = (os.listdir(path))
            #Remove misc file
            image_list.remove(image_list[0])

            #Loop through images in dir
            for image_name in image_list:

                #Path to that image
                path_image_name = training_path + image_name
                #Append to data structures
                images.append(path_image_name)
                labels.append(label)

        #Convert labels to numerical indicies
        labels = self.extract_indicies(labels)

        #Create a Dataframe object to hold the image paths and labels
        df = pd.DataFrame()
        #Append the data
        df['path'] = images
        df['label'] = labels

        #Shuffle the rows
        df = shuffle(df)
        #Reset the index column
        df.reset_index(drop=True, inplace=True)

        return df

    def get_data_root_labels(self,path):
        return os.listdir(path)
    def extract_indicies(self,labels):

        indicies= []
        label_ref = list(set(labels))

        for label in labels:
            indicies.append(label_ref.index(label))

        return  indicies



