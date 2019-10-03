# python3
import sys

def InverseBWT(bwt):
    # write your code here
    last = list(zip(bwt, range(len(bwt))))
    first = sorted(last, key=lambda x: x[0])
    s = ''
    prev = first[0][1]
    for i in range(len(bwt)):
        s += first[prev][0]
        prev = first[prev][1]
    return s


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))