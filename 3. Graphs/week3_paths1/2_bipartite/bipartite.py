#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    color = [-1] * len(adj)
    color[0] = 0
    q = queue.Queue()
    q.put(0)
    while not q.empty():
        u = q.get()
        for i in adj[u]:
            if not (color[i] + 1):
                q.put(i)
                color[i] = (color[u] + 1) % 2
            elif color[i] == color[u]:
                return 0
    return 1

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
    print(bipartite(adj))
