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

#####

train_x = [0, 1, 2, 3]
train_y = [0, 0, 1, 1]
train_x = np.array(train_x).reshape(-1, 1)
train_y = np.reshape(train_y, (-1))

test_x = [4, 5, 6, 7]
test_y = [2, 2, 3, 3]
test_x = np.array(test_x).reshape(-1, 1)
test_y = np.reshape(test_y, (-1))

AF = models.Sequential()
AF.add(layers.Dense(64, input_shape = (train_x.shape[1], )))
AF.add(layers.Activation('relu'))
AF.add(layers.Dropout(0.5))
AF.add(layers.Dense(10))
AF.add(layers.Activation('softmax'))
AF.add(layers.Dense(1))
AF.compile(loss='mse',optimizer='Adam',metrics=['mae'])

AS = models.Sequential()
AS.add(layers.Dense(64, input_shape = (train_x.shape[1], )))
AS.add(layers.Activation('relu'))
AS.add(layers.Dropout(0.5))
AS.add(layers.Dense(10))
AS.add(layers.Activation('softmax'))
AS.add(layers.Dense(1))
AS.compile(loss='mse',optimizer='Adam',metrics=['mae'])

EU = models.Sequential()
EU.add(layers.Dense(64, input_shape = (train_x.shape[1], )))
EU.add(layers.Activation('relu'))
EU.add(layers.Dropout(0.5))
EU.add(layers.Dense(10))
EU.add(layers.Activation('softmax'))
EU.add(layers.Dense(1))
EU.compile(loss='mse',optimizer='Adam',metrics=['mae'])

NA = models.Sequential()
NA.add(layers.Dense(64, input_shape = (train_x.shape[1], )))
NA.add(layers.Activation('relu'))
NA.add(layers.Dropout(0.5))
NA.add(layers.Dense(10))
NA.add(layers.Activation('softmax'))
NA.add(layers.Dense(1))
NA.compile(loss='mse',optimizer='Adam',metrics=['mae'])

OC = models.Sequential()
OC.add(layers.Dense(64, input_shape = (train_x.shape[1], )))
OC.add(layers.Activation('relu'))
OC.add(layers.Dropout(0.5))
OC.add(layers.Dense(10))
OC.add(layers.Activation('softmax'))
OC.add(layers.Dense(1))
OC.compile(loss='mse',optimizer='Adam',metrics=['mae'])

SA = models.Sequential()
SA.add(layers.Dense(64, input_shape = (train_x.shape[1], )))
SA.add(layers.Activation('relu'))
SA.add(layers.Dropout(0.5))
SA.add(layers.Dense(10))
SA.add(layers.Activation('softmax'))
SA.add(layers.Dense(1))
SA.compile(loss='mse',optimizer='Adam',metrics=['mae'])

MASTER = models.Sequential()
MASTER.add(layers.Dense(64, input_shape = (train_x.shape[1], )))
MASTER.add(layers.Activation('relu'))
MASTER.add(layers.Dropout(0.5))
MASTER.add(layers.Dense(10))
MASTER.add(layers.Activation('softmax'))
MASTER.add(layers.Dense(1))
MASTER.compile(loss='mse',optimizer='Adam',metrics=['mae'])



history = AF.fit(train_x, train_y, epochs=1, verbose=1)
history = AS.fit(train_x, train_y, epochs=1, verbose=1)
history = EU.fit(train_x, train_y, epochs=1, verbose=1)
history = NA.fit(train_x, train_y, epochs=1, verbose=1)
history = OC.fit(train_x, train_y, epochs=1, verbose=1)
history = SA.fit(train_x, train_y, epochs=1, verbose=1)


loss, acc = AS.evaluate(test_x, test_y, verbose=0)
loss, acc = EU.evaluate(test_x, test_y, verbose=0)
loss, acc = NA.evaluate(test_x, test_y, verbose=0)
loss, acc = OC.evaluate(test_x, test_y, verbose=0)
loss, acc = SA.evaluate(test_x, test_y, verbose=0)
loss, acc = AF.evaluate(test_x, test_y, verbose=0)


WAF = AF.get_weights()
WAS = AS.get_weights()
WEU = EU.get_weights()
WNA = NA.get_weights()
WOC = OC.get_weights()
WSA = SA.get_weights()

sumW = [(a + b + c + d + e + f) / 6 for (a, b, c, d, e, f) in zip(WAF, WAS, WEU, WNA, WOC, WSA)]

MASTER.set_weights(sumW)
history = MASTER.fit(train_x, train_y, epochs=1, verbose=1)
LOSS, MAE = MASTER.evaluate(test_x, test_y, verbose=0)

print("MSE : " + str(LOSS) + " / MAE : " + str(MAE))