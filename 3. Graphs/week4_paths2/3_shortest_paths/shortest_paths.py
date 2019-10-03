#Uses python3

import sys
import queue

def bfs(adj, s, shortest):
    #write your code here
    shortest[s] = 0
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for i in adj[u]:
            if shortest[i]:
                q.put(i)
                shortest[i] = 0


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    reachable[s] = 1
    distance[s] = 0
    used = set()
    cycle = queue.Queue()
    for _ in range(len(adj)):
        for k in range(len(adj)):
            for n, v in enumerate(adj[k]):
                if (reachable[k])and(not reachable[v] or distance[v] > distance[k] + cost[k][n]):
                    reachable[v] = 1
                    distance[v] = distance[k] + cost[k][n]
                    if _ == len(adj) - 1:
                        cycle.put(v)

    while not cycle.empty():
        u = cycle.get()
        if shortest[u]:
            shortest[u] = 0
            for i in adj[u]:
                if shortest[i]:
                    cycle.put(i)

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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

