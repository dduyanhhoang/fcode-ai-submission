import random

from two_crystal_balls import two_crystal_balls


def test_two_crystal_balls():
    idx = random.randint(0, 9999)
    data = [False] * 10000

    for i in range(idx, 10000):
        data[i] = True

    assert two_crystal_balls(data) == idx
    assert two_crystal_balls([False] * 821) == -1
