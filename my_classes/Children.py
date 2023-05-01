"""
класс Children, который содержит такие поля (члены класса): закрытые – имя ребенка, фамилию, возраст,
публичные – методы ввода данных (геттеры и сеттеры) и отображения их на экран.
"""


class Children:
    __fname = ''
    __lname = ''
    __age = 0

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
