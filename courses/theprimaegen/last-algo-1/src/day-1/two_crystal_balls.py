import math
from math import floor
from typing import List


def two_crystal_balls(breaks: List[bool]) -> int:
    jmp_amount = floor(math.sqrt(len(breaks)))

    i = jmp_amount

    for i in range(0, len(breaks), jmp_amount):
        if breaks[i]:
            break

    i -= jmp_amount

    for j in range(i, i + jmp_amount):
        if breaks[j]:
            return j

    return -1
