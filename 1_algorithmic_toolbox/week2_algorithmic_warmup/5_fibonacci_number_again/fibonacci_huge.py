# Uses python3

def pisano_period(m):
    current = 1
    previous = 1
    period = 1
    while not (current == 1 and previous == 0):
        previous, current = current, (current + previous) % m
        period += 1

    return period

def get_fibonacci_huge(n, m):
    period = pisano_period(m)

    previous = 0
    current  = 1

    for _ in range(n % period):
        previous, current = current, (previous + current) % m

    return previous 

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
