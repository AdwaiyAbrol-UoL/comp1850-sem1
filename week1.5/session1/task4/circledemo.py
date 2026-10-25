# Week 1.5, Session 1: Task 4

from geometry import Point, Circle

x_coordinate = float(input("Enter the centre x coordinate: "))
y_coordinate = float(input("Enter the centre y coordinate: "))
radius = float(input("Enter the circle radius: "))

centre = Point(x_coordinate, y_coordinate)
circle = Circle(radius, centre)

print("Area:", format(circle.area(), ".4f"))
print("Perimeter:", format(circle.perimeter(),".4f"))
