import mip
import networkx

n1 = 1000
n2 = 2000
g = networkx.complete_bipartite_graph(n1, n2)

model = mip.Model("Independent Set")
x = [model.add_var(var_type=mip.BINARY) for _ in range(n1 + n2)]
model.objective = mip.maximize(mip.xsum(x[i] for i in range(n1 + n2)))
for (i, j) in g.edges:
	model += mip.xsum([x[i], x[j]]) <= 1
#model += mip.xsum(x[i] + x[j] for (i, j) in g.edges) <= 1
model.optimize()
selected = [i for i in range(n1 + n2) if x[i].x >= 0.99]
print(selected)