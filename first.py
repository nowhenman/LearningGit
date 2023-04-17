# Задание 1 -- работает
# С клавиатуры ввести количество элементов списка.
# Заполнить один список случайными числами, другой - введенными с клавиатуры числами,
# в ячейки третьего записать суммы соответствующих ячеек первых двух. Вывести содержимое списков на экран.
from random import randint
from math import factorial
elem = int(input("Количество элементов списка: "))
list_2 = [int(input("Введите число: ")) for n in range(elem)]
list_1 = [randint(-100500, 100500) for i in range(elem)]
list_3 = [(list_1[i]+list_2[i]) for i in range(elem)]
print(list_1, list_2, list_3, sep='\n')

# Задание 2 -- работает
# С клавиатуры ввести количество элементов списка. Заполнить список случайными числами от -50 до 50.
# Найти номер минимального по модулю элемента списка.
# Например, в списке [10, -3, -5, 2, 5] минимальным по модулю элементом является число 2. Его номер 3.

# from random import randint
# т.к. выше уже есть
count = int(input("Количество элементов списка: "))
abs_list = [randint(-50, 50) for j in range(count)]
start = abs(abs_list[0])
val = 0
for i in range(1, len(abs_list)):
    if abs(abs_list[i]) < start:
        start = abs(abs_list[i])
        val = i
print(val)

# Задание 3 -- работает
# С клавиатуры ввести количество элементов списка. Заполнить список случайными числами от 1 до 100.
# Найти в списке те элементы, значение которых меньше среднего арифметического, взятого от всех элементов списка.

# from random import randint
kk = int(input("Количество элементов списка: "))
llist = [randint(1, 100) for x in range(kk)]
aver = sum(llist) / kk
nnew = []
for h in llist:
    if h < aver:
        nnew.append(h)
print(nnew)

# Задание 4 -- работает
# С клавиатуры ввести количество элементов списка. Заполнить список случайными числами от 0 до 10.
# В одномерном списке целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# from random import randint
jeez = int(input("количество элементов списка: "))
mins = [randint(0, 10) for k in range(jeez)]
min_1 = min(mins)
mins.remove(min_1)
min_2 = min(mins)
print(min_1, min_2, sep='\n')


# Задание 5 -- работает
# В списке чисел проверить, все ли элементы являются уникальными, т. е. каждое число встречается только один раз.
user_list = input("Введите числа через пробел:\n").split()
user_set = set(user_list)

if len(user_set) == len(user_list):
    print("Все элементы уникальны")
else:
    print("Есть одинаковые")

# Задание 6 -- работает, но...
# Даны два списка и необходимо найти их совпадающие элементы, которые присутствуют в обоих списках.
# вариант 1 -- работает
list_1 = ['abc', 1535, 1535, ['lost', 'in', 'space'], True, (100010011001001100010, 1)]
list_2 = [1536, 1998, (1010010010011100110101, 0), ['lost'], 'abc', 1535, False]
shared = []
for i in list_1:
    if i in list_2 and i not in shared:
        shared.append(i)
print(shared)

# вариант 2 -- ошибка, надо убрать список из списка
list_1 = ['abc', 1535, ['lost', 'in', 'space'], True, (100010011001001100010, 1)]
list_2 = [1536, 1987, (1010010010011100110101, 0), ['lost'], 'abc', 1535, False]
list_1, list_2 = set(list_1), set(list_2)

print(list(list_1 & list_2))

# Задание 7 -- работает
# Создать множество всех наименований месяцев года.
# Пользователь вводит имя месяца, а программа удаляет из множества указанный месяц.
# Сравнить методы remove() и discard().
months = {
    'January', 'February', 'March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December'
}

useless = input("Choose a month to remove:\n")
months.discard(useless)
# Метод discard(), в отличие от метода remove(), не выдаст критическую ошибку при отсутствии элемента.
print(months)

# Задание 8 -- работает
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
winter = (12, 1, 2)
spring = (3, 4, 5)
summer = (6, 7, 8)
autumn = (9, 10, 11)


def season(month):
    if month in winter:
        print("WINTER")
    elif month in spring:
        print("SPRING")
    elif month in summer:
        print("SUMMER")
    elif month in autumn:
        print("AUTUMN")
    else:
        print("wrong input")

# Задание 9 -- работает
# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.


def bank(a, years):
    interest = 10  # переменная, а не число, чтобы потом можно было легко изменить и не искать по всему коду
    money = a * (((100 + interest) / 100) ** years)
    return money

# Задание 10 -- работает
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Задание 11 -- работает
# Написать функцию, принимающую число секунд, и отображающую результат на консоль в виде: дни:часы:минуты:секунды.


# from random import randint


