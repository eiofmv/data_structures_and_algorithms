# python3

def sift_down(a, i):
    n = len(a)
    min_index = i
    if 2 * i + 1 < n:
        if a[2*i + 1] < a[min_index]:
            min_index = 2 * i + 1
    if 2 * i + 2 < n:
        if a[2*i + 2] < a[min_index]:
            min_index = 2 * i + 2
    if min_index != i:
        a[i], a[min_index] = a[min_index], a[i]
        return [[i, min_index]] + sift_down(a, min_index)
    return []

def build_heap(data):
    swaps = []
    for i in range((len(data) + 1) // 2)[::-1]:
        swaps += sift_down(data, i)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
