# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    Qi = deque()
    for i in range(m):
        while Qi and sequence[i] >= sequence[Qi[-1]] : 
            Qi.pop()
        Qi.append(i)
    
    for i in range(m, len(sequence)):
        maximums.append(sequence[Qi[0]])
        while Qi and Qi[0] <= i-m:
            Qi.popleft()
            
        while Qi and sequence[i] >= sequence[Qi[-1]] : 
            Qi.pop()

        Qi.append(i)
    return maximums + [sequence[Qi.popleft()]]

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(" ".join(map(str, max_sliding_window_naive(input_sequence, window_size))))
