# Week 1.5, Session 2: Task 1

# Add type checking to the constructor of Point

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x: int | float, y: int | float) -> None:
        """
        Creates a Point, given x & y coordinates.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be an integer or float")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be an integer or float")
        self.x = x
        self.y = y

    def distance(self) -> float:
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p: "Point") -> float:
        """
        Returns distance of this Point from the specified Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)


# Test program

p = Point("2", 1)
print(p.distance())