def timenotes(sec):
    days = sec // 86400
    sec %= days
    hours = sec // 3600
    try:
        sec %= hours
    except ZeroDivisionError:
        pass
    minutes = sec // 60
    try:
        sec %= minutes
    except ZeroDivisionError:
        pass

    print(str(days) + ' days : ' + str(hours) + ' hours : ' + str(minutes) + ' minutes : ' + str(sec) + ' seconds')


for i in range(200):
    timenotes(randint(0, 1234567890))


# Задание 12 -- работает
# С помощью анонимной функции извлеките из списка числа, делимые на 15.
# from random import randint
length = 20
generic = [randint(-500, 500) for x in range(length)]
# print(generic)
new_list = list(filter(lambda x: (x % 15 == 0), generic))
print(new_list)
# С map и filter мне точно нужно разобраться, а не копировать из интернета

# Задание 13 -- работает
# По координатам точки определите принадлежности к одной из координатных четвертей.

x = float(input("X coordinate:\n"))
y = float(input("Y coordinate:\n"))
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)

# Задание 14 -- работает
# Определите, принадлежит ли точка x одному из выделенных отрезков B или D.
x = float(input("Введите число:\n"))
print("YES" if (-3 <= x <= 1) or (5 <= x <= 9) else "NO")

# Задание 15 -- работает
# Создать кортеж цветов (не менее 5 цветов).
# Пользователь вводит с клавиатуры цвет, а программа должна вывести на экран присутствует ли этот цвет в палитре.

colours = ('Черный', 'Белый', 'Синий', 'Желтый', 'Красный', 'Зеленый')
colour = input("Введите цвет:\n")
print("Цвет есть в палитре!" if colour in colours else "Цвета нет в палитре!")

# Задание 16 -- работает
# Проходит соревнование по плаванию. Администратор должен ввести с клавиатуры количество участников,
# а затем Фамилии и Города участников. Требуется вывести на экран уникальные наименования
# городов участников и самую часто встречающуюся фамилию.
people = int(input("Количество участников: "))
competes_list = [input("Фамилия и город: ").split() for x in range(people)]
competes_dict = {competes_list[i][0]: competes_list[i][1] for i in range(people)}
un_cities = set(competes_dict.values())
print("Уникальные города: " + str(un_cities))

old_var = 0
new_var = 0
popular_name = ''
names = competes_dict.keys()

surname = [i for i in names]
for i in surname:
    new_var = surname.count(i)
    if new_var > old_var:
        old_var = new_var
        popular_name = i
print("Самая популярная фамилия: " + popular_name)

#                                                                                                                       Задание 17.
# Администратор заполняет данные о животных зоопарка. Сначала он должен ввести количество видов животных.
# Затем вводится наименование вида (например, лев) и количество особей данного вида.
# Если администратор уже вводил информацию по какому-то виду и пытается сделать это повторно, вывести ему уведомление:
# «Данный вид уже был введен! Хотите изменить количество особей?». Вывести на экран введенные данные.
# Протестировать на различных примерах, демонстрирующих работу всей программы.
# Написать самостоятельно тесты к данному заданию, как это сделано в первой-второй задаче
# (можно сделать в обычном текстовом документе).
# P.S. Подумать над типом данных переменной, в которой будут храниться и название вида, и его количество.

species = int(input("Количество видов: "))
zoo = {}
for j in range(species):
    s = input("Вид и количество: ").split()
    if s[0] in zoo:
        change = input("Данный вид уже был введен! Хотите изменить количество особей? Y/N \n")
        if change == 'N' or change == 'n':
            pass
        elif change == 'Y' or change == 'y':
            zoo[s[0]] = int(s[1])
            pass
        else:
            print("Некорректный ввод.")
            pass
    else:
        zoo[s[0]] = int(s[1])
print(zoo)

# Задание 18 -- работает
# Пользователь должен ввести с клавиатуры количество студентов. Проверить введенную информацию на корректность.
# Например, человек вводит не число, а свое имя.
try:
    students = int(input("Введите количество студентов: "))
    print("Принято!")
except ValueError:
    print("Число должно быть в формате int!")

# Задание 19 -- работает
# Последовательность чисел вводится до «нуля». Найти среди них максимум и минимум.
x = []
while True:
    y = float(input())
    if y != 0:
        x.append(y)
    else:
        break
print("minimum is: " + str(min(x)))
print("maximum is: " + str(max(x)))

# Задание 20 -- работает
# Вводится число N. Вычислить сумму S = (1^2)/1! + (2^2)/2! + ... + (n^2)/n!
# Ответ вывести с точностью до 3 знака после запятой, общее количество символов – 8

# from math import factorial
N = int(input())
S = 0
for i in range(1, N):
    S += ((i**2) / factorial(i))
print('%.3f' % S)
