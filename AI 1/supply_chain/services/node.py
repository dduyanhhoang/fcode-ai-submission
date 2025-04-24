from ..data_structures.darray import DynamicArray
from .pair import Pair

class Node:
    def __init__(self, vertexNumber):
        self.vertexNumber = vertexNumber
        self.children = DynamicArray()

    def Add_child(self, vNumber, length):
        p = Pair(vNumber, length)
        self.children.append(p)
