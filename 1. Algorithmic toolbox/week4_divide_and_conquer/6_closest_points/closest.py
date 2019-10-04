#Uses python3
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def binary_search(a, x):
    left, right = 0, len(a) - 1
    mid = (left + right) // 2
    if left > right:
        return left - 1
    if a[mid][0] == x:
        return mid
    elif a[mid][0] > x:
        return binary_search(a[:mid], x)
    else:
        return binary_search(a[mid+1:], x)

def minimum_distance(points):
    if len(points) == 2:
        return distance(points[0], points[1])
    if len(points) == 3:
        return min(distance(points[0], points[1]), distance(points[2], points[1]))
    mid = (len(points) - 1) // 2
    d1 = minimum_distance(points[:mid+1])
    d2 = minimum_distance(points[mid+1:])
    d = min(d1, d2)
    mid = (points[mid][0] + points[mid+1][0]) / 2
    x_min = binary_search(points, mid - d)
    x_max = binary_search(points, mid + d)
    y_sorted = sorted(points[x_min+1:x_max], key=lambda x: [x[1], x[0]])
    for i in range(len(y_sorted) - 1):
        for j in range(i + 1, min(len(y_sorted), i + 7)):
            dist = distance(y_sorted[i], y_sorted[j])
            if dist < d:
                d = dist        
    return d

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(i) for i in input().split(' ')])
    points = sorted(points, key=lambda x: [x[0], x[1]])
    print("{0:.9f}".format(minimum_distance(points)))
