# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a point using its x and y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate

    def distance(self):
        """
        Returns the distance from this point to the origin.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance_to(self, other_point):
        """
        Returns the distance from this point to another point.
        """
        x_difference = other_point.x - self.x
        y_difference = other_point.y - self.y
        return math.sqrt(x_difference ** 2 + y_difference ** 2)


class Circle:
    """
    A circle with a radius and a centre point.
    """

    def __init__(self, radius, centre=None):
        """
        Creates a circle with a radius and a centre point.
        """
        self.radius = radius
        if centre is None:
            centre = Point(0.0, 0.0)
        self.centre = centre

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius
