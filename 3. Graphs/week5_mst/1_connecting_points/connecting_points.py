#Uses python3
import sys
from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class Database:
    def __init__(self, n):
        self.rank = [0] * n
        self.parents = list(range(n))

    def merge(self, dst, src):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent != dst_parent:
            if self.rank[src_parent] > self.rank[dst_parent]:
                dst_parent, src_parent = src_parent, dst_parent

            self.rank[dst_parent] += int(self.rank[src_parent] == self.rank[dst_parent])
            self.parents[src_parent] = dst_parent

    def get_parent(self, table):
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]

def clustering(x, y, k):
    #write your code here
    adj = []
    for i in range(len(x) - 1):
        for j in range(i, len(x)):
            adj.append((i, j, distance(x[i], y[i], x[j], y[j])))

    db = Database(len(x))

    adj = sorted(adj, key=lambda x: x[2], reverse=True)
    sets_count = len(x)
    while sets_count > k:
        src, dst, weight = adj.pop()
        if db.get_parent(src) != db.get_parent(dst):
            db.merge(src, dst)
            sets_count -= 1

    src, dst, weight = adj.pop()
    while db.get_parent(src) == db.get_parent(dst):
        src, dst, weight = adj.pop()

    return weight

def minimum_distance(x, y):
    #write your code here
    adj = []
    for i in range(len(x) - 1):
        for j in range(i, len(x)):
            adj.append((i, j, distance(x[i], y[i], x[j], y[j])))

    db = Database(len(x))

    adj = sorted(adj, key=lambda x: x[2], reverse=True)
    sets_count = len(x)
    result = 0.
    while sets_count > 1:
        src, dst, weight = adj.pop()
        if db.get_parent(src) != db.get_parent(dst):
            db.merge(src, dst)
            sets_count -= 1
            result += weight

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
