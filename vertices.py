import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter the number of vertices: "))

if n > 3:
    G = nx.complete_graph(n)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.title(f'Graph with {n} Vertices')
    plt.show()
else:
    print("Please enter a number greater than 3 to create a complete graph.")