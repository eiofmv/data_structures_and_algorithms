#Uses python3

import sys
import queue


def negative_cycle(adj, cost):
    #write your code here
    dist = [0] * len(adj)
    ans = False
    for j in range(len(adj)):
        cycle = False
        for k in range(len(adj)):
            for n, v in enumerate(adj[k]):
                if dist[v] > dist[k] + cost[k][n]:
                    dist[v] = dist[k] + cost[k][n]
                    cycle = True
    return int(cycle)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
