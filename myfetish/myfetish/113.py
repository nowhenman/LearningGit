from math import pi

class Shape:

    def calculate_area(self):
        return 0  # so you won't forget

    def calculate_perim(self):
        return 0  # so you won't forget


class Circle(Shape):
    def __init__(self, r):
        self.__r = r

    def calculate_area(self):
        return pi * self.__r ** 2

    def calculate_perim(self):
        return 2 * pi * self.__r


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a, self.__side_b, self.__side_c = side_a, side_b, side_c

    def calculate_perim(self):
        return self.__side_a + self.__side_b + self.__side_c

    def calculate_area(self):
        p = self.calculate_perim() / 2
        return (p*(p-self.__side_a)*(p-self.__side_b)*(p-self.__side_c)) ** 0.5


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def calculate_area(self):
        return self.__side ** 2

    def calculate_perim(self):
        return self.__side * 4


def show_obj(shape_list):
    for elem in shape_list:
        print(elem.calculate_area(), elem.calculate_perim())


my_triangle = Triangle(3, 4, 5)
my_circle = Circle(50)
my_square = Square(pi)
my_list = []
my_list.append(my_triangle)
my_list.extend([my_circle, my_square])

show_obj(my_list)
