import math
class Circle:
    def __init__(self, rad):
        self.radius = rad
    def square_is(self):
        square = math.pi * (self.radius ** 2)
        return square

a = Circle(9)
Circle.j = 5
print(dir(Circle))

B = Circle
a = B(3)
Circle = 5
