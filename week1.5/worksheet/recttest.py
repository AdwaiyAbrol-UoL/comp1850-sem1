from rect import Rectangle

x = Rectangle(6,7)
print(x.is_square()) # Should be False
print(x.area()) # Should be 42
print(x.perimeter()) # Should be 26

y = Rectangle(2,2)
print(y.is_square()) # Should be True
print(y.area()) # Should be 4
print(y.perimeter()) # Should be 8