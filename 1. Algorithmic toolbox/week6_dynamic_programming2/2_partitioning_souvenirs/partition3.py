# Uses python3

def optimal_weight(W, w):
    value = [[0 for _ in range(W + 1)] for _ in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, W + 1):
            value[i][j] = value[i-1][j]
            if w[i-1] <= j:
                val = value[i-1][j-w[i-1]] + w[i-1]
                if value[i][j] < val:
                    value[i][j] = val
    # write your code here
    ans = [0 for _ in range(len(w))]
    x, y = len(w), W
    for i in range(len(w))[::-1]:
        if (w[i] <= y)and(value[x-1][y] <= value[x-1][y-w[i]] + w[i]):
            ans[i] = 1
            y -= w[i]   
        x -= 1
    return value[-1][-1], ans

if __name__ == '__main__':
    n = int(input())
    w = list(map(int, input().split(' ')))
    W = sum(w) // 3
    if (sum(w) % 3 != 0)or(len(w) < 3):
        print(0)
    else:
        W1, values = optimal_weight(W, w)
        if W1 != W:
            print(0)
        else:
            w1 = []
            for i in range(len(w)):
                if not values[i]:
                    w1.append(w[i])
            w = w1
            W1, values = optimal_weight(W, w)
            if W1 != W:
                print(0)
            else:
                w1 = []
                for i in range(len(w)):
                    if not values[i]:
                        w1.append(w[i])
                w = w1
                print(int(sum(w) == W))
                
# import sys
# import itertools

# def partition3(A):
#     for c in itertools.product(range(3), repeat=len(A)):
#         sums = [None] * 3
#         for i in range(3):
#             sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

#         if sums[0] == sums[1] and sums[1] == sums[2]:
#             return 1

#     return 0

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *A = list(map(int, input.split()))
#     print(partition3(A))
