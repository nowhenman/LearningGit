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


def bin_search(massiv, num):
    massiv.sort()
    ind = len(massiv)//2
    x = massiv[ind]
    if x == num:
        return ind
    elif x > num:
        massiv = massiv[:ind]
        return bin_search(massiv, num)
    elif x < num:
        massiv = massiv[ind:]
        return bin_search(massiv, num)
    return -1


ab = list(map(int, input("Введите список чисел: ").split()))
needed = int(input("искомое число: "))
print(bin_search(ab, needed))

# от 0 до n-1 только перестраивать диапазон индексов, а не трогать!
# попробуй на листе бумаги!
# тащить границы диапазона в котором (переобозначать не массив, а его индексы!)
