# python3
from itertools import combinations
import os


# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula(n, edges):
    clauses = []
    for i in range(n):
        clauses.append([n * i + l + 1 for l in range(n)])
        clauses.append([n * l + i + 1 for l in range(n)])
        for pair in combinations(range(n), 2):
            clauses.append([-(n * i + l + 1) for l in pair])
            clauses.append([-(n * l + i + 1) for l in pair])

    for v1, v2 in combinations(range(n), 2):
        if (v1 + 1, v2 + 1) in edges or (v2 + 1, v1 + 1) in edges:
            continue
        for i in range(n-1):
            clauses.append([-(n * v1 + i + 1), -(n * v2 + i + 2)])
            clauses.append([-(n * v2 + i + 1), -(n * v1 + i + 2)])

    print(len(clauses), n * n)
    for clause in clauses:
        print(' '.join(map(str, clause + [0])))



if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = set(tuple(map(int, input().split())) for i in range(m))
    printEquisatisfiableSatFormula(n, edges)