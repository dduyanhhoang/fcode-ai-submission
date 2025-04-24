from typing import List


def bubble_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    arr = [9, 3, 7, 4, 69, 420, 42]
    bubble_sort(arr)
    print(arr)  # Output should be [3, 4, 7, 9, 42, 69, 420]
