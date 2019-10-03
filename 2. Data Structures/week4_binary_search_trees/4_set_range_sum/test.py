import os

i = input().rstrip()

with open('tests/{}.a'.format(i), 'r') as f:
    correct = f.read()

os.system('cat tests/%s | python set_range_sum.py > ans' % i)

with open('ans', 'r')as f:
    answer = f.read()

print(correct == answer)
