# python3
from itertools import combinations

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula(n, m, edges):
    clauses = []
    for i in range(n):
        clauses.append([3 * i + l + 1 for l in range(3)])
        for pair in combinations(range(3), 2):
            clauses.append([-(3 * i + l + 1) for l in pair])
    for i in range(m):
        v1, v2 = edges[i]
        for j in range(3):
            clauses.append([-(3 * (v1 - 1) + j + 1),
                            -(3 * (v2 - 1) + j + 1)])

    print(len(clauses), 3 * n)
    for claus in clauses:
        print(' '.join(map(str, claus + [0])))


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    printEquisatisfiableSatFormula(n, m, edges)
