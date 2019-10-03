# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
        
def min_and_max(i, j, M, m, ops):
    min_ = float('inf')
    max_ = -float('inf')
    for k in range(i, j):
        for x,y in [[M,M], [M,m], [m,M], [m,m]]:
            a = evalt(x[i][k], y[k+1][j], ops[k])
            min_ = min(a, min_)
            max_ = max(a, max_)
    
    return (min_, max_)

def get_maximum_value(dataset):
    n = (len(dataset) + 1) // 2
    ops = dataset[1::2]
    digits = [int(i) for i in dataset[::2]]
    M = [[0 for _ in range(n)] for _ in range(n)]
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i][j], M[i][j] = min_and_max(i, j, M, m, ops)
    return M[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
