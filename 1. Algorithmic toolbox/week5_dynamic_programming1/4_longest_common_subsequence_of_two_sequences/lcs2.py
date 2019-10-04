#Uses python3

def lcs2(s, t):
    d = [[0] * (len(t) + 1)]
    for i in range(1, len(s) + 1):
        d.append([0] * (len(t) + 1))
        for j in range(1, len(t) + 1):
            d[i][j] = max(d[i-1][j], d[i][j-1], d[i-1][j-1] + int(s[i-1] == t[j-1]))
    
    #write your code here
    return d[-1][-1]

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]

    m = int(input())
    b = [int(i) for i in input().split()]

    print(lcs2(a, b))
