import numpy as np

class Point:
    """
    A "Point" in 2D Space. Helper class for Node.
    """

    def __init__(self, point: tuple[int, int]):
        """
        Creates a new "Point" class object.

        @arguments
        point: tuple - a two-tuple consisting of two integers representing the point.
        """

        self.x: int = point[0]
        self.y: int = point[1]

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def asnumpy(self) -> np.ndarray:
        """Returns a numpy array representing the point. First element is x, second is y."""
        return np.array([self.x, self.y])

    def astuple(self) -> tuple[int, int]:
        """Returns a tuple representing the point. First element is x, second is y."""
        return (self.x, self.y)

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Node:
    """
    A singular node of a graph system. Contains a Point and a "cost" of construction.
    Used for "p-median" problem.
    """

    __identifier = 0

    def __init__(self, point: Point, cost: float):
        """
        Creates a new "Node" class object.

        @arguments
        point: Point - a point representation (location of the "Node")
        cost: cost of constructing at the node.
        """
        self.point: Point = point
        self.cost: float = cost

        Node.__identifier += 1
        self.id = Node.__identifier

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __repr__(self) -> str:
        return f"Node({self.point}, cost={self.cost})"
