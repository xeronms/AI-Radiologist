# -*- coding: utf-8 -*-
"""
To schemat ładowania i zachowywania modelu

Dla całego shcematu tworzenia itp. musicie trochę poczekać
 bo muszę go przetestowa
"""


# TAK ZACHOPWUJEMY MODEL
"""checkpoint_path = "Wybrany_Folder_wKtórym_Chemy_Model\Nazw_pliku.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)"""


#### CHEKPOINT MA W SOBIE TRZY RÓZNE PLIKI!!! _ MODELEM JEST TEN KTÓRY NJWIECJ WAŻY####

from keras.models import Sequential
from keras import layers
from keras.layers import Conv2D, MaxPooling2D,Dropout,Flatten,Dense,Activation,GlobalMaxPooling2D
from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications import ResNet50
from keras.models import Model

import os
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img

from keras.utils import to_categorical
from sklearn.model_selection import train_test_split



pre_trained_model_Dense = DenseNet121(input_shape = (224,224,3), include_top = False, weights='imagenet')
pre_trained_model_Dense.trainable = False


model_test = tf.keras.Sequential()
model_test.add(pre_trained_model_Dense)
model_test.add(Prediciton0)
model_test.add(Prediction1)
model_test.add(Prediction2)
model_test.add(Prediction3)
model_test.add(Prediction4)
model_test.add(Prediction5)

model_test.load_weights(checkpoint_path)
model_test.compile(loss='categorical_crossentropy',optimizer = 'adam',metrics=['accuracy',tf.keras.metrics.Recall(),tf.keras.metrics.Precision()])
model_test.summary()

loss_Dense,accuracy_Dense,recall_Dense,precision_Dense = model_test.evaluate_generator(validation_generator, total_validate//batch_size,workers = 12)
print("Test accuracy:{:.3f}% ".format(accuracy_Dense))
print("Test recall:{:,.3f}% ".format(recall_Dense))
print("Test precision:{:,.3f}% ".format(precision_Dense))
print("Test loss:{:,.3f}% ".format(loss_Dense))
#print(loss)