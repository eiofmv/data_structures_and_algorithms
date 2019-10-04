# Uses python3

def pisano_period(m):
    current = 1
    previous = 1
    period = 1
    while not (current == 1 and previous == 0):
        previous, current = current, (current + previous) % m
        period += 1

    return period

def fibonacci_sum_squares(n):
    period = pisano_period(10)
    sum_ = 0
    current = 0
    next = 1

    for i in range(n % period):
        current, next = next, (current + next) % 10
        sum_ += current * current
        sum_ %= 10

    return sum_

if __name__ == '__main__':
    print(fibonacci_sum_squares(int(input())))
