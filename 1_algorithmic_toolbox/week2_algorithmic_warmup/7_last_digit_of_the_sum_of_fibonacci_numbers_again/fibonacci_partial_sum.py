# Uses python3

def pisano_period(m):
    current = 1
    previous = 1
    period = 1
    while not (current == 1 and previous == 0):
        previous, current = current, (current + previous) % m
        period += 1

    return period

def fibonacci_partial_sum(from_, to):
    period = pisano_period(10)
    from_ %= period
    to %= period
    sum1 = 0
    sum2 = 0
    current = 0
    next = 1

    for i in range(max(from_, to)):
        current, next = next, (current + next) % 10
        if i < from_ - 1:
            sum2 += current
            sum2 %= 10
        if i < to:
            sum1 += current
            sum1 %= 10

    sum1 += 10 - sum2
    sum1 %= 10

    return sum1


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
