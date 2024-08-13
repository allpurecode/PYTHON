# opening blank canvas
'''import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nx.draw(G, with_labels=True, font_color="whitesmoke")
plt.show()'''

# creating nodes
'''import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
#G.add_nodes_from([2, 5])
G = nx.path_graph(10)
nx.draw(G, with_labels=True, font_color="whitesmoke")
plt.show()'''

# adding edges and nodes
'''import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_edges_from([(1, 2), (1, 3)])
G.add_node("spam")
G.add_nodes_from("spam")
G.add_edge(3, 'm')
print(G.number_of_nodes(), G.number_of_edges())
print(list(G.nodes))
print(list(G.edges))
print(G.adj[1])
print(G.degree[1])

nx.draw(G, with_labels=True, font_color="Whitesmoke")
plt.show()'''

# for directed graphs use DG=nx.DiGraph()
'''import networkx as nx
import matplotlib.pyplot as plt

MG = nx.MultiDiGraph()
MG.add_weighted_edges_from([(1, 2, 3), (2, 1, .5), (2, 3, .5)])
nx.draw(MG, with_labels=True, font_color="Whitesmoke")
plt.show()
print(MG.degree(1))'''

'''import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()
subax1 = plt.subplot(221)
nx.draw_random(G)
subax2 = plt.subplot(222)
nx.draw_circular(G)
subax3 = plt.subplot(223)
nx.draw_spectral(G)
subax4 = plt.subplot(224) #the positions of the nodes are randomly chosen within the plotting area.
nx.draw_shell(G, nlist=[range(3, 10), range(5)])
plt.show()'''

'''import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
e_list = [(1, 2, 3), (2, 3, 4), (3, 1, 5)]
G.add_weighted_edges_from(e_list)
nx.draw(G,with_labels=True,font_color="white")
plt.show()'''

# multigraph
'''import networkx as nx
import matplotlib.pyplot as plt

M = nx.MultiGraph()
M.add_node(1)
M.add_nodes_from([2, 3])
M.add_nodes_from(range(100, 110))
H = nx.path_graph(10)
M.add_nodes_from(H)
M.add_edges_from(H.edges)
nx.draw(M, with_labels=True, font_color="white")
plt.show()'''



