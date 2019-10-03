#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.order = []

        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def get_order(self, i):
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if (self.left[i] + 1):
            if self.key[i] == self.key[self.left[i]]:
                self.key[self.left[i]] += 1
            self.get_order(self.left[i])
        self.order.append(self.key[i])
        if (self.right[i] + 1):
            self.get_order(self.right[i])

def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if not (tree.n):
        return True
    tree.get_order(0)
    return tree.order == sorted(tree.order)


def main():
    tree = TreeOrders()
    tree.read()
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
