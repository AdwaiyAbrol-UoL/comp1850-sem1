# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        
        # type checking
        if not isinstance(width, int):
            raise TypeError("Width must be an integer.")
        if not isinstance(height, int):
            raise TypeError("Height must be an integer.")
        
        # value checking
        if width <= 0:
            raise ValueError("Width must be greater than 0.")
        if height <= 0:
            raise ValueError("Height must be greater than 0.")
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

    def is_square(self):
        """
        Checks if the rectangle is a sqaure and returns True if it is, False otherwise.
        """
        if self.width == self.height:
            return True
        else: 
            return False
    
    
    def area(self):
        """
        Returns the area of the rectangle. 
        """
        return self.width * self.height

    
    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return ((self.width * 2) + (self.height * 2))
