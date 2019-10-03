#Uses python3
import random

with open('my_test.txt', 'w') as f:
    f.write(str(200) + '\n')
    points = set()
    for i in range(200):
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        if (x, y) not in points:
            points.add((x, y))
            f.write(' '.join(map(str, [x, y])) + '\n')

    f.write(str(2))





