class DijkstraNode:
    def __init__(self, vertexNumber, distance):
        self.vertexNumber = vertexNumber
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance
