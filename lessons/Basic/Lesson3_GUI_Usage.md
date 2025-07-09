# Lesson 3 - Using the GUI

In this lesson we'll be explaining how to use and what are the usages of the CM-GUI.

## Clustering Algorithms

The GUI supports 4 different Algorithms:

- Leiden CPM
- Leiden Modularity
- Infomap
- Stochastic Block Model (SBM)


### Leiden (CPM and Modularity)

Leiden is an algorithm which is built upon the [Louvain clustering method](https://en.wikipedia.org/wiki/Louvain_method). 

In our GUI, we have 2 different versions of Leiden available. 

#### Leiden CPM (Constant-Potts Model)

Used when:

```python
algorithm == 'Leiden-CPM'
```

**Parameters:**

* `Resolution` (`res`) – *float*
  Controls the resolution parameter $\gamma$ for Constant Potts Model.
* `Iterations` (`i`) – *int*
  Number of times the Leiden CPM algorithm is run.


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






For a more in-depth explanation, please see [Traag et. Al](https://arxiv.org/pdf/1104.3083)



#### **2. Leiden-Mod**

Used when:

```python
algorithm == 'Leiden-Mod'
```

**Parameters:**

* `Iterations` (`i`) – *int*
  Number of times the modularity-based Leiden algorithm is run.


### **3. Infomap**

No need to pass parameters via GUI, only the input files.


### **4. Stochastic Block Model (SBM)**

Used when:

```python
algorithm == 'Stochastic Block Model (SBM)'
```

**Parameters:**

* `Block state` (`block_state`) – *str*
  Determines the variant of SBM:

  * `"Non Nested"`
  * `"Planted Partition Model"`
* `Degree corrected` – *bool*
  *(Only available if `"Non Nested"` is selected)*
  Whether to use the degree-corrected version of SBM.
