import numpy as np


class Point:
    """
    A "Point" in 2D Space. Helper class for Node.
    """

    def __init__(self, point: tuple):
        self.x = point[0]
        self.y = point[1]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def asnumpy(self):
        """Returns a numpy array representing the point. First element is x, second is y."""
        return np.array([self.x, self.y])
    
    def astuple(self):
        """Returns a tuple representing the point. First element is x, second is y."""
        return (self.x, self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Node:
    """
    A singular node of a graph system. Contains a Point and a "cost" of construction. 
    Used for "p-median" problem.
    """

    __identifier = 0

    def __init__(self, point: Point, cost):
        self.point = point
        self.cost = cost

        Node.__identifier += 1
        self.id = Node.__identifier

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f"Node({self.point}, id={self.id})"

