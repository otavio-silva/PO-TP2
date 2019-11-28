import os
import mip
import networkx
from matplotlib import pyplot

g = networkx.to_undirected(networkx.read_edgelist(os.path.join("data", "Email-Enron.txt")))
n = len(g.nodes)

model = mip.Model("Independent Set")
x = [model.add_var(var_type=mip.BINARY) for _ in range(n)]
model.objective = mip.maximize(mip.xsum(x[i] for i in range(n)))
for (i, j) in g.edges:
	model += mip.xsum([x[int(i)], x[int(j)]]) <= 1
model.optimize()
selected = [i for i in range(n) if x[i].x >= 0.99]
g1 = g.subgraph(selected)
print(selected)