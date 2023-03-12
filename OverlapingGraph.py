import networkx as nx
import matplotlib.pyplot as plt

# Define a function to compute the overlap between two DNA reads
def compute_overlap(read1, read2):
    overlap = 0
    k = min(len(read1), len(read2))
    for i in range(k):
        if read1[-k+i:] == read2[:k-i]:
            overlap = k-i
    return overlap

# Define a list of DNA reads
reads = ['ATGGCGTCCG', 'CCGTGTTAGTAC', 'TACGAGTGGC', 'GCTGATCAGT', 'AGTACGAGT', 'TGGCAGTAC', 'GTCCGCTGAT', 'GTTAGTACG', 'ATCAGTACG', 'AGTGGCAG']

# Create a directed graph to represent the overlap relationships between the reads
overlap_graph = nx.DiGraph()
for i in range(len(reads)):
    for j in range(len(reads)):
        if i != j:
            overlap = compute_overlap(reads[i], reads[j])
            if overlap > 0:
                overlap_graph.add_edge(i, j, weight=overlap)

# Draw the overlap graph
pos = nx.circular_layout(overlap_graph)
nx.draw_networkx_nodes(overlap_graph, pos)
nx.draw_networkx_edges(overlap_graph, pos)
nx.draw_networkx_labels(overlap_graph, pos)
labels = nx.get_edge_attributes(overlap_graph, 'weight')
nx.draw_networkx_edge_labels(overlap_graph, pos, edge_labels=labels)
plt.axis('off')
plt.show()
