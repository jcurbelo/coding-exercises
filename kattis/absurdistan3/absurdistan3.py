def main():
	n = input()
	edges = set()
	for i in xrange(n):
		t = tuple([int(x) for x in raw_input().split(' ')])
		if t in edges:
			edges.add(t[::-1])
		else:
			edges.add(t)
	for a, b in edges:
		print a, b
if __name__=='__main__':
	main()