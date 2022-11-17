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

##### Africa

filename = os.listdir("C:/Users/anli/iris/FL/result/rsa_ttl/Africa")
print("Africa")

AFTIME = []
AFMSE = []
AFMAE = []

for a in range(len(filename)):

    print(filename[a])
    df  = pd.read_excel("./result/rsa_ttl/Africa/" + filename[a], engine="openpyxl")
    AFTIME.append(a)
    AFMSE.append(df.iat[1, 1])
    AFMAE.append(df.iat[1, 2])

##### Asia

filename = os.listdir("C:/Users/anli/iris/FL/result/rsa_ttl/Asia")
print("Asia")

ASTIME = []
ASMSE = []
ASMAE = []

for d in range(len(filename)):

    print(filename[d])
    df  = pd.read_excel("./result/rsa_ttl/Asia/" + filename[d], engine="openpyxl")
    ASTIME.append(d)
    ASMSE.append(df.iat[1, 1])
    ASMAE.append(df.iat[1, 2])

##### Europe

filename = os.listdir("C:/Users/anli/iris/FL/result/rsa_ttl/Europe")
print("Europe")

EUTIME = []
EUMSE = []
EUMAE = []

for g in range(len(filename)):

    print(filename[g])
    df  = pd.read_excel("./result/rsa_ttl/Europe/" + filename[g], engine="openpyxl")
    EUTIME.append(g)
    EUMSE.append(df.iat[1, 1])
    EUMAE.append(df.iat[1, 2])

##### NA

filename = os.listdir("C:/Users/anli/iris/FL/result/rsa_ttl/NA")
print("NA")

NATIME = []
NAMSE = []
NAMAE = []

for j in range(len(filename)):

    print(filename[j])
    df  = pd.read_excel("./result/rsa_ttl/NA/" + filename[j], engine="openpyxl")
    NATIME.append(j)
    NAMSE.append(df.iat[1, 1])
    NAMAE.append(df.iat[1, 2])

##### Oceania

filename = os.listdir("C:/Users/anli/iris/FL/result/rsa_ttl/Oceania")
print("Oceania")

OCTIME = []
OCMSE = []
OCMAE = []

for m in range(len(filename)):

    print(filename[m])
    df  = pd.read_excel("./result/rsa_ttl/Oceania/" + filename[m], engine="openpyxl")
    OCTIME.append(m)
    OCMSE.append(df.iat[1, 1])
    OCMAE.append(df.iat[1, 2])

##### SA

filename = os.listdir("C:/Users/anli/iris/FL/result/rsa_ttl/SA")
print("SA")

SATIME = []
SAMSE = []
SAMAE = []

for p in range(len(filename)):

    print(filename[p])
    df  = pd.read_excel("./result/rsa_ttl/SA/" + filename[p], engine="openpyxl")
    SATIME.append(p)
    SAMSE.append(df.iat[1, 1])
    SAMAE.append(df.iat[1, 2])

##### Master

filename = os.listdir("C:/Users/anli/iris/FL/result/rsa_ttl/Master")
print("Master")

MASTIME = []
MASMSE = []
MASMAE = []

for s in range(len(filename)):

    print(filename[s])
    df  = pd.read_excel("./result/rsa_ttl/Master/" + filename[s], engine="openpyxl")
    MASTIME.append(s)
    MASMSE.append(df.iat[1, 1])
    MASMAE.append(df.iat[1, 2])

##### 

plt.plot(AFTIME, AFMSE, label='Africa')
plt.plot(ASTIME, ASMSE, label='Asia')
plt.plot(EUTIME, EUMSE, label='Europe')
plt.plot(NATIME, NAMSE, label='NA')
plt.plot(OCTIME, OCMSE, label='Oceania')
plt.plot(SATIME, SAMSE, label='SA')
plt.plot(MASTIME, MASMSE, label='World')
plt.title('MSE / rsa_ttl')
plt.ylabel('MSE', fontsize=14)
plt.xlabel('Round', fontsize=14)
plt.xlim(0, )
plt.ylim(0, )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=14)
plt.show()

plt.plot(AFTIME, AFMAE, label='Africa')
plt.plot(ASTIME, ASMAE, label='Asia')
plt.plot(EUTIME, EUMAE, label='Europe')
plt.plot(NATIME, NAMAE, label='NA')
plt.plot(OCTIME, OCMAE, label='Oceania')
plt.plot(SATIME, SAMAE, label='SA')
plt.plot(MASTIME, MASMAE, label='World')
plt.title('MAE / rsa_ttl')
plt.ylabel('MAE', fontsize=14)
plt.xlabel('Round', fontsize=14)
plt.xlim(0, )
plt.ylim(0, )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=14)
plt.show()