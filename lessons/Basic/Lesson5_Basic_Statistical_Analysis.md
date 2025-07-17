# Lesson 5 - Analizing a Clustered Network

In this lesson we explain some statistical analysis that can be applied to a clustered network.


## Statistics - Introduction

We'll be looking at 4 different stats for the output clustering of either *Lesson 3* or *Lesson 4*. Those 4 statistics are:

- Node Coverage
- Cluster Size Distribution
- Cluster Density [Source](https://en.wikipedia.org/wiki/Dense_subgraph)
- Edge Cut Size

### Node Coverage

Node coverage is a network-level statistic that is defined as:

$$
N = \frac{n_c}{n}
$$

Where:

* $n_c$ is the number of nodes in clusters.
* $n$ is the number of nodes in the network.


To calculate it, you need to get each individual node id from the edge list and cluster file and compare both of them by number of nodes.


### Cluster Size Distribution

This is something that can be computed from the clustering file. You first need to calculat the size of each cluster, this can be done in many ways bu the simplest one would be using `pandas`. 

Here's a code snippet that loads in a clustering file and produces a plot showing the distribution of cluster sizes:

```py
import pandas as pd
import matplotlib.pyplot as plt

df_cluster = pd.read_csv("clustering.tsv", sep="\t", header=None, names=['node_id', 'cluster_id'], dtype=str)

values = df_cluster["cluster_id"].value_counts()

plt.figure(figsize=(8, 6))
plt.hist(values, bins=30, edgecolor='black')
plt.title("Distribution of Cluster Sizes")
plt.xlabel("Cluster Size (Number of Nodes)")
plt.ylabel("Frequency")
plt.show()
```

### Cluster Density

The **density** of a cluster $C' = (V', E')$ of an undirected graph is defined as:

$$
\text{density}(C') = \frac{|E'|}{|V'|}
$$

Where:

* $|E'|$ is the number of edges in the cluster.
* $|V'|$ is the number of vertices in the cluster.

To calculate this, you need to filter the cluster file by cluster, get the individual node ids and all edges between them from the edge list.



### Edge Cut Size

This is the number of edges that must be removed from each cluster to make it disjoint, creating 2 separate connected components.

