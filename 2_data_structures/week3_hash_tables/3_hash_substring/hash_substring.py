# python3
from random import randint

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))
    
def are_equal(a, b):
    return a == b

def mod(a, p):
    return ((a % p) + p) % p

def precompute_hashes(T, len_P, p, x):
    H = [0 for i in range(len(T) - len_P + 1)]
    S = T[-len_P:]
    H[len(T) - len_P] = poly_hash(S, p, x)
    y = 1
    for i in range(len_P):
        y = (y * x) % p
    for i in range(len(T) - len_P)[::-1]:
        H[i] = mod((x * H[i+1] + ord(T[i]) - y * ord(T[i + len_P])), p)
    return H
    
def poly_hash(S, p, x):
    hash_ = 0
    for i in range(len(S))[::-1]:
        hash_ = mod((hash_ * x + ord(S[i])), p)
    return hash_
    
def rabin_karp(P, T):
    result = []
    p = 1125899839733759
    x = randint(1, len(P))
    p_hash = poly_hash(P, p, x)
    H = precompute_hashes(T, len(P), p, x)
    t_hash = poly_hash(T[:len(P)], p, x)
    for i in range(len(T) - len(P) + 1):
        if p_hash != H[i]:
            continue
        if are_equal(T[i:i+len(P)], P):
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))
