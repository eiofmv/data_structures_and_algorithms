# Uses python3
import sys

def get_change(m):
    a = [0, 1, 2, 1, 1]
    if m <= 4:
        return a[m]
    i = 4
    while i < m:
        a.append(a.pop(0))
        i += 1
        a[-1] = min(a[-5], a[-4], a[-2]) + 1
    #write your code here
    return a[-1]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
