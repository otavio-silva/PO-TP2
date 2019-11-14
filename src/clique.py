import mip
import networkx
from matplotlib import pyplot

n = 2 ** 3
g = networkx.binomial_tree(n)
networkx.add_star(g, [i for i in range(n)])
networkx.drawing.draw_networkx(g)
pyplot.show()

model = mip.Model("Clique")
x = [model.add_var(var_type=mip.BINARY) for _ in range(len(g.nodes))]
model.objective = mip.maximize(mip.xsum(i for i in x))
for (i, j) in networkx.complement(g).edges:
	model += mip.xsum([x[i], x[j]]) <= 1
model.optimize()
selected = [i for i in range(len(g.nodes)) if x[i].x >= 0.99]
print(selected)
g1 = g.subgraph(selected)
networkx.drawing.draw_networkx(g1)
pyplot.show()