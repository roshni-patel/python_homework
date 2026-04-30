import math

"""
Task 5: Extending a Class
    Within the assignment3 folder, create a file called extend-point-to-vector.py.
    Create a class called Point. It represents a point in 2d space, with x and y values passed to the __init__() method. It should include methods for equality, string representation, and Euclidian distance to another point.
    Create a class called Vector which is a subclass of Point and uses the same __init__() method. Add a method in the vector class which overrides the string representation so Vectors print differently than Points. Override the + operator so that it implements vector addition, summing the x and y values and returning a new Vector.
    Print results which demonstrate all of the classes and methods which have been implemented.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Equality check
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    # String representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Euclidean distance to another point
    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("Distance can only be calculated between Points")
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    # Inherits __init__ from Point

    # Override string representation
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    # Override + operator for vector addition
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add another Vector")
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)

    print(p1)  
    print(p2) 

    print(p1 == Point(1, 2))  # True
    print(p1 == p2)  # False

    print("Distance:", p1.distance_to(p2))  # 5.0

    # Create Vectors
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)

    print(v1)  
    print(v2) 

    # Vector addition
    v3 = v1 + v2
    print("v1 + v2 =", v3)  # Vector<6, 8>