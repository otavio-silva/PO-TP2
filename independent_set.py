import mip
import networkx
from matplotlib import pyplot

g = networkx.to_undirected(networkx.read_edgelist("Email-Enron.txt"))
n = len(g.nodes)
networkx.drawing.draw_networkx(g)
pyplot.show()

model = mip.Model("Independent Set")
x = [model.add_var(var_type=mip.BINARY) for _ in range(n)]
model.objective = mip.maximize(mip.xsum(x[i] for i in range(n)))
for (i, j) in g.edges:
	model += mip.xsum([x[int(i)], x[int(j)]]) <= 1
model.optimize()
selected = [i for i in range(n) if x[i].x >= 0.99]
print(selected)
g1 = g.subgraph(selected)
networkx.drawing.draw_networkx(g1)
pyplot.show()