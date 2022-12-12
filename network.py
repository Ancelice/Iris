import requests
import json

import pandas as pd
import numpy as np
import sys
import os
import openpyxl

import networkx as nx
from pyvis.network import Network

#####

filename = os.listdir("C:/Users/anli/iris/pdp_rsa")
print(filename)

#####

for i in range(len(filename)):

    df = pd.read_excel("./pdp_rsa/" + filename[i], engine="openpyxl")

    PDP = df['probe_dst_prefix'].unique().tolist()
    RSA = df['reply_src_addr'].unique().tolist()

    pdp = df['probe_dst_prefix'].nunique()
    rsa = df['reply_src_addr'].nunique()

    print(filename[i])
    print('pdp : ' + str(pdp))
    print('rsa : ' + str(rsa))

    net = ''
    net = Network('950px', '1200px')
    net.add_node('132.227.123.8', color='Purple', size=100)

    for j in range(rsa):
        net.add_node(str(RSA[j]), color='Purple', size=1)
        net.add_edge('132.227.123.8', str(RSA[j]), color='Red', size=1)

    for k in range(pdp):
        net.add_node(str(PDP[k]), color='Purple', size=20)

    for n in range(len(df)):
        net.add_edge(str(df.iat[n, 0]), str(df.iat[n, 1]), color='Blue', size=1)

    tmpName = filename[i]
    tmpName = tmpName.replace('./data', '')
    tmpName = tmpName.replace('log_', '')
    tmpName = tmpName.replace('/', '_')
    tmpName = tmpName.replace('.xlsx', '')
    tmpName = './RESULT/network/' + tmpName + '_' + str(pdp) + '_' + str(rsa) + '.html'
    print(tmpName)

    net.show_buttons(filter_=['physics', 'nodes'])
    net.show(tmpName)