def floyd_warshall(g, t, c):
	n = len(g)
	for k in xrange(n):
		for i in xrange(n):
			for j in xrange(n):
				g[i][j] = min(g[i][j], g[i][k] + g[k][j])
				t[i][j] = t[i][j] or (t[i][k] and t[k][j])

	# Find negative cycles
	for k in xrange(n):
		for i in xrange(n):
			for j in xrange(n):
				if g[i][k] + g[k][j] < g[i][j]:
					c[i][j] = True
					break

def main():
	first = True
	max_w = 1e3 + 1
	while True:
		get_input = lambda : map(int, raw_input().split())
		n, m, q = get_input()
		if n + m + q == 0:
			break
		if not first:
			print
		else:
			first = False
		g = [[max_w] * n for _ in xrange(n)]
		t = [[False] * n for _ in xrange(n)]
		c = [[False] * n for _ in xrange(n)]
		for _ in xrange(m):
			u, v, w = get_input()
			g[u][v] = w
			t[u][v] = True
		floyd_warshall(g, t, c)
		for _ in xrange(q):
			u, v = get_input()
			if t[u][v]:
				print 0 if u == v else g[u][v] if not c[u][v] else '-Infinity'
			else:
				print 'Impossible'
			

if __name__ == '__main__':
	main()