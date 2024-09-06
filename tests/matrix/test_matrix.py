import pytest
from src.matrix import Matrix

def test_init():
    m = Matrix(2, 3)
    assert m.rows == 2
    assert m.cols == 3
    assert m.data == [[0, 0, 0], [0, 0, 0]]
