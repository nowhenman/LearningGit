
# Задание 4.
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
