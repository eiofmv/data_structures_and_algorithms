# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.in_order = []
        self.pre_order = []
        self.post_order = []
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def orders(self, i):
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.pre_order.append(self.key[i])
        if (self.left[i] + 1):
            self.orders(self.left[i])
        self.in_order.append(self.key[i])
        if (self.right[i] + 1):
            self.orders(self.right[i])
        self.post_order.append(self.key[i])

def main():
    tree = TreeOrders()
    tree.read()
    tree.orders(0)
    print(" ".join(str(x) for x in tree.in_order))
    print(" ".join(str(x) for x in tree.pre_order))
    print(" ".join(str(x) for x in tree.post_order))
    
threading.Thread(target=main).start()
