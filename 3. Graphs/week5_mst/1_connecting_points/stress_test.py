#Uses python3
from connecting_points import minimum_distance as minimum_distance_v1
from connecting_points_v2 import minimum_distance as minimum_distance_v2
from random import randint

c = 1
while 1:
    n = randint(0, 200)
    x = []
    y = []
    for _ in range(n):
        x.append(randint(-1000, 1000))
        y.append(randint(-1000, 1000))

    assert minimum_distance_v1(x, y) - minimum_distance_v2(x, y) <= 1e-6
    print('ok')

