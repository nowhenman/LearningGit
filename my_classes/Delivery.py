"""
Класс Delivery, содержащий следующие закрытые атрибуты:
ref - Артикул
name - Наименование товара
amount - Количество товара
date - Дата поставки
"""


class Delivery:
    def __init__(self, ref, name, amount, date):
        self.__ref = ref
        self.__name = name
        self.__amount = amount
        self.__date = date

    def check_dest(self):
        if self.__amount < 1:
            print("\nКоличество товара = 0", end=', ')
            self.__del__()

    def __del__(self):
        print(f"Доставка {self.__name} от {self.__date } удалена")

    def get_ref(self):
        return self.__ref

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def get_date(self):
        return self.__date

    def set_amount(self, amount):
        self.__amount = amount
        self.check_dest()
