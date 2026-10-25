# Week 1.5, Session 1: Task 4
import math

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance_to(self, other_point):
        x_difference = other_point.x - self.x
        y_difference = other_point.y - self.y
        return math.sqrt(x_difference ** 2 + y_difference ** 2)

class Circle:

    def __init__(self, radius, centre=Point(0.0, 0.0)):
        self.radius = radius
        self.centre = centre

    def area(self):
        return round(math.pi * self.radius * 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)
