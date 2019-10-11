# python3
from sys import stdin
from itertools import combinations


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def SelectPivotElement(a, step):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(step, step)
    while not a[pivot_element.row][pivot_element.column]:
        pivot_element.row += 1
        if pivot_element.row == len(a):
            pivot_element.row = step
            pivot_element.column += 1
        if pivot_element.column == len(A[0]):
            return Position(-1, -1)
    return pivot_element

def SwapLines(a, b, pivot_element, step):
    a[step], a[pivot_element.row] = a[pivot_element.row], a[step]
    b[step], b[pivot_element.row] = b[pivot_element.row], b[step]
    pivot_element.row = step;

def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    x = a[pivot_element.row][pivot_element.column]
    for i in range(pivot_element.column, len(a[0])):
        a[pivot_element.row][i] /= x
    b[pivot_element.row] /= x

    for i in range(len(a)):
        if i == pivot_element.row:
            continue
        dif = a[i][pivot_element.column]
        for j in range(pivot_element.column, len(a[0])):
            a[i][j] -= dif * a[pivot_element.row][j]
        b[i] -= dif * b[pivot_element.row]

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    for step in range(size):
        pivot_element = SelectPivotElement(a, step)
        if pivot_element.row == -1:
            return b
        SwapLines(a, b, pivot_element, step)
        ProcessPivotElement(a, b, pivot_element)

    return b


def scalar_product(a, b):
    sum_ = 0
    for i in range(len(a)):
        sum_ += a[i] * b[i]

    return sum_


def solve_diet_problem(n, m, A, b, c):
    # Write your code here
    for i in range(m):
        x = [0] * m
        x[i] = -1
        A.append(x)
        b.append(0)

    A.append([1 for _ in range(m)])
    b.append(1e9)
    max_pleasure = 0
    best_solution = [-1] * m
    unlimited_solution = False

    for indexes in combinations(range(len(A)), m):
        equation_a = []
        equation_b = []
        for i in indexes:
            equation_a.append(A[i].copy())
            equation_b.append(b[i])

        solution = SolveEquation(Equation(equation_a, equation_b))
        not_satisfying_solution = False
        for i in range(len(A)):
            if scalar_product(A[i], solution) > b[i] + 1e-3:
                not_satisfying_solution = True
                break
        if not_satisfying_solution:
            continue

        pleasure = scalar_product(solution, c)
        if pleasure > max_pleasure or best_solution[0] == -1:
            max_pleasure = pleasure
            best_solution = solution
            if (len(A) - 1) in indexes:
                unlimited_solution = True
            else:
                unlimited_solution = False

    if best_solution[0] == -1:
        return [-1, best_solution]
    return [int(unlimited_solution), best_solution]


n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, b, c)

if anst == -1:
    print("No solution")
if anst == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
