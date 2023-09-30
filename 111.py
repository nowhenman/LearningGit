import math


class Circle:

    def __init__(self, r):
        self.__r = r

    def area(self):
        return math.pi * (self.__r ** 2)

    def perim(self):
        return 2 * math.pi * self.__r


new_c = Circle(5)
print(new_c.area(), new_c.perim())