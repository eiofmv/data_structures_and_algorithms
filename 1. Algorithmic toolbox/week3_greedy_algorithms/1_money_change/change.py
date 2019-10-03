# Uses python3

def get_change(m):
    coins = 0
    for i in [10, 5, 1]:
        coins += m // i
        m %= i
    #write your code here
    return coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
