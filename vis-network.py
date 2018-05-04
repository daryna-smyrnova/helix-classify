
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import nxviz as nv
from sklearn.cluster import KMeans


filein = 'clean_data'


network = pd.read_csv(filein, sep = '\t', header = 0)

f1 = network['node1'].values
f2 = network['node2'].values
f3 = network['count'].values
X = np.array(list(zip(f1, f2)))
plt.scatter(f1, f2, c='black', s=7)
#plt.show()



#kmeans = KMeans(n_clusters=3)
#kmeans = kmeans.fit(network)
#labels = kmeans.predict(network)
#centroids = kmeans.cluster_centers_
#len(labels)
#network['cluster'] = labels
#network['distance'] = 1/labels
#network.head(20)
#print (labels)


G=nx.OrderedGraph()
G=nx.from_pandas_dataframe(network, 'node1', 'node2', ['count'])
for n in G.nodes():
    G.node[n]['connectivity'] = float(len(list(G.neighbors(n))))
#ap = nv.BasePlot(G, node_grouping='cluster', node_color = 'connectivity', node_size = 'cluster', node_label='connectivity')

color = nx.betweenness_centrality(G,weight='count').values()
nx.draw(G, cmap = plt.get_cmap('jet'), alpha=0.4, node_order = 'count', node_color=color, node_size=65, with_labels=True, font_size=8, radius=20)
        #ap.draw()
#plt.show()
plt.savefig('network.png', dpi=300)



cutsets = list(nx.all_node_cuts(G))
len(cutsets)


# In[10]:

all(1 == len(cutset) for cutset in cutsets)


# In[11]:

color


# In[12]:

color.items()

