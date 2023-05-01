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

# 0 1 2 3


def bin_search(massiv, num):
    a, b = 0, (len(massiv)-1)
    ind = (a + b) // 2
    if massiv[ind] == num:
        return ind
    elif massiv[ind] > num:
        b = ind
        return bin_search(massiv[a:b], num)
    elif massiv[ind] < num:
        a = ind
        return bin_search(massiv[a:b+1], num)


orig = [1, 500, -9, 0, 55, 71]
orig.sort()

# ab = list(map(int, input("Введите список чисел: ").split()))
needed = int(input("искомое число: "))
print(bin_search(orig, needed))

# от 0 до n-1 только перестраивать диапазон индексов, а не трогать!
# попробуй на листе бумаги!
# тащить границы диапазона в котором (переобозначать не массив, а его индексы!)
