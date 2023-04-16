# Задание №1 -- работает
# С клавиатуры вводятся три целых числа. Найти среди них максимум.
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
max_three = max(first, second, third)
print("Максимальное число -- %s" % max_three)

#                                                                                                                       Задание №2.
# Перевести число, введенное пользователем, в байты или килобайты в зависимости от его выбора.

# Задание №3 -- работает
# Вводится год. Определить, является ли он високосным или обычным.
# Високосными являются года, которые делятся на 4, за исключением столетий, которые не делятся на 400.


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(leap_year(int(input("Enter a year: "))))

# Задание №4 -- работает
# Пользователь вводит два числа. Одно присваивается одной переменной, а второе - другой.
# Необходимо поменять значения переменных так, чтобы значение первой оказалось во второй, а второй - в первой.
a = float(input("number 1: "))
b = float(input("number 2: "))
a, b = b, a
print("number 1 is {n1}, number 2 is {n2}".format(n1=a, n2=b))

# Задание №5 -- работает, но зачем?..
# В программе определяется переменная PI 3.141593. Требуется вывести на экран значение PI с двумя знаками после запятой.
pi = 3.141593
print("Pi kind of equals %.2f" % pi)

# Задание №6 -- работает
# Дана следующая функция y=f(x):
# y = 2x - 10, если x > 0
# y = 0, если x <= 0
# Требуется найти значение функции по переданному x.


def new_func(x):
    if x <= 0:
        return "y = 0"
    else:
        y = 2 * x - 10
        return "y равно {y}".format(y=y)


print(new_func(float(input("Введите x: "))))

# Задание №7 -- работает
# Вводятся два целых числа. Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом, а также остаток (если он есть) и частное (в любом случае).
fnum, snum = int(input("first integer: ")), int(input("second integer: "))
try:
    if fnum % snum == 0:
        print("Делится нацело, частное %s" % (fnum // snum) if ... else "bla")
    else:
        print("Нацело не делится, остаток %s, неполное частное %s" % ((fnum % snum), (fnum // snum)))
except ZeroDivisionError:
    print("Нельзя делить на ноль")

# Задание №8 -- работает
# Найти сумму и произведение цифр, введенного натурального числа от 10 до 99.
# Например, если введено число 76, то сумма его цифр равна 13 (7+6), а произведение 42 (7*6).
victim = str(input("Your two-digit number: "))
f_dig, s_dig = int(victim[0]), int(victim[1])
print("The sum is: %d" % (f_dig + s_dig))
print("The multipication is: %d" % (f_dig * s_dig))

# Задание №9 -- работает
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
three_d = str(input("Your three-digit number: "))
f_dig, s_dig, t_dig = int(three_d[0]), int(three_d[1]), int(three_d[2])
print("The sum is: {sum}".format(sum=(f_dig + s_dig + t_dig)))
print("The multipication is: {mul}".format(mul=(f_dig * s_dig * t_dig)))

# Задание №10 -- работает (оба варианта)
# Ввести с клавиатуры вещественное число (с плавающей точкой).
# Определить является ли оно положительным и вывести результат на экран.
# не совсем понял сложность задания, так как в любом случае надо использовать float
sus = float(input("Введите число: "))
# print("больше нуля" if sus > 0 else ("равен нулю" if (sus == 0) else "меньше нуля")) # ужасно
print("больше нуля" if sus > 0 else "меньше или равен 0")  # то, что нужно

# Задача №11 -- работает
# В зависимости от ввода вычислить массу, плотность или объем. Для расчетов использовать формулу m = Vρ.
given = input("\nВведите данные (вы можете ввести два значения из трёх -- m (масса), v (объём) и p (плотность).\n"
              "Формат ввода: тип значения(буква m, v или p) и величину (масса в кг, объём в м^3, например \"m120 v27\"."
              "\nПрограмма самостоятельно рассчитает оставшийся параметр: ").split()

for i in given:
    if i[0] == "m":
        mass = float(i[1:])
    elif i[0] == "v":
        volume = float(i[1:])
    elif i[0] == "p":
        rho = float(i[1:])

par_1 = given[0]
par_2 = given[1]
m_1 = ("p", "v")
v_1 = ("p", "m")
p_1 = ("m", "v")

if par_1[0] and par_2[0] in p_1:
    print("Плотность равна %f кг/м^3" % (mass / volume))
elif par_1[0] and par_2[0] in v_1:
    print("Объём равен %f м^3" % (mass / rho))
elif par_1[0] and par_2[0] in m_1:
    print("Масса равна %f кг" % (rho * volume))
else:
    print("something's wrong")

# Задание №12 -- работает
# С клавиатуры вводятся три целых числа. Найти среди них максимум.
# Просто второй вариант решения


def max_number(nums):
    all_three = [int(input("Введите число: ")) for i in range(nums)]
    return max(all_three)


print("Максимальное число --", max_number(3))

# Задание №13 -- работает
# С клавиатуры вводится число n. Вычислить сумму S=1/1+1/2+1/3+...+1/n.
# Ответ вывести с точностью до 4 знака после запятой, общее количество символов – 10.
n = int(input("Enter a number: "))
if len(str(n)) > 9:
    print("Number too big")
else:
    s = 0
    for i in range(1, n+1):
        s += 1 / i
    print("Сумма S для числа {n} равна {sum:10.4f}".format(n=n, sum=s))


# Задание №14 -- работает
# С клавиатуры вводится число n. Узнать, является ли n факториалом какого-либо числа? Если да, то вывести это число.
from math import factorial
n = int(input("Enter your number: "))
s, i = 0, 0
while s <= n:
    s = factorial(i)
    if s == n:
        print("{input} is a factorial of {num}".format(input=n, num=i))
        break
    i += 1
if s > n:
    print("Apparently, {input} is not a factorial of any number".format(input=n))


# Задание №15 -- работает
# С клавиатуры вводится целое число. Вывести звездочками последовательность Фибоначчи (считаем «с единицы»).
def fib(number):
    prev = 0
    curr = 1
    next_v = 1
    for i in range(1, number+1):
        print(next_v * "*", str(next_v))
        prev = curr
        curr = next_v
        next_v = prev + curr


user = int(input("Enter the number of iterationbs: "))
fib(user)
