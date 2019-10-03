# Uses python3

def binary_search(a, x):
    left, right = 0, len(a) - 1
    while (right >= left):
        mid = (right + left) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1
    
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    a = list(map(int, input().split(' ')))[1:]
    points_to_search = list(map(int, input().split(' ')))[1:]
    for x in points_to_search:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
