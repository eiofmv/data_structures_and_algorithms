#Uses python3

def is_greater(a, b):
    return int(a + b) > int(b + a)

def largest_number(digits):
    #write your code here
    res = ""
    while (len(digits) != 0):
        max_ = '0'
        for i in range(len(digits)):
            if is_greater(digits[i], max_):
                max_ = digits[i]
                max_index = i
        res += digits.pop(max_index)
    return res

if __name__ == '__main__':
    n = int(input())
    data = [i for i in input().split()]
    print(largest_number(data))
    
