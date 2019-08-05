from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import pandas as pd
import pathlib as pl
import os
import utils.data_inputter as data_input
import utils.image_handler as image_handle

PATH = "C:/Users/james/Documents/GitHub/JP/JP-Programming/Pneumonia Image Classification/resources/chest_xray"

if __name__ == '__main__':
    tf.enable_eager_execution()
    Inputter = data_input.Inputter(PATH)
    img_df = pd.DataFrame(Inputter.load_data(1))

    handler = image_handle.ImageHandler()

    for i in range(1,len(img_df)):
        print(img_df['path'][i])




