# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    previous = 0
    current  = 1

    for _ in range(n):
        previous, current = current, (previous + current) % 10

    return previous

if __name__ == '__main__':
    print(get_fibonacci_last_digit_naive(int(input())))
