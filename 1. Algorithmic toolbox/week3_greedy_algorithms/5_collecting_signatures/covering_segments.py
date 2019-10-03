# Uses python3

def optimal_points(segments):
    segments = sorted(segments, key=lambda x: x[1])
    i = 0
    points = []
    while (i < len(segments)):
        right = segments[i][1]
        points += [right]
        while (i < len(segments))and(segments[i][0] <= right):
            i += 1
    return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(tuple(int(i) for i in input().split(' ')))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
