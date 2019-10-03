#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(adj, used, order, x):
    # write your code here
    used[x] = 1
    for i in adj[x]:
        if not used[i]:
            dfs(adj, used, order, i)
    order.append(x)

def number_of_strongly_connected_components(adj, reversed_adj):
    result = 0
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if not used[i]:
            dfs(reversed_adj, used, order, i)

    used = [0] * len(adj)
    for i in order[::-1]:
        if not used[i]:
            result += 1
            dfs(adj, used, order, i)
    #write your code here
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    reversed_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        reversed_adj[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, reversed_adj))
