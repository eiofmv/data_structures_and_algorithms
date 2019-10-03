# Uses python3
import random

def partition3(a, l, r):
    x = a[l]
    j1 = l
    j2 = l
    for i in range(l + 1, r + 1):
        if a[i] == x:
            j2 += 1
            a[i], a[j2] = a[j2], a[i]

        if a[i] < x:
            j2 += 1            
            a[j2], a[j1] = a[j1], a[j2]
            j1 += 1
            a[i], a[j1] = a[j1], a[i]


    a[l], a[j2] = a[j2], a[l]
    k = j
    return j1, j2
    #write your code here
    #pass

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = l + r + (l + r) // 2 - min(l, r, (l + r) // 2) - max(l, r, (l + r) // 2)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0] - 1);
    randomized_quick_sort(a, m[1] + 1, r);


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split(' ')))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
