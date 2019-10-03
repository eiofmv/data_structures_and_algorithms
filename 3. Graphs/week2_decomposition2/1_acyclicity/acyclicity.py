#Uses python3

import sys

def dfs(adj, used, order, x):
    # write your code here
    used[x] = 1
    ans = False
    order.append(x)
    for i in adj[x]:
        if not used[i]:
            ans |= dfs(adj, used, order, i)
        if i in order:
            return True
    order.pop()
    return ans
        
        

def acyclic(adj):
    used = [0] * len(adj)
    ans = False
    for i in range(len(adj)):
        if not used[i]:
            ans |= dfs(adj, used, [], i)
    
    return int(ans)

def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

if __name__ == '__main__':
    main()
