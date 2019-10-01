# python3

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]

    max1, max2 = max(a[0], a[1]), min(a[0], a[1])

    for i in range(2, n):
        if a[i] >= max1:
            max2 = max1
            max1 = a[i]
        elif a[i] >= max2:
            max2 = a[i]

    print(max1 * max2)
