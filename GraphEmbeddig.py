import networkx as nx
import numpy as np
from node2vec import Node2Vec
import matplotlib.pyplot as plt

# Load the Zachary Karate Club graph
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

# Generate node embeddings using node2vec
node2vec = Node2Vec(overlap_graph, dimensions=2, walk_length=30, num_walks=200)
model = node2vec.fit(window=10, min_count=1, batch_words=4)

# Get the node embeddings
emb = np.array([model.wv[str(i)] for i in range(len(overlap_graph))])

print(emb)

# Plot the graph using the node embeddings
pos = {i: emb[i] for i in range(len(overlap_graph))}
nx.draw(overlap_graph, pos=pos, with_labels=True)
plt.show()
