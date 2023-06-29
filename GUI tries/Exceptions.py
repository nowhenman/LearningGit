# Задание 1 -- Done
# Написать функцию, которая принимает два числа и строку, характеризующую арифметическое действие, одно из */+-,
# например «+». Подпрограмма должна вычислить указанное выражение и вернуть ответ. Предусмотреть поимку исключения
# в необходимой ситуации.
def here_goes_nothing():
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    except (TypeError, ValueError):
        # return "The input must be a number"
        raise Exception("some text")
    else:
        operand = input("operand: ")
        if operand == '+':
            return num1 + num2
        elif operand == '-':
            return num1 - num2
        elif operand == '*':
            return num1 * num2
        elif operand == '/':
            try:
                return num1 / num2
            except ZeroDivisionError:
                return "Division by zero!"
        else:
            return "Can't recognise this operand"


# валидация данных должна быть отдельно! Только потом основная функция.

try:
    print(here_goes_nothing())
except Exception as e:
    print(e)

# Задание 2.
# Пользователь вводит с клавиатуры количество элементов списка. Заполнить список случайными числами в диапазоне
# от -10 до 10. Пользователь вводит номер элемента массива, который хочет вывести. Предусмотреть исключения на
# ввод чисел и корректный номер элементам массива, который требуется отобразить.

from random import randint
# input
# valid
# main


class StupidException(Exception):
    def __init__(self, message):
        super().__init__(message)


def is_valid_int(x):
    try:
        x = int(x)
    except ValueError:
        raise StupidException("Integers only!")


def is_in_range(x, mass):
    try:
        a = mass[x]
    except IndexError:
        raise StupidException("Index is out of range!")


amount = input("Items count: ")
try:
    is_valid_int(amount)  # либо ничего и это норм либо ошибка и ж...
except StupidException as se:
    print(se)
else:
    amount = int(amount)

rand_list = [randint(-10, 10) for i in range(amount)]

rand_ind = input("Index: ")
try:
    is_valid_int(rand_ind)
except StupidException as se:
    print(se)
else:
    rand_ind = int(rand_ind)

try:
    is_in_range(rand_ind, rand_list)
except StupidException as se:
    print(se)
else:
    print(rand_list[rand_ind])

# Задание 3.
# Пользовать вводит свой возраст. Требуется выбросить исключение, если введен некорректный возраст.
# Создать собственный класс для выдачи исключения.
# Пользователь вводит логин и пароль. Выдавать сообщение об ошибке, если хоть один из введенных параметров
# содержит менее 6 символов.


def age_ok(x):
    if x < 0 or type(x) != int:
        raise StupidException("Age must be a positive integer!")


def char_6(x):
    if len(x) < 6:
        raise StupidException("At least 6 characters long!")


t_age = input("Enter age: ")
try:
    is_valid_int(t_age)
    t_age = int(t_age)
    age_ok(t_age)
except StupidException as se:
    print(se)
    exit(0)
else:
    age = t_age

print(age)
# физически больно видеть все эти данные напрямую
t_login = input("Enter your login: ")
t_password = input("Enter your password: ")

try:
    char_6(t_login)
except StupidException as se:
    print(se)
else:
    login = t_login

try:
    char_6(t_password)
except StupidException as se:
    print(se)
else:
    password = t_password


# Задание 4

from Registration import Registration

Registration.validity_check(input("login: "), input("password: "), input("confirm password: "))

# Набор ссылок (если будут вопросы)
# https://rollbar.com/blog/throwing-exceptions-in-python/
# https://www.programiz.com/python-programming/user-defined-exception
# https://realpython.com/regex-python/ - материал сложный (его будем подробно разбирать вместе)
