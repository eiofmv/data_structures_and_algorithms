#Uses python3

import sys
import queue


class Heap:
    def __init__(self, a):
        self.data = [a]

    def extract_min(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        m = self.data.pop()
        self.sift_down()
        return m[0]

    def append(self, element):
        self.data.append(element)
        self.sift_up()

    def sift_up(self):
        v = len(self.data) - 1
        while self.data[v][1] < self.data[v // 2][1]:
            self.data[v], self.data[v // 2] = self.data[v // 2], self.data[v]
            v //= 2

    def sift_down(self, i=0):
        n = len(self.data)
        min_index = i
        if 2 * i + 1 < n:
            if self.data[2 * i + 1][1] < self.data[min_index][1]:
                min_index = 2 * i + 1
        if 2 * i + 2 < n:
            if self.data[2 * i + 2][1] < self.data[min_index][1]:
                min_index = 2 * i + 2
        if min_index != i:
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.sift_down(min_index)

    def is_empty(self):
        return len(self.data) == 0

def distance(adj, cost, s, t):
    #write your code here
    dist = [-1] * len(adj)
    dist[s] = 0
    heap = Heap((s, dist[s]))
    used = set()
    while not heap.is_empty():
        u = heap.extract_min()
        if u in used:
            continue
        used.add(u)
        for i in range(len(cost[u])):
            if (not dist[adj[u][i]] + 1)or(dist[adj[u][i]] > dist[u] + cost[u][i]):
                dist[adj[u][i]] = dist[u] + cost[u][i]
                heap.append((adj[u][i], dist[adj[u][i]]))
    return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
