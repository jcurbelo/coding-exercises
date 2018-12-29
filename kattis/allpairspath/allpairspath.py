def floyd_warshall(g, p, c):
    n = len(g)
    lst = xrange(n)
    for k in lst:
        for i in lst:
            for j in lst:
                if g[i][k] + g[k][j] < g[i][j]:
                    g[i][j] = g[i][k] + g[k][j]
                    p[i][j] = p[k][j]

    # Find negative cycles
    # for i in lst:
    # 	for j in lst:
    # 		v = p[i][j]
    # 		flag = False
    # 		while v:
    # 			if g[v][v] < 0:
    # 				c[i][j] = flag = True
    # 				break
    # 			# little case for non negative self edges
    # 			if p[i][v] == v:
    # 				break
    # 			v = p[i][v]
    # 		if flag:
    # 			break
    g_1 = [r[:] for r in g]
    for k in lst:
        for i in lst:
            for j in lst:
                if g_1[i][k] + g_1[k][j] < g_1[i][j]:
                    g_1[i][j] = g_1[i][k] + g_1[k][j]
                    c[i][j] = True

# def test():
# 	import networkx as nx
# 	import random
# 	weights = range(-1000, 1001)
# 	n, p = 150, 1
# 	inf  = float('inf')
# 	lst = xrange(n)
# 	g = nx.fast_gnp_random_graph(n, p, directed=True)
# 	g1 = [[inf if j != i else 0 for j in lst ] for i in lst]
# 	p = [[None] * n for _ in lst]
# 	c = [[False] * n for _ in lst]
# 	# Add weights
# 	for i, j in g.edges():
# 		w = random.choice(weights)
# 		g[i][j]['weight'] = g1[i][j] = w
# 	# d1 = [r[:] for r in g1]
# 	floyd_warshall(g1, p, c)
# 	d1 = nx.floyd_warshall(g)

# 	for i in lst:
# 		for j in lst:
# 			if d1[i][j] != g1[i][j]:
# 				print (i, j), d1[i][j], g1[i][j]


def main():
    first = True
    inf = float('inf')
    while True:
        def get_input(): return map(int, raw_input().split())
        n, m, q = get_input()
        lst = xrange(n)
        if n + m + q == 0:
            break
        if not first:
            print
        else:
            first = False
        g = [[inf if j != i else 0 for j in lst] for i in lst]
        p = [[None] * n for _ in lst]
        c = [[False] * n for _ in lst]
        for _ in xrange(m):
            u, v, w = get_input()
            g[u][v] = min(g[u][v], w)  # Assuming Multigraphs
            p[u][v] = u
        floyd_warshall(g, p, c)
        for _ in xrange(q):
            u, v = get_input()
            if g[u][v] != inf:
                if c[u][v]:
                    print '-Infinity'
                else:
                    print 0 if u == v else g[u][v]
            else:
                print 'Impossible'


if __name__ == '__main__':
    main()
