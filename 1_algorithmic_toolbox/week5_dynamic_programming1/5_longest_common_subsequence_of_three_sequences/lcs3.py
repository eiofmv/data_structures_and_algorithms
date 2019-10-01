#Uses python3

def lcs3(s, t, v):
    d = [[[0 for _ in range(len(v) + 1)] for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            for k in range(1, len(v) + 1):
                d[i][j][k] = max(d[i-1][j][k], 
                                 d[i][j-1][k], 
                                 d[i][j][k-1], 
                                 d[i-1][j-1][k-1] + int((s[i-1] == t[j-1]) and (t[j-1] == v[k-1])))
    
    #write your code here	
    return d[-1][-1][-1]

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]

    n = int(input())
    b = [int(i) for i in input().split()]

    n = int(input())
    c = [int(i) for i in input().split()]
    print(lcs3(a, b, c))
