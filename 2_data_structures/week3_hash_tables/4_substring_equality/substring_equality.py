# python3

from random import randint

class Solver:
    _m = [int(10e9 + 7), int(10e9 + 9)]
    _x = randint(1, int(1e9))
    
    def __init__(self, s):
        self.s = s
        self.h = self.preprocess(s)
        
    def preprocess(self, s):
        h = [0 for _ in range(len(s) + 1)]
        h1 = [0 for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            h[i] = (self._x * h[i-1] + ord(s[i - 1])) % self._m[0]
            h1[i] = (self._x * h1[i-1] + ord(s[i - 1])) % self._m[1]
        return [h, h1]
    
    def get_hash(self, a, l, order):
        return ((self.h[order][a + l] - (self._x ** l) * self.h[order][a])) % self._m[order]
        
    def ask(self, a, b, l):
        if (self.get_hash(a, l, 0) == self.get_hash(b, l, 0) ):
            return (self.get_hash(a, l, 1) == self.get_hash(b, l, 1))
        return False

s = input().rstrip()
q = int(input())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, input().split())
    print("Yes" if solver.ask(a, b, l) else "No")
