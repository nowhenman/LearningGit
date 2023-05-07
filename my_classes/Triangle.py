import math
# Задание 7.
# Описать класс, представляющий треугольник.
# Предусмотреть методы для создания объектов, вычисления площади, периметра и точки пересечения медиан.
# Описать свойства для получения состояния объекта.


class Triangle:
    """
    Треугольник можно построить по трём сторонам; по стороне и прилежащим углам; по двум сторонам и углу.
    qa = distance from M to side a; qb = distance from M to side b; qc = distance from M to side c.
    """

    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__c = 0
        self.__ang_a = 0
        self.__ang_b = 0
        self.__ang_c = 0
        self.__perimeter = 0
        self.__square = 0
        self.__qa = 0
        self.__qb = 0
        self.__qc = 0

    def __str__(self):
        return f"\nA triangle with sides: {self.__a}, {self.__b} and {self.__c} and angles {self.__ang_a}," \
               f" {self.__ang_b} and {self.__ang_c}. \n" \
               f"The median point is {self.get_med_point()} from sides a, b and c." \
               f"\nIts perimeter is {self.get_per()} " \
               f"and its square is {self.get_square()}."

    def set_all_sides(self, a, b, c):
        self.__c = c
        self.__a = a
        self.__b = b
        self.__ang_a = math.degrees(math.acos((self.__b ** 2 + self.__c ** 2 - self.__a ** 2) / (2 * self.__b * self.__c)))
        self.__ang_b = math.degrees(math.acos((self.__a ** 2 + self.__c ** 2 - self.__b ** 2) / (2 * self.__a * self.__c)))
        self.__ang_c = 180 - (self.__ang_a + self.__ang_b)

    def set_two_angles(self, c, ang_a, ang_b):
        self.__c = c
        self.__ang_a = ang_a
        self.__ang_b = ang_b
        self.__ang_c = 180 - (self.__ang_b + self.__ang_a)
        self.__a = self.__c * (math.sin(math.radians(self.__ang_a)) / math.sin(math.radians(self.__ang_c)))
        self.__b = self.__c * (math.sin(math.radians(self.__ang_b)) / math.sin(math.radians(self.__ang_c)))

    def set_two_sides(self, b, a, ang_c):
        self.__b = b
        self.__a = a
        self.__ang_c = ang_c
        self.__c = (self.__a ** 2 + self.__b ** 2 - (2 * self.__a * self.__b * math.cos(math.radians(self.__ang_c)))) ** 0.5
        self.__ang_a = math.degrees(math.acos((self.__b ** 2 + self.__c ** 2 - self.__a ** 2) / (2 * self.__b * self.__c)))
        self.__ang_b = 180 - (self.__ang_c + self.__ang_a)

    def get_per(self):
        self.__perimeter = self.__c + self.__a + self.__b
        return self.__perimeter

    def get_square(self):
        self.__square = 0.5 * (self.__a * self.__b * math.sin(math.radians(self.__ang_c)))
        return self.__square

    def get_med_point(self):
        self.__qa = (self.get_square() * 2 / 3 / self.__a)
        self.__qb = (self.get_square() * 2 / 3 / self.__b)
        self.__qc = (self.get_square() * 2 / 3 / self.__c)
        return [self.__qa, self.__qb, self.__qc]
