import numpy as np
import matplotlib.pyplot as plt
import keras
import cv2
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense
from keras.utils import to_categorical
from keras.layers import Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.models import load_model
from tensorflow.keras.models import save_model
import pickle
import random
import pandas as pd
import requests
from PIL import Image

#prepping image functions
def grayscale(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.axis('off')
    return image

def equalize(img):
    img = cv2.equalizeHist(img)
    return img

def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img/255
    return img
#testing with image
mph_20_url = 'https://c7.alamy.com/comp/2RBXEHH/german-traffic-sign-restricting-speed-to-20-kilometers-per-hour-2RBXEHH.jpg'
right_turn_url = 'https://c7.alamy.com/comp/M5MTMK/german-road-sign-turn-right-ahead-M5MTMK.jpg'
r = requests.get(right_turn_url, stream=True)
image = Image.open(r.raw)
plt.axis('off')
plt.imshow(image, cmap=plt.get_cmap('gray'))

img = np.asarray(image)
img = cv2.resize(img, (32, 32))
img = preprocessing(img)
plt.imshow(img, cmap = plt.get_cmap('gray'))
print(img.shape)
img = img.reshape(1, 32, 32, 1)

data = pd.read_csv('/Users/rohansiva/Desktop/ML_Projects/TrafficSignClassification/training_data/signnames.csv')
model = load_model('/Users/rohansiva/Desktop/ML_Projects/TrafficSignClassification/CNN_Models/german_traffic_signs_classifier.h5')

prediction = model.predict(img)
pred = np.argmax(prediction)
plt.imshow(image)
plt.axis('off')

for num, name in data.items():
  name = name.values
  print("predicted sign: "+ str(name[pred]))