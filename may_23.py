# Задание 0 на слайде 12 -- работает
# Создать класс Delivery, содержащий следующие закрытые атрибуты:
# - Артикул
# - Наименование товара
# - Количество товара
# - Дата поставки

# Создать новый объект класса Delivery.
# Организовать поставку товара 456123 «Дисплей ЖК N192» в количестве 11 штук 13 сентября 2019 года.
# Организовать поставку товара 456124 «Мышь беспроводная N435» в количестве 9 штук 14 сентября 2019 года.
# Списать два дисплея.
# Списать одну мышь.
# Списать девять дисплеев.
# Если количество какого-либо из товаров становится менее 1, то он удаляется из памяти.

# Доп.материал: https://www.tutorialsteacher.com/python/public-private-protected-modifiers

from my_classes.Delivery import Delivery

delivery_1 = Delivery(456123, "Дисплей ЖК N192", 11, "2019.09.13")
delivery_2 = Delivery(456124, "Мышь беспроводная N435", 9, "2019.09.14")

delivery_1.set_amount(delivery_1.get_amount() - 2)
delivery_2.set_amount(delivery_2.get_amount() - 1)
delivery_1.set_amount(delivery_1.get_amount() - 9)

print("\n==========End of program==========\n")


# Задание 1 -- сделал
# Создайте класс с методом класса, в котором определялась бы сумма двух целых чисел.

from my_classes.IntegerAdd import IntegerAdd

# Задание 2 -- сделали вместе
# Доработать класс методом-конструктором, в котором следует определить атрибуты экземпляра класса,
# необходимые для сложения двух целых чисел.
# Напишите метод, в котором бы определялась сумма двух целых чисел, переданных через конструктор.

# Задание 3 -- PROBLEM
# Создайте класс с методами, формирующими вложенную последовательность.  # список внутри списка
# Пользователю должна быть предоставлена возможность заполнить ее либо
# случайными числами в интервале [-10; 10], либо осуществить ввод данных с клавиатуры.

# Задание 4 -- сделал
# Определить класс Children, который содержит такие поля (члены класса): закрытые – имя ребенка, фамилию и возраст,
# публичные – методы ввода данных (геттеры и сеттеры) и отображения их на экран.
# Создать массив данных и добавить в него двух детей.
# Определить класс Parent, который содержит такие поля (члены класса): закрытые – имя родителя, фамилию, возраст,
# публичные – методы ввода данных (геттеры и сеттеры) и отображения их на экран.
# Объявить два объекта класса, внести данные и показать их.

from my_classes.Children import Children
from my_classes.Parent import Parent

kid_1 = Children()
kid_2 = Children()
kids = [kid_1, kid_2]

parent_1 = Parent()
parent_1.set_fname('John')
parent_1.set_lname("Doe")
parent_1.set_age(32)

print(parent_1.get_fname(), parent_1.get_lname(), parent_1.get_age())

parent_2 = Parent()
parent_2.set_fname('Jane')
parent_2.set_lname('Doe')
parent_2.set_age(30)

print(parent_2.get_fname(), parent_2.get_lname(), parent_2.get_age())

# Задание 5.
# Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
# Добавить функцию, которая находит сумму значений этих переменных, и функцию
# которая находит наибольшее значение из этих двух переменных.

# Задание 6.
# Создать класс с двумя переменными. Добавить конструктор с входными параметрами.
# Добавить конструктор, инициализирующий члены класса по умолчанию.
# Добавить деструктор, выводящий на экран сообщение об удалении объекта.

# Задание 7.
# Описать класс, представляющий треугольник.
# Предусмотреть методы для создания объектов, вычисления площади, периметра и точки пересечения медиан.
# Описать свойства для получения состояния объекта.

# Задание 8 -- при использовании по назначению работает. Это задание заняло у меня больше 2 часов
# Создайте класс Персона с методами, позволяющими вывести на экран информацию о персоне, а также определить
# ее возраст (в текущем году). Создайте список из n персон, выведите полную информацию из базы на экран, а также
# организуйте поиск персон, чей возраст попадает в заданный диапазон. -- ЭТО НЕ СДЕЛАЛ ЕЩЁ
# При этом n, данные о персонах и диапазон вводятся с клавиатуры.
# Доп. задание: Сделать проверку на корректность введенных данных.

from my_classes.Person import Person

try:
    n = int(input("Number of people: "))
except Exception:
    print("This should be an integer.")
    n = int(input("Number of people: "))
print("Enter a person's name, surname, date of birth(yyyymmdd), separated by commas only (no whitespaces)\n"
      "Here's an example: \"John,Smith,19810125\" (use 05 instead of 5 etc): \n")

list_of_ppl = []
for i in range(n):
    data = input("person: ")
    d_list = data.split(",")
    list_of_ppl.append(Person(d_list[0], d_list[1], d_list[2]))
print()
for person in list_of_ppl:
    print(person.get_fname(), person.get_mname(), person.get_lname(), "is", person.get_age(),
          "years old, the DoB is", person.get_birthday())


def age_search():
    search = input("Please specify the needed age range separated by '-', like '1-37'\n")
    min_age = int(search.split("-")[0])
    max_age = int(search.split("-")[1])
    needed = [i for i in list_of_ppl if i.get_years() in range(min_age, max_age)]
    return needed


good = False
while not good:
    answer = input("\nWould you like to find people of specific age? Y/N\n")
    if answer == "Y" or answer == "y":
        print(f"There are {len(age_search())} people of that age")
        good = True
    elif answer == "N" or answer == "n":
        good = True
    else:
        print("Sorry, didn't get that. Come again?")