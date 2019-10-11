# python3
from itertools import combinations
from sys import stdin


# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def scalar_product(x, y):
    sum_ = 0
    for i in range(len(x)):
        sum_ += x[i] * y[i]
    return sum_

def printEquisatisfiableSatFormula(A, b, m):
    clauses = []
    for i in range(len(A)):
        non_zero = []
        for j in range(len(A[i])):
            if A[i][j] != 0:
                non_zero.append(j)

        for j in range(len(non_zero)):
            if scalar_product([0] * m, A[i]) > b[i]:
                clauses.append([l + 1  for l in non_zero])

            for combination in combinations(non_zero, j + 1):
                solution = [0] * m
                for l in combination:
                    solution[l] = 1
                if scalar_product(solution, A[i]) > b[i]:
                    clauses.append([-(l + 1) if l in combination else l + 1 for l in non_zero])

    if len(clauses) == 0:
        clauses = [[1, -1]]

    print(len(clauses), m)
    for cur_clause in clauses:
        print(' '.join(map(str, cur_clause + [0])))

if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for i in range(n):
      A += [list(map(int, stdin.readline().split()))]
    b = list(map(int, stdin.readline().split()))

    printEquisatisfiableSatFormula(A, b, m)
