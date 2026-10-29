# Week 1.5, Session 2: Task 4

from geometry import Point, Circle

centre = Point(0, 0)
circle = Circle(5, centre)

inside_point = Point(2, 3)
outside_point = Point(6, 0)

print(inside_point in circle)
print(outside_point in circle)
