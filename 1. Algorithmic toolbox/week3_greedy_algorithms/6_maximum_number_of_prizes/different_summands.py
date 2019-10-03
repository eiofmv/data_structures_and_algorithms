# Uses python3
from math import sqrt

def optimal_summands(n):
    max_i = int((-1 + sqrt(1 + 8*n)) / 2)
    lag = n - ((1 + max_i) * max_i) // 2
    summands = list(range(1, max_i+1))
    summands[-1] += lag
    #write your code here
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
