import requests
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sys
import os
import plotly.express as px

import openpyxl

# rsa_ttl
filename = os.listdir("C:/Users/anli/iris/FL/result/rsa_ttl/Master")
print("rsa-ttl")

RTTIME = []
RTMSE = []
RTMAE = []

for s in range(len(filename)):

    print(filename[s])
    df  = pd.read_excel("./result/rsa_ttl/Master/" + filename[s], engine="openpyxl")
    RTTIME.append(s)
    RTMSE.append(df.iat[1, 1])
    RTMAE.append(df.iat[1, 2])


# pdp_ttl
filename = os.listdir("C:/Users/anli/iris/FL/result/pdp_ttl/Master")
print("pdp-ttl")

PTTIME = []
PTMSE = []
PTMAE = []

for g in range(len(filename)):

    print(filename[g])
    df  = pd.read_excel("./result/pdp_ttl/Master/" + filename[g], engine="openpyxl")
    PTTIME.append(g)
    PTMSE.append(df.iat[1, 1])
    PTMAE.append(df.iat[1, 2])


# pdprsa_ttl
filename = os.listdir("C:/Users/anli/iris/FL/result/pdprsa_ttl")
print("pdprsa-ttl")

PRTTIME = []
PRTMSE = []
PRTMAE = []

for t in range(len(filename)):

    print(filename[t])
    df  = pd.read_excel("./result/pdprsa_ttl/" + filename[t], engine="openpyxl")
    PRTTIME.append(t)
    PRTMSE.append(df.iat[1, 1])
    PRTMAE.append(df.iat[1, 2])

##### 

plt.plot(PRTTIME, PRTMSE, label='PDP & RSA')
plt.title('MSE / PDP & RSA - TTL')
plt.ylabel('MSE', fontsize=14)
plt.xlabel('Round', fontsize=14)
plt.xlim(0, )
plt.ylim(0, )
plt.show()

plt.plot(PRTTIME, PRTMAE, label='PDP & RSA')
plt.title('MAE / PDP & RSA - TTL')
plt.ylabel('MAE', fontsize=14)
plt.xlabel('Round', fontsize=14)
plt.xlim(0, )
plt.ylim(0, )
plt.show()

plt.plot(PRTTIME, PRTMSE, label='PDP & RSA - TTL')
plt.plot(PTTIME, PTMSE, label='PDP - TTL')
plt.plot(RTTIME, RTMSE, label='RSA - TTL')
plt.title('MSE')
plt.ylabel('MSE', fontsize=14)
plt.xlabel('Round', fontsize=14)
plt.xlim(0, )
plt.ylim(0, )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=14)
plt.show()

plt.plot(PRTTIME, PRTMAE, label='PDP & RSA - TTL')
plt.plot(PTTIME, PTMAE, label='PDP - TTL')
plt.plot(RTTIME, RTMAE, label='RSA - TTL')
plt.title('MAE')
plt.ylabel('MAE', fontsize=14)
plt.xlabel('Round', fontsize=14)
plt.xlim(0, )
plt.ylim(0, )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=14)
plt.show()