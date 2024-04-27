import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        if isinstance(k, int):
            if not 0 <= k < self._n:
                raise IndexError('invalid index')
            return self._A[k]
        elif isinstance(k, slice):
            # Handle slice case
            start, stop, step = k.indices(self._n)  # Calculate actual indices from slice
            return [self._A[i] for i in range(start, stop, step)]  # Create a list from slice
        else:
            raise TypeError('Invalid argument type.')

    def __setitem__(self, k, value):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        self._A[k] = value

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def pop(self):
        if self._n == 0:
            raise IndexError("pop from empty DynamicArray")
        value = self._A[self._n - 1]
        self._A[self._n - 1] = None  # Optionally set the last element to None
        self._n -= 1
        return value

    def remove(self, obj):
        for i in range(self._n):
            if self._A[i] == obj:
                for j in range(i, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return True
        return False

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def index(self, value):
        for i in range(self._n):
            if self._A[i] == value:
                return i
        raise ValueError(f"{value} is not in array")

    def reverse(self):
        start, end = 0, self._n - 1
        while start < end:
            self._A[start], self._A[end] = self._A[end], self._A[start]
            start, end = start + 1, end - 1
