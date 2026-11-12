# Week 1.6, Session 1: Task 3

from point import Point
from shapes import Circle

circle = Circle(2.5, Point(0.0, 0.0), "red")
print(circle)
print(f"Area = {circle.area():.3f}")
print(f"Perimeter = {circle.perimeter():.3f}")
print("Moving the circle...")
circle.set_position(Point(1.6, 3.2))
print(circle)
print("Changing the circle's colour...")
circle.set_colour("green")
print(circle)
