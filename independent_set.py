import mip
import networkx

n1 = 2 ** 10
n2 = 2 ** 11

g = networkx.to_undirected(networkx.complete_bipartite_graph(n1, n2))
n = len(g.nodes)

model = mip.Model("Independent Set")
x = [model.add_var(var_type=mip.BINARY) for _ in range(n)]
model.objective = mip.maximize(mip.xsum(x[i] for i in range(n)))
for (i, j) in g.edges:
	model += mip.xsum([x[int(i)], x[int(j)]]) <= 1
model.optimize()
selected = [i for i in range(n) if x[i].x >= 0.99]
print(selected)
g1 = g.subgraph(selected)