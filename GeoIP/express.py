import requests
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sys
import os
import plotly.express as px


filename = os.listdir("C:/Users/anli/iris/GeoIP/probe_dst_prefix")
print(filename)

df = pd.read_excel("./probe_dst_prefix/" + filename[len(filename)-1], engine="openpyxl")

for i in range(len(filename) - 1):
    df2  = pd.read_excel("./probe_dst_prefix/" + filename[len(filename) - i - 1], engine="openpyxl")
    df = pd.concat([df2, df], axis=0)

#pd.set_option('display.max_rows', 500)
print(df)

fig = px.choropleth(df,
                    locations = "Country",
                    color = 'Frequency', 
                    animation_frame="Time",
                    range_color=[0, df['Frequency'].max() * 0.9])

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 2000
                    
fig.write_html("geoIP_probe_dst_prefix.html")
fig.show()