# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def tree_walk(children, i):
    if len(children[i]) == 0:
        return 1
    max_ = 0
    for p in children[i]:
        max_ = max(max_, 1 + tree_walk(children, p))
    return max_

class TreeHeight:
        def read(self):
            self.n = int(int(input()))
            parent = list(map(int, input().split()))
            self.children = [[] for _ in range(len(parent))]
            for i, p in enumerate(parent):
                if p == -1:
                    self.root = i
                else:
                    self.children[p].append(i)

        def compute_height(self):
                # Replace this code with a faster implementation
                #maxHeight = 0
                #for vertex in range(self.n):
                #        height = 0
                #        i = vertex
                #        while i != -1:
                #                height += 1
                #                i = self.parent[i]
                #        maxHeight = max(maxHeight, height);
                return tree_walk(self.children, self.root);

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
