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

AF_rsa = []
AS_rsa = []
EU_rsa = []
NA_rsa = []
OC_rsa = []
SA_rsa = []

AF_pdp = []
AS_pdp = []
EU_pdp = []
NA_pdp = []
OC_pdp = []
SA_pdp = []

TIME = []

filename = os.listdir("C:/Users/anli/iris/FL/rsa/Africa")
print("Africa")
for a in range(len(filename)):
    df  = pd.read_excel("./rsa/Africa/" + filename[a], engine="openpyxl")
    print(filename[a])
    print(str(len(df)))
    AF_rsa.append(len(df))
    TIME.append(a)

filename = os.listdir("C:/Users/anli/iris/FL/rsa/Asia")
print("Asia")
for b in range(len(filename)):
    df  = pd.read_excel("./rsa/Asia/" + filename[b], engine="openpyxl")
    print(filename[b])
    print(str(len(df)))
    AS_rsa.append(len(df))

filename = os.listdir("C:/Users/anli/iris/FL/rsa/Europe")
print("Europe")
for c in range(len(filename)):
    df  = pd.read_excel("./rsa/Europe/" + filename[c], engine="openpyxl")
    print(filename[c])
    print(str(len(df)))
    EU_rsa.append(len(df))

filename = os.listdir("C:/Users/anli/iris/FL/rsa/NA")
print("NA")
for d in range(len(filename)):
    df  = pd.read_excel("./rsa/NA/" + filename[d], engine="openpyxl")
    print(filename[d])
    print(str(len(df)))
    NA_rsa.append(len(df))

filename = os.listdir("C:/Users/anli/iris/FL/rsa/Oceania")
print("Oceania")
for e in range(len(filename)):
    df  = pd.read_excel("./rsa/Oceania/" + filename[e], engine="openpyxl")
    print(filename[e])
    print(str(len(df)))
    OC_rsa.append(len(df))

filename = os.listdir("C:/Users/anli/iris/FL/rsa/SA")
print("SA")
for f in range(len(filename)):
    df  = pd.read_excel("./rsa/SA/" + filename[f], engine="openpyxl")
    print(filename[f])
    print(str(len(df)))
    SA_rsa.append(len(df))

##### 

filename = os.listdir("C:/Users/anli/iris/FL/pdp/Africa")
print("Africa")
for g in range(len(filename)):
    df  = pd.read_excel("./pdp/Africa/" + filename[g], engine="openpyxl")
    print(filename[g])
    print(str(len(df)))
    AF_pdp.append(len(df))

filename = os.listdir("C:/Users/anli/iris/FL/pdp/Asia")
print("Asia")
for h in range(len(filename)):
    df  = pd.read_excel("./pdp/Asia/" + filename[h], engine="openpyxl")
    print(filename[h])
    print(str(len(df)))
    AS_pdp.append(len(df))

filename = os.listdir("C:/Users/anli/iris/FL/pdp/Europe")
print("Europe")
for i in range(len(filename)):
    df  = pd.read_excel("./pdp/Europe/" + filename[i], engine="openpyxl")
    print(filename[i])
    print(str(len(df)))
    EU_pdp.append(len(df))

filename = os.listdir("C:/Users/anli/iris/FL/pdp/NA")
print("NA")
for j in range(len(filename)):
    df  = pd.read_excel("./pdp/NA/" + filename[j], engine="openpyxl")
    print(filename[j])
    print(str(len(df)))
    NA_pdp.append(len(df))

filename = os.listdir("C:/Users/anli/iris/FL/pdp/Oceania")
print("Oceania")
for k in range(len(filename)):
    df  = pd.read_excel("./pdp/Oceania/" + filename[k], engine="openpyxl")
    print(filename[k])
    print(str(len(df)))
    OC_pdp.append(len(df))

filename = os.listdir("C:/Users/anli/iris/FL/pdp/SA")
print("SA")
for l in range(len(filename)):
    df  = pd.read_excel("./pdp/SA/" + filename[l], engine="openpyxl")
    print(filename[l])
    print(str(len(df)))
    SA_pdp.append(len(df))


##### 

plt.plot(TIME, AF_rsa, label='Africa')
plt.plot(TIME, AS_rsa, label='Asia')
plt.plot(TIME, EU_rsa, label='Europe')
plt.plot(TIME, NA_rsa, label='NA')
plt.plot(TIME, OC_rsa, label='Oceania')
plt.plot(TIME, SA_rsa, label='SA')
plt.title('The amount of data / rsa')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=14)
plt.ylabel('Data', fontsize=14)
plt.xlabel('Round', fontsize=14)
plt.xlim(0, )
plt.ylim(0, 100000)
plt.show()

plt.plot(TIME, AF_pdp, label='Africa')
plt.plot(TIME, AS_pdp, label='Asia')
plt.plot(TIME, EU_pdp, label='Europe')
plt.plot(TIME, NA_pdp, label='NA')
plt.plot(TIME, OC_pdp, label='Oceania')
plt.plot(TIME, SA_pdp, label='SA')
plt.title('The amount of data / pdp')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=14)
plt.ylabel('Data', fontsize=14)
plt.xlabel('Round', fontsize=14)
plt.xlim(0, )
plt.ylim(0, 100000)
plt.show()