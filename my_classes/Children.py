"""
класс Children, который содержит такие поля (члены класса): закрытые – имя ребенка, фамилию, возраст,
публичные – методы ввода данных (геттеры и сеттеры) и отображения их на экран.
"""


class Children:
    """Comment"""
    count = 0

    def __init__(self):  # todo подумать, почему в конструкторе все поля
        self.__age = None
        self.__lname = None
        self.__fname = None
        Children.count += 1
        self.__id = Children.count

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

    def get_id(self):
        return self.__id


ch1 = Children()
ch1.set_fname('Test')
ch2 = Children()
ch2.set_fname('Test')
print(ch1.get_fname())
print(Children.count)
print(ch1.get_id())
print(ch2.get_id())
print(getattr(ch1, "weight", 0))
delattr(ch1, "__age")
print(ch1.get_age())
