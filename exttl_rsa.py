import requests
import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import sys
import os
import plotly.express as px

import pycountry
from pycountry_convert import country_alpha2_to_country_name, country_name_to_country_alpha3

filename = os.listdir("C:/Users/anli/iris/ttl_rsa")
print(filename)

df = pd.read_excel("./ttl_rsa/" + filename[len(filename)-1], engine="openpyxl")

for k in range(len(df)):
    if(k == 153):
        df.iat[153, 1] = 'NAM'
    else:
        country = pycountry.countries.get(alpha_2=df.iat[k, 1])
        df.iat[k, 1] = country.alpha_3

for i in range(len(filename) - 1):
    df2  = pd.read_excel("./ttl_pdp/" + filename[len(filename) - i - 1], engine="openpyxl")
    for j in range(len(df2)):
        if(j == 153):
            df2.iat[153, 1] = 'NAM'
        else:
            df2.iat[j, 1] = pycountry.countries.get(alpha_2=str(df2.iat[j, 1])).alpha_3
    df = pd.concat([df2, df], axis=0)

#pd.set_option('display.max_rows', 500)
print(df)

fig = px.choropleth(df,
                    locations = "Country",
                    color = 'TTL', 
                    animation_frame="Time",
                    range_color=[0, df['TTL'].max()])

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
                    
fig.write_html("geoIP_TTL_rsa.html")
fig.show()