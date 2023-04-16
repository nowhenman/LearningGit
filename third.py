import math


class Circle:
    def __init__(self, rad):
        self.radius = rad

    def square_is(self):
        square = math.pi * (self.radius ** 2)
        return square


a = Circle(9)
print(id(Circle))
Circle.j = 5
print(id(a))
print(id(Circle))


B = Circle
print(id(B))
a = B(3)
Circle = 5
