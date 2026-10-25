# Week 1.5, Session 1: Task 3
import math 

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    # Add distance() method here
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other_point):
        dx = other_point.x - self.x
        dy = other_point.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)



# Finally, add code here to demonstrate use of Point
p1 = Point(6, 7)
print("p1.x =", p1.x)
print("p1.y =", p1.y)
print("Distance from origin =", round(p1.distance(), 1))
p2 = Point(2, -1)
print("Distance from p1 to p2 =", round(p1.distance_to(p2), 1))