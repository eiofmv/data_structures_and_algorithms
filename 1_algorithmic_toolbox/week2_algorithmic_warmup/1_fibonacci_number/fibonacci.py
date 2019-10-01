# Uses python3

def fib(n):
    f1, f0 = 1, 0
    for i in range(n):
        f1, f0 = f1 + f0, f1
    return f0

print(fib(int(input())))
