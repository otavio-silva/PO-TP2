import mip
import networkx
from matplotlib import pyplot

n1 = 1000
n2 = 2000
g = networkx.complete_bipartite_graph(n1, n2)
networkx.drawing.draw_networkx(g)
pyplot.show()

model = mip.Model("Independent Set")
x = [model.add_var(var_type=mip.BINARY) for _ in range(len(g.nodes))]
model.objective = mip.maximize(mip.xsum(x[i] for i in range(len(g.nodes))))
for (i, j) in g.edges:
	model += mip.xsum([x[i], x[j]]) <= 1
model.optimize()
selected = [i for i in range(len(g.nodes)) if x[i].x >= 0.99]
print(selected)
g1 = g.subgraph(selected)
networkx.drawing.draw_networkx(g1)
pyplot.show()