#Uses python3

import sys

def explore(x, adj, explored):
    explored[x] = 1
    for v in adj[x]:
        if not explored[v]:
            explore(v, adj, explored) 


def number_of_components(adj):
    result = 0
    explored = [0] * len(adj)
    for v in range(len(adj)):
        if not explored[v]:
            result += 1
            explore(v, adj, explored)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
