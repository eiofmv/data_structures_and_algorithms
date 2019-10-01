# Uses python3

def edit_distance(s, t):
    d = [list(range(len(t) + 1))]
    for i in range(1, len(s) + 1):
        d.append(list(range(i, i + len(t) + 1)))
        for j in range(1, len(t) + 1):
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + int(s[i-1] != t[j-1]))

    #write your code here
    return d[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
