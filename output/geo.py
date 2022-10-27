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

filename = sys.argv[1]
print(filename)

#ISO code 2
tmpISO = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR",
"AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE",
"BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO",
"BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD",
"CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI",
"HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG",
"SV", "GQ", "ER", "EE", "ET", "FK", "FO", "FJ", "FI", "FR", "GF",
"PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD",
"GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN",
"HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT",
"JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG",
"LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK",
"MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT",
"MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA",
"NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP",
"NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN",
"PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN",
"LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC",
"SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES",
"LK", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ",
"TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV",
"UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN",
"VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]

# ISO Code 3
ISO = []
for k in range(len(tmpISO)):
    ISO.append(pycountry.countries.get(alpha_2=tmpISO[k]).alpha_3)

print(ISO)
print(str(len(ISO)))


iso_list = [0] * len(ISO)
print(iso_list)
print(str(len(iso_list)))

ind = []
val = []

df = pd.read_excel(filename, engine="openpyxl")
for index, value in df['probe_dst_prefix'].value_counts().items():
    print(index, ': ', value)
    ind.append(str(index))
    val.append(value)

print(val)

num = 0
for i in range(len(ind)):
    
    # IP address to test
    ip_address = ind[i]

    # URL to send the request to
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    # Send request and decode the result
    response = requests.get(request_url)
    result = response.content.decode()
    # Clean the returned string so it just contains the dictionary data for the IP address
    result = result.split("(")[1].strip(")")
    # Convert this data into a dictionary
    result  = json.loads(result)
    print(result)
    print(result['country_code'])
    
    #add frequency to iso_list
    count = 0
    for j in range(len(ISO)):
        if (tmpISO[count]) == (result['country_code']):
            print(count)
            iso_list[count] = iso_list[count] + val[num]
            print(val[num])
        count = count + 1

    num = num + 1
    

data = pd.DataFrame(
    data={'ISO': ISO, 
          'Frequency': iso_list}
)

print(data)

fig = px.choropleth(data,
                    locations = "ISO",
                    color = 'Frequency', 
                    animation_frame="Year",
                    range_color=[0, max(iso_list)])
                    
fig.write_html("./probe_dst_prefix/geo_100000.html")
fig.show()