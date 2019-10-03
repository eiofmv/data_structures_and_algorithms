# python3
import sys

def solve (text, n, patterns):
	result = []

	tree = {0: {}}
	for p in patterns:
		prev = 0
		for i in p:
			if i not in tree[prev]:
				size = len(tree)
				tree[prev][i] = size
				prev = size
				tree[prev] = {}
			else:
				prev = tree[prev][i]

	for i in range(len(text)):
		prev = 0
		k = i
		s = text[k]
		while text[k] in tree[prev]:
			prev = tree[prev][text[k]]
			k += 1
			if len(tree[prev]) == 0:
				result.append(i)
				break
			if k == len(text):
				break


	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
