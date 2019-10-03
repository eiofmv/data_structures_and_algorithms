# python3
import sys

def BWT(text):
    array = []
    for i in range(len(text)):
        array.append(text[i:] + text[:i])

    array = sorted(array)
    array = list(map(lambda x: x[-1], array))
    return ''.join(array)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))