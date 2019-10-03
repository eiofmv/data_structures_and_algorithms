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
    return value[-1][-1]

if __name__ == '__main__':
    W, n = [int(i) for i in input().split(' ')]
    w = list(map(int, input().split(' ')))
    print(optimal_weight(W, w))
