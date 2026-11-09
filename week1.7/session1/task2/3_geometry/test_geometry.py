# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

import math
from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance_to(p2) == 5.0

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates

def test_circle_constructor():
    circle = Circle(2)
    assert circle.radius == 2
    assert circle.centre.x == 0.0
    assert circle.centre.y == 0.0

def test_circle_area():
    assert Circle(2).area() == 4 * math.pi

def test_circle_perimeter():
    assert Circle(2).perimeter() == 4 * math.pi
