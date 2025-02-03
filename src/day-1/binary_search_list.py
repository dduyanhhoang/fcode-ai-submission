from math import floor
from typing import List


def binary_search(haystack: List[int], needle: int) -> bool:
    if not isinstance(needle, int):
        raise ValueError("needle must be an int")

    if not isinstance(haystack, List):
        raise ValueError("haystack is not a List")

    for i in haystack:
        if not isinstance(i, int):
            raise ValueError("haystack must have only ints")

    lo = 0
    hi = len(haystack)

    while lo < hi:
        m = floor(lo + (hi - lo) / 2)
        v = haystack[m]

        if v == needle:
            return True
        elif v > needle:
            hi = m
        else:
            lo = m + 1

    return False
