import requests
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sys
import os
import plotly.express as px


filename = os.listdir("C:/Users/anli/iris/probe_ttl")
print(filename)

df = pd.read_excel("./probe_ttl/" + filename[len(filename)-1], engine="openpyxl")
df = df.sort_values('TTL')

for i in range(len(filename) - 1):
    df2  = pd.read_excel("./probe_ttl/" + filename[len(filename) - i - 1], engine="openpyxl")
    df2 = df2.sort_values('TTL')
    df = pd.concat([df2, df], axis=0)

print(df)

fig = px.bar(df,x='TTL',y='Frequency',animation_frame='Time', range_y=(0,df['Frequency'].max()))
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 2000
                    
fig.write_html("probe_ttl.html")
fig.show()