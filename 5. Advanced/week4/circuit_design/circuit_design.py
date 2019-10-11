# python3
import sys
import threading


sys.setrecursionlimit(10**6)
threading.stack_size(2**26)


# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
def dfs(adj, used, order, x, scc=1):
    used[x] = scc
    for i in adj[x]:
        if not used[i]:
            dfs(adj, used, order, i, scc)
    order.append(x)


def strongly_connected_components(adj, reversed_adj):
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
            dfs(adj, used, order, i, result)

    return used, result

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n, m = data[0:2]
#     data = data[2:]
#     edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#     adj = [[] for _ in range(n)]
#     reversed_adj = [[] for _ in range(n)]
#     for (a, b) in edges:
#         adj[a - 1].append(b - 1)
#         reversed_adj[b - 1].append(a - 1)
#     print(strongly_connected_components(adj, reversed_adj))


def isSatisfiable(clauses, n):
    adj = [set() for _ in range(2 * n + 1)]
    reversed_adj = [set() for _ in range(2 * n + 1)]
    for (a, b) in clauses:
        adj[-a + n].add(b + n)
        adj[-b + n].add(a + n)
        reversed_adj[b + n].add(-a + n)
        reversed_adj[a + n].add(-b + n)

    scc, scc_num = strongly_connected_components(adj, reversed_adj)
    for i in range(1, n + 1):
        if scc[n - i] == scc[n + i]:
            return None


    result = [-1] * n
    for i in sorted(range(2 * n + 1), key=lambda x: scc[x]):
        if i == n:
            continue
        if result[abs(i - n) - 1] == -1:
            result[abs(i - n) - 1] = int(i > n)

    return result


def main():
    n, m = map(int, input().split())
    clauses = [list(map(int, input().split())) for i in range(m)]

    result = isSatisfiable(clauses, n)
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE");
        print(" ".join(str(-i-1 if not result[i] else i+1) for i in range(n)))

threading.Thread(target=main).start()