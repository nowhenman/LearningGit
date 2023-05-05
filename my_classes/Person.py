import datetime

# Задание 8.
# Создайте класс Персона с методами, позволяющими вывести на экран информацию о персоне, а также определить
# ее возраст (в текущем году). Создайте список из n персон, выведите полную информацию из базы на экран, а также
# организуйте поиск персон, чей возраст попадает в заданный диапазон.
# При этом n, данные о персонах и диапазон вводятся с клавиатуры.
# Доп. задание: Сделать проверку на корректность введенных данных.
"""
Date_of_birth should be provided in yyyymmdd format only!
"""

months = {
        1: "January", 2: "February", 3: "March",
        4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September",
        10: "October", 11: "November", 12: "December"
}


class Person:
    def __init__(self, fname, lname, date_of_birth):
        self.__fname = fname
        self.__lname = lname
        self.__date_of_birth_t = date_of_birth
        self.__day_birth = int(date_of_birth[-2:])
        self.__month_birth = int(date_of_birth[4:-2])
        self.__year_birth = int(date_of_birth[:4])

    __mname = 'None'

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_mname(self):
        if self.__mname != 'None':
            return self.__mname
        else:
            return "This person doesn't have a middle name"

    def get_birthday(self):
        return f"{self.__day_birth} of {months[self.__month_birth]}, {self.__year_birth}"

    def get_birthday_t(self):
        return self.__date_of_birth_t

    def get_age(self):
        person_birth_date = datetime.date(self.__year_birth, self.__month_birth, self.__day_birth)  # Example birth date
        person_age = (datetime.date.today() - person_birth_date).days
        person_years = person_age // 365
        person_days = person_age % 365
        return f"{person_years} years and {person_days} days"

    def set_fname(self, name):
        self.__fname = name

    def set_lname(self, name):
        self.__lname = name

    def set_mname(self, name):
        self.__mname = name

    def set_dob(self, date_of_birth):
        self.__date_of_birth_t = date_of_birth
