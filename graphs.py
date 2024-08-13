import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_edges_from([(1, 2), (1, 3)])
G.add_node("spam")
G.add_nodes_from("spam")
G.add_edge(3, 'm')
print(G.number_of_nodes(), G.number_of_edges())
nx.draw(G, with_labels=True, font_color="Whitesmoke")
plt.show()
