# KERAS
from tensorflow import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.backend import function

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
from PIL import Image
from numpy import *
# SKLEARN
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# input image dimensions
img_rows, img_cols = 200, 200

# number of channels
img_channels = 1

model = keras.models.load_model('cnn-model')

# %%
#  data

path2 = '.\\input_data_resized'  # path of data

imlist = os.listdir(path2)

im1 = array(Image.open('input_data_resized' + '\\' + imlist[0]))  # open one image to get size
m, n = im1.shape[0:2]  # get the size of the images
imnbr = len(imlist)  # get the number of images

# create matrix to store all flattened images
immatrix = array([array(Image.open('input_data_resized' + '\\' + im2)).flatten()
                  for im2 in imlist], 'f')

labels = ['Benign', 'Ransomware']


for i in range(len(immatrix)):
    img = immatrix[i].reshape(1, 1, img_rows, img_cols)
    is_ransom = imlist[i].upper().__contains__('RANSOM')
    pred = labels[model.predict(img)[0][1].astype(int)]

    if pred == labels[0]:
        classification = 'Negative'
    else:
        classification = 'Positive'

    if is_ransom and pred == 'Ransomware' or not is_ransom and pred != 'Ransomware':
        classification = 'True  ' + classification
    else:
        classification = 'False ' + classification

    print(classification, ' | ', imlist[i], 'predicted as', pred)

print('Done')
