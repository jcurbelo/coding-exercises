import sys

def main():
	lines = [l.rstrip("\r\n") for l in sys.stdin.readlines()]
	for l in lines:
		a, b = [int(x) for x in l.split()]
		print abs(a - b)

if __name__=='__main__':
	main()