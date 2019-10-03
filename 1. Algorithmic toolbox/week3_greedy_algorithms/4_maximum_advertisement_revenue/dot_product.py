#Uses python3

def max_dot_product(a, b):
    #write your code here
    res = 0
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    for i in range(len(a_sorted)):
        res += a_sorted[i] * b_sorted[i]
    return res

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    print(max_dot_product(a, b))
    
