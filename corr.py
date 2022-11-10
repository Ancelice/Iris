import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pylab import rcParams
import os
import ipaddress

#####

filename = os.listdir("C:/Users/anli/iris/data")
print(filename)
print()

df = pd.read_excel("./data/" + filename[0], engine="openpyxl")
df = df.drop('probe_src_addr', axis = 1)

#convert IP address to numeric number
for j in range(len(df)):
    df.iat[j, 0] = np.int64(int(ipaddress.IPv4Address(df.iat[j, 0])))
    df.iat[j, 2] = np.int64(int(ipaddress.IPv4Address(df.iat[j, 2])))

editName = filename[0]
editName = editName.replace('log_', '')
editName = editName.replace('_', '')
editName = editName.replace('.xlsx', '')
df['Time'] = np.int64(int(editName))

print(type(df.iat[0, 0]))
print(type(df.iat[0, 1]))
print(type(df.iat[0, 2]))
print(type(df.iat[0, 3]))

num = 1

for i in range(len(filename) - 1):

    print(filename[num])
    df2 = pd.read_excel("./data/" + filename[num], engine="openpyxl")
    df2 = df2.drop('probe_src_addr', axis = 1)
    for k in range(len(df2)):
        df2.iat[k, 0] = np.int64(int(ipaddress.IPv4Address(df2.iat[k, 0])))
        df2.iat[k, 2] = np.int64(int(ipaddress.IPv4Address(df2.iat[k, 2])))
    editName = filename[num]
    editName = editName.replace('log_', '')
    editName = editName.replace('_', '')
    editName = editName.replace('.xlsx', '')
    df2['Time'] = np.int64(int(editName))
    df = pd.concat([df, df2], axis = 0)
    num = num + 1

print(df)

# calculate and plot correlation matrix (heat map)
corr = df.corr(numeric_only = False)

sns.heatmap(corr,
            vmin=-1.0,
            vmax=1.0,
            center=0,
            cmap = 'coolwarm',
            annot=True,
            fmt='.1f',
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values
           )
plt.show()