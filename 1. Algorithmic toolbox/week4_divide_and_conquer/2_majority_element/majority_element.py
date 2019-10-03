# Uses python3

def get_majority_element(a, left, right):
    if left == right:
        return a[left]
    mid = (left + right) // 2
    m1 = get_majority_element(a, left, mid)
    m2 = get_majority_element(a, mid + 1, right)
    count1 = 0
    count2 = 0
    for i in range(left, right + 1):
        if a[i] == m1:
            count1 += 1
        if a[i] == m2:
            count2 += 1
    if count1 > (right - left + 1) / 2:
        return m1
    if count2 > (right - left + 1) / 2:
        return m2
    #write your code here
    return -1

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split(' ')]
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)
