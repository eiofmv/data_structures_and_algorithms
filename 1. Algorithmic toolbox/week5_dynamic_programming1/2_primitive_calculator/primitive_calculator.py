# Uses python3

def optimal_sequence(n):
    a = [0] * (n + 1)
    i = 2
    while i <= n:
        a[i] = a[i-1] + 1
        if i % 3 == 0:
            a[i] = min(a[i], a[i // 3] + 1) 
        if i % 2 == 0:
            a[i] = min(a[i], a[i // 2] + 1)
        i += 1
 
    sequence = []
    while n >= 1:
        sequence.append(n)
        if (n % 3 == 0)and(a[n] - a[n // 3] == 1):
            n = n // 3
        elif (n % 2 == 0)and(a[n] - a[n // 2] == 1):
            n = n // 2
        else:
            n -= 1
    return reversed(sequence)

n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
