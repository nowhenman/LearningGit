"""
класс Children, который содержит такие поля (члены класса): закрытые – имя ребенка, фамилию, возраст,
публичные – методы ввода данных (геттеры и сеттеры) и отображения их на экран.
"""


class Children:
    age = 0

    def __init__(self):  # todo подумать, почему в конструкторе все поля
        self.__age = None
        self.__lname = None
        self.__fname = None

    def set_fname(self, fname):
        self.__fname = fname

    def set_lname(self, lname):
        self.__lname = lname

    def set_age(self, age):
        self.__age = age

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_age(self):
        return self.__age


ch1 = Children()
ch1.set_fname('Test')
print(ch1.get_fname())
print(Children.age)
