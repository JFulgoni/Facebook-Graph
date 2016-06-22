__author__ = 'johnfulgoni'

# https://plot.ly/ipython-notebooks/network-graphs/
# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html

import plotly.plotly as py
from plotly.graph_objs import *

import networkx as nx
import main

def create_graph(dataset, names):
    G = nx.Graph()
    for friend_list, name in zip(dataset, names):
        add_edges(G,friend_list, name)
    return G

def add_edges(G, friend_list, name):
    G.add_node(name)
    for friend in friend_list:
        G.add_node(friend)
        G.add_edge(name, friend)

if __name__ == '__main__':
    main.main()