# Uses python3

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while(b > 0):
        a, b = b, a % b

    return a

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
