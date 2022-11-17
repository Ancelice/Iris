import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import ipaddress
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import openpyxl
from tensorflow.keras import layers, models
from tensorflow.keras.utils import plot_model

filename = os.listdir("C:/Users/anli/iris/GeoIP/reply_src_addr")
print(filename)
print()

df = pd.read_excel("./rsa/Asia/" + filename[0], engine="openpyxl")
train_rsa = df['probe_dst_prefix']
tmp1 = df['reply_src_addr']
train_x = []
train_y = []
for z in range(len(tmp1)):
    train_x.append(int(ipaddress.IPv4Address(df.iat[z, 3])))
    train_y.append(int(ipaddress.IPv4Address(df.iat[z, 1])))
train_x = np.array(train_x).reshape(-1, 1)
train_y = np.reshape(train_y, (-1))

AF = models.Sequential()
AF.add(layers.Dense(64, input_shape = (train_x.shape[1], )))
AF.add(layers.Activation('relu'))
AF.add(layers.Dropout(0.5))
AF.add(layers.Dense(10))
AF.add(layers.Activation('softmax'))
AF.add(layers.Dense(1))
AF.compile(loss='mse',optimizer='Adam',metrics=['mae'])

AF.summary()

SAVE_DATA_DIR_PATH = "C:/Users/anli//Iris/FL/"
plot_model(AF, to_file=SAVE_DATA_DIR_PATH + "plot_model.png")