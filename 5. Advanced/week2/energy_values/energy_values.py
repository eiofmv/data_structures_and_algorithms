# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, step):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(step, step)
    while not a[pivot_element.row][pivot_element.column]:
        pivot_element.row += 1
    return pivot_element

def SwapLines(a, b, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    pivot_element.row = pivot_element.column;

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

# def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
#     used_rows[pivot_element.row] = True
#     used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    # used_columns = [False] * size
    # used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, step)
        SwapLines(a, b, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        # MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b


def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])


if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
