import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
from sklearn.datasets import load_boston
 
import networkx as nx
from pyvis.network import Network

import sys

filename = sys.argv[1]
print(filename)

ind = []
val = []

df = pd.read_excel(filename, engine="openpyxl")
for index, value in df['probe_dst_prefix'].value_counts().iteritems():
    print(index, ': ', value)
    ind.append(str(index))
    val.append(value)


print(ind)
print(type(ind))
print(val)
print(type(val))

#####

net = Network()
net.add_node('132.227.123.8',color='Red', size=sum(val)/200)
for i in range(len(ind)):
    net.add_node(str(ind[i]), size=val[i]/5)
    net.add_edge('132.227.123.8', str(ind[i]), color='Green', width=val[i]/10)

#net.toggle_physics(True)
net.show_buttons(filter_=['physics', 'nodes'])
net.show('./connect/10000.html')