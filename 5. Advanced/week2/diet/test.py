# python3
import os

str1 = 'python diet.py < ./tests/'
str2 = 'cat ./tests/'

for i in os.listdir('./tests'):
    if not i.endswith('.a'):
        print('\nTest case {}: '.format(i))
        os.system(str1 + i)
        print('Ans:')
        os.system(str2 + i + '.a')



