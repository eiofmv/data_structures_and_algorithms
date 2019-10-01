#Uses python3

import sys

def explore(x, adj, explored):
    explored[x] = 1
    for v in adj[x]:
        if not explored[v]:
            explore(v, adj, explored) 

def reach(adj, x, y):
    explored = [0] * len(adj)
    explore(x, adj, explored)
    return explored[y]

def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))

if __name__ == '__main__':
    main()
