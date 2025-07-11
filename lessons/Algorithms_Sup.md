# Algorithm Explanations


## Leiden CPM (Constant-Potts Model)

CPM is a way of grouping together nodes based on the following formula:

$$
\mathcal{H} = - \sum_{ij} \left( A_{ij} w_{ij} - \gamma \right) \delta(\sigma_i, \sigma_j)
$$


| **Symbol**                   | **Meaning**                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------- |
| $\mathcal{H}$                | Total energy (the value we want to **minimize**)                                       |
| $\sum_{ij}$                  | Sum over **all pairs** of nodes $i$ and $j$                                            |
| $A_{ij}$                     | Entry in the **adjacency matrix**: 1 if edge exists between $i$ and $j$, else 0        |
| $w_{ij}$                     | **Weight** of the edge between nodes $i$ and $j$                                       |
| $\gamma$                     | **Resolution parameter**: constant set by the User |
| $\delta(\sigma_i, \sigma_j)$ | Equals 1 if nodes $i$ and $j$ are in the **same community**; otherwise 0               |

In out GUI, there is no weight between the edges, we are looking only at the existence of edges between nodes. In this case, $w_{ij} = 1$ always.

The "Constant" in CPM is a reference to the Resolution Parameter, which you can pass to the GUI as a parameter

For a more in-depth explanation, please see [Traag et. Al](https://www.nature.com/articles/s41598-019-41695-z)

## Leiden Modularity

Modularity, as a concept, is a method that tries to maximise the difference between the actual number of edges in a community and the expected number of such edges. It is given by the following formula:

$$
\mathcal{H} = \frac{1}{2m} \sum_c \left( e_c - \gamma \frac{K_c^2}{2m} \right)
$$


| Symbol        | Meaning                                                                 |
|---------------|-------------------------------------------------------------------------|
| $\mathcal{H}$| Modularity score (objective function being maximized)                  |
| $m$       | Total number of edges in the network                                     |
| $c$       | A community (subset of nodes in the network)                            |
| $e_c$     | Number of edges **within** community $c$                           |
| $K_c$     | Sum of the degrees of all nodes in community $c$                   |
| $\gamma$  | Resolution parameter (controls granularity of the communities detected) |

For a more in-depth explanation, please see [Traag et. Al](https://www.nature.com/articles/s41598-019-41695-z)

## Infomap

$$
L(M) = q_{\curvearrowright} H(\mathcal{Q}) + \sum_{i=1}^{m} p_{\circlearrowright}^i H(\mathcal{P}^i)
$$


| Symbol                         | Meaning                                                                 |
|--------------------------------|-------------------------------------------------------------------------|
| $L(M)$                     | Description length of the random walk using partition $M$          |
| $q_{\curvearrowright}$     | Probability of exiting a module (community)                            |
| $H(\mathcal{Q})$           | Entropy of the index codebook (used when jumping between modules)      |
| $m$                        | Number of modules (communities) in the network                         |
| $p_{\circlearrowright}^i$  | Probability of visiting module $i$ and staying within it           |
| $H(\mathcal{P}^i)$         | Entropy of the codebook within module $i$                          |

For a more in-depth explanation please visit [mapequation.org/infomap](https://www.mapequation.org/infomap/)