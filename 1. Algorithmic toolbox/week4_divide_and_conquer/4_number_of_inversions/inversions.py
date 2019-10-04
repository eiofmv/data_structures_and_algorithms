# Uses python3

def merge(a, b):
    i = 0 
    j = 0
    result = []
    inversions = 0
    while (i < len(a))and(j < len(b)):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
            inversions += len(a) - i
    while (i < len(a)):
        result.append(a[i])
        i += 1
    while (j < len(b)):
        result.append(b[j])
        j += 1
    return result, inversions

def merge_sort(a):
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    v1, inv1 = merge_sort(a[:mid])
    v2, inv2 = merge_sort(a[mid:])
    result, inv = merge(v1, v2)
    return result, inv1 + inv2 + inv

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = n * [0]
    print(merge_sort(a)[1])
