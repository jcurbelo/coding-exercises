import sys

def main():
	lines = [l.rstrip("\r\n") for l in sys.stdin.readlines()]
	vars, lit = {}, {}
	for l in lines:
		tokens = l.split()
		cmd = tokens[0]
		if cmd == 'def':
			v, l = tokens[1], int(tokens[2])
			vars[v] = l
			lit[l] = v
		elif cmd == 'calc':
			lst = tokens[1:]
			exp = ' '.join(lst)
			ans, curr, add = 'unknown', 0, True
			for t in lst[:-1]:
				if t == '+':
					add = True
					continue
				if t == '-':
					add = False
					continue
				if t not in vars:
					curr = None
					break
				l = vars[t]
				curr += l if add else -l
			print exp, lit.get(curr, ans)
		else:
			vars, lit = {}, {}


if __name__=='__main__':
	main()