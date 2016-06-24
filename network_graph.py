__author__ = 'johnfulgoni'

# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
# https://plot.ly/ipython-notebooks/network-graphs/

import plotly.plotly as py
import plotly.graph_objs as go

import networkx as nx
import main
import matplotlib.pyplot as plt

def create_graph(dataset, names, key_list):
    G = nx.Graph()
    for friend_list, name in zip(dataset, names):
        add_edges(G,friend_list, name, key_list)
    return G

def add_edges(G, friend_list, name, key_list):
    G.add_node(key_list[name])
    for friend in friend_list:
        G.add_node(key_list[friend])
        G.add_edge(key_list[name], key_list[friend])

def print_edges(G):
    edges = G.edges()
    for edge in edges:
        print edge

def mat_draw(G):
    pos=nx.spring_layout(G)   #G is my graph

    nx.draw(G,pos,node_color='#A0CBE2',edge_color='#ff944d',width=0.5,edge_cmap=plt.cm.Blues,with_labels=True)
    #plt.savefig("graph.pdf")
    plt.savefig("graph.png", dpi=1000)

if __name__ == '__main__':
    main.main()