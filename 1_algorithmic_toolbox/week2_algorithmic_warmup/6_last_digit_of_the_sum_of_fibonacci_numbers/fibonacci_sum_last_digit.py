# Uses python3

def pisano_period(m):
    current = 1
    previous = 1
    period = 1
    while not (current == 1 and previous == 0):
        previous, current = current, (current + previous) % m
        period += 1

    return period

def fibonacci_sum(n):
    period = pisano_period(10)

    previous = 0
    current  = 1
    sum = 0

    for _ in range(n % period):
        previous, current = current, (previous + current) % 10
        sum += previous
        sum %= 10

    return sum

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
