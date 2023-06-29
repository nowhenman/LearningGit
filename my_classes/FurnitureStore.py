"""
Задание 3.
Интернет-магазин продает двери, окна, обои и полы. Продумать характеристики товаров.
Создать необходимые классы с полями и методами. Продемонстрировать работу классов на нескольких примерах.
"""

import itertools


class Item:

    counter = itertools.count(1)

    def __init__(self, make, model, price):
        self.__id = next(Item.counter)
        self.__make = make
        self.__model = model
        self.__price = float(price)

    def get_id(self):
        return self.__id

    @property
    def price(self):
        return self.__price


class Door(Item):
    def __init__(self,  make, model, price, height, width, material, finish, use):
        super().__init__(make, model, price)
        self.__height = float(height)
        self.__width = float(width)
        self.__material = material
        self.__finish = finish
        self.__use = use


class Window(Item):
    def __init__(self, make, model, width, height, panes, material, layers, price):
        super().__init__(make, model, price)
        self.__width = float(width)
        self.__height = float(height)
        self.__panes = int(panes)
        self.__material = material
        self.__layers = int(layers)


class Wallpaper(Item):
    def __init__(self, make, model, width, length, material, design, price):
        Item.__init__(self, make, model, price)
        self.__width = float(width)
        self.__length = float(length)
        self.__material = material
        self.__design = design


class Floor(Item):
    def __init__(self, make, model, material, d_type, width, length, price):
        super().__init__(make, model, price)
        self.__width = float(width)
        self.__length = float(length)
        self.__material = material
        self.__d_type = d_type
