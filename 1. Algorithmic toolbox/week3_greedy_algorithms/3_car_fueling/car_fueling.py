# python3


def compute_min_refills(distance, tank, stops):
    n = len(stops)
    stops = [0] + stops + [distance]
    n_refills = 0
    current_refill = 0
    while (current_refill <= n):
        last_refill = current_refill
        while (current_refill <= n)and(stops[current_refill + 1] - stops[last_refill] <= tank):
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= n:
            n_refills += 1
        
    # write your code here
    return n_refills

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = [int(i) for i in input().split(' ')]
    print(compute_min_refills(d, m, stops))
