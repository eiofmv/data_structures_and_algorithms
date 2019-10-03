#Uses python3
import sys
from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class Heap:
    def __init__(self, unordered):
        self.data = unordered
        for i in range((len(self.data) + 1) // 2)[::-1]:
            self.sift_down(i)

    def extract_min(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        m = self.data.pop()
        self.sift_down()
        return m[0]

    def append(self, element):
        self.data.append(element)
        self.sift_up()

    def sift_up(self):
        v = len(self.data) - 1
        while self.data[v][1] < self.data[v // 2][1]:
            self.data[v], self.data[v // 2] = self.data[v // 2], self.data[v]
            v //= 2

    def sift_down(self, i=0):
        n = len(self.data)
        min_index = i
        if 2 * i + 1 < n:
            if self.data[2 * i + 1][1] < self.data[min_index][1]:
                min_index = 2 * i + 1
        if 2 * i + 2 < n:
            if self.data[2 * i + 2][1] < self.data[min_index][1]:
                min_index = 2 * i + 2
        if min_index != i:
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.sift_down(min_index)

    def is_empty(self):
        return len(self.data) == 0

def minimum_distance(x, y):
    result = 0.
    #write your code here
    dist = [distance(x[0], y[0], x[i], y[i]) for i in range(len(x))]
    heap = Heap([(i, dist[i]) for i in range(len(x))])
    used = set()

    while not heap.is_empty():
        u = heap.extract_min()
        if u in used:
            continue
        used.add(u)
        result += dist[u]
        for i in range(len(x)):
            if (i not in used)and(dist[i] > distance(x[u], y[u], x[i], y[i])):
                dist[i] = distance(x[u], y[u], x[i], y[i])
                heap.append((i, dist[i]))

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
