import mip
import networkx

n1 = 2 ** 10
n2 = 2 ** 11

g = networkx.to_undirected(networkx.complete_bipartite_graph(n1, n2))
n = len(g.nodes)

model = mip.Model("Clique")
x = [model.add_var(var_type=mip.BINARY) for _ in range(n)]
model.objective = mip.maximize(mip.xsum(i for i in x))
for (i, j) in networkx.complement(g).edges:
	model += mip.xsum([x[i], x[j]]) <= 1
model.optimize()
selected = [i for i in range(n) if x[i].x >= 0.99]
g1 = g.subgraph(selected)
print(selected)
