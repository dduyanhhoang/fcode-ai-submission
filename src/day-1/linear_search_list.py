from typing import List


def linear_search(haystack: List[int], needle: int) -> bool:
    if not isinstance(needle, int):
        raise ValueError("needle must be an int")

    if not isinstance(haystack, List):
        raise ValueError("haystack is not a List")

    for i in haystack:
        if isinstance(i, int):
            raise ValueError("haystack must have only ints")

    for i in haystack:
        if i == needle:
            return True

    return False
