import sys

MAX_CLIQUES = [0]
G = [{}]
D = [{}]

def N(v):
	return G[0].get(v, set())

def BronKerbosch(R, P, X): 
	if not P and not X:
		MAX_CLIQUES[0] += 1
	coll = sorted(P, key=lambda v: D[0][v], reverse=True)
	for v in coll:
 		n_v = N(v)
 		if MAX_CLIQUES[0] > 1e3:
			return
		BronKerbosch(R | set([v]), P & n_v, X & n_v)
		P.remove(v)
		X.add(v)

def main():
	cursor = 0
	lines = [l.rstrip("\r\n") for l in sys.stdin.readlines()]
	lines_len = len(lines)
	while cursor < lines_len:
		n, m = [int(x) for x in lines[cursor].split()]
		MAX_CLIQUES[0] = 0
		G[0] = {}
		D[0] = {}
		P = set()
		cursor += 1	
		edges = lines[cursor: cursor + m]
		for e in edges:
			i, j = [int(x) for x in e.split()]
			G[0][i] = G[0].get(i, set()) | set([j])
			G[0][j] = G[0].get(j, set()) | set([i])
			P.add(i)
			P.add(j)
			D[0][i] = D[0].get(i, 0) + 1
			D[0][j] = D[0].get(j, 0) + 1
		BronKerbosch(set(), P, set())
		print MAX_CLIQUES[0] if MAX_CLIQUES[0] <= 1e3 else 'Too many maximal sets of friends.'
		cursor += (m + 1)


# def main():
# 	while True:
# 		G = {}
# 		P = set()
# 		n, m = [int(x) for x in raw_input().split()]
# 		P = set()
# 		for _ in xrange(m):
# 			i, j = [int(x) for x in raw_input().split()]
# 			G[i] = G.get(i, set()) | set([j])
# 			G[j] = G.get(j, set()) | set([i])
# 			P.add(i)
# 			P.add(j)
# 		BronKerbosch(set(), P, set())
# 		print MAX_CLIQUES[0] if MAX_CLIQUES[0] <= 1e3 else 'Too many maximal sets of friends.'
# 		try:
# 			raw_input()
# 		except EOFError:
# 			break

def test():
	import networkx as nx
	n, p = 128, 0.015
	g = nx.erdos_renyi_graph(n, p)
	print '|V|: ', n, '|E|: ', len(g.edges())
	print 'RUNNING NETWORKX ALGORITHM...'
	print 'CLIQUES: ', len(list(nx.find_cliques(g)))
	print 'RUNNING MY ALGORITHM...'
	P = set()
	for i, j in g.edges():
		G[0][i] = G[0].get(i, set()) | set([j])
		G[0][j] = G[0].get(j, set()) | set([i])
		D[0][i] = D[0].get(i, 0) + 1
		D[0][j] = D[0].get(j, 0) + 1		
		P.add(i)
		P.add(j)
	BronKerbosch(set(), P, set())
	print 'CLIQUES: ', MAX_CLIQUES[0] if MAX_CLIQUES[0] <= 1e3 else 'Too many maximal sets of friends.'	

if __name__=='__main__':
	test()