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
for i in range(len(ind)):
    net.add_node(str(ind[i]), size=val[i]/5)

#net.toggle_physics(True)
net.show_buttons(filter_=['physics', 'nodes'])
net.show('./probe_dst_prefix/100000.html')