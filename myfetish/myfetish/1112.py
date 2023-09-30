import datetime


# Write a Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.

class Person:
    def __init__(self, name, country, birthday):
        self.__name = name
        self.__country = country
        self.__birthday = datetime.date.fromisoformat(birthday)

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.__birthday.year
        if self.__birthday.month > today.month or self.__birthday.month == today.month \
                and self.__birthday.day > today.day:
            age -= 1
        return age


new_per = Person("John", "UK", "1997-08-27")
print(new_per.calculate_age())
