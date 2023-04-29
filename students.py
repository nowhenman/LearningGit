class Student:
    pass


vasya = Student()
vasya.age = 22
vasya.univer = 'MSU'

petya = Student()
petya.last_name = 'Smirnov'
petya.age = 21
# print(vasya.age, vasya.univer)
# print(petya.last_name, petya.age)

# Задание 1.
# Создать список имен. Заполнить с клавиатуры (конец ввода - exit). Проверить существует ли в списке имя "Ольга".
# Если существует, то вывести на экран уведомление.
# Использовать выше описанный метод
names = []
while True:
    i = input("enter name: ")
    if i == 'exit':
        break
    names.append(i)
olga_free = True
if "Ольга" in names:
    olga_free = False
if not olga_free:
    print("Olga found!")
else:
    print("no Olga")
# Задание 2. Протестировать пример слайд 3 (правый блок)
# Результат отправить в гит!


# эта функция должна быть в классе, не отдельно (понял по self и ошибкам интерпретатора)
# вопрос -- если создать класс и в него пустить эту функцию, будет ли она работать с экземплярами других классов?
def display(self, text):
    for i in text:
        if i == ' ':
            return False
# функция display возвращает False, если в строке есть пробел и True, если пробела нет. Также она печатает строку
    print(text)
    return True


class User:
    display_info = display
# в новом клаасе User новый метод display_info это функция display (печатает текст и возвращает True в отсутствии ' '.


class Author:
    display_my_name = display
# аналогично


user = User()
if not user.display_info("hi, my name is Oulina"):
    # если display_info у user False (т.е. с пробелом):..
    print("Некорректные данные")
author = Author()
if author.display_my_name("Oulina"):
    # если display_my_name у author True (т.е. без пробела):..
    print("Корректное имя")

display("hi, my name is Oulina")
display("Oulina")
# эти две просто печатают текст, но возвращают соответственно False и True

# Задание 1 (новое)
# Создать класс "Студент". Описать в нем поля имя, университет и балл зачисления.
# Создать 3 объекта. Добавить их в список студентов.
# Проверить, есть ли в списке студенты, которые набрали менее 20 баллов. Вывести на экран общую сумму баллов.


class Student1:
    full_name = 'John Doe'
    uni = 'sharaga'
    points = -9999


maga = Student1()  # Не забывай скобки!
maga.full_name = 'Иван Михайлович Краснов'
maga.uni = 'МФТИ'
maga.points = 315

goga = Student1()  # Не забывай скобки!
goga.full_name = "Лев Исаакович Эйдельман"
goga.uni = 'имени Баумана'
goga.points = 352

vaha = Student1()  # Не забывай скобки!
vaha.full_name = 'Вахид Рамзанович Дудаев'
vaha.uni = 'МГУ'
vaha.points = 400

the_youth = [maga, goga, vaha]
points_more_20 = True
all_points = 0
for i in the_youth:
    if i.points < 20:
        points_more_20 = False
    all_points += i.points
print(points_more_20, all_points)


# Задание 2 (новое)
# Создать класс "Товар" со следующими полями: id, наименование, стоимость.
# Создать класс "Заказ" со следующими данными: номер, имя клиента, список товаров.
# В классе создать метод, который подсчитывает общую сумму заказа.
# Создать список с 3 заказами и разными товарами (товары могут пересекаться).
# Вывести на экран, есть ли заказы стоимостью менее 1000 рублей. Вывести общую сумму за все заказы.

class Product:
    def __init__(self, id1, name, price):
        self.id = id1
        self.name = name
        self.price = price


class Order:
    def __init__(self, number, customer, items):
        self.ord_no = number
        self.client = customer
        self.items = items

    def amount(self):
        spent = 0
        for i in self.items:
            spent += i.price  # where i == name in Product
        return spent
# В классе создать метод, который подсчитывает общую сумму заказа.
# Создать список с 3 заказами и разными товарами (товары могут пересекаться).
# ===можно ли создать список и в нем уже прописать всё? чтоб не как в первом примере===
# Вывести на экран, есть ли заказы стоимостью менее 1000 рублей. Вывести общую сумму за все заказы.


mango = Product(1, 'Манго египетское', 300)
detergent = Product(2, "Порошок Persil 2 л. для деликатной стирки", 500)
iPhone = Product(3, "iPhone 11 Pro Max восстановленный 512 ГБ", 50000)
catnip = Product(4, "Кошачья мята 15 г.", 75)
chicken_fillet = Product(5, "Филе куриной грудки свежее 500 г", 200)

items1001 = [detergent, catnip, chicken_fillet]
items1528 = [mango, detergent, iPhone]
items1784 = [chicken_fillet]

order1 = Order(1001, "Ivan Ivanov", items1001)
order2 = Order(1528, 'Marina Klyuchik', items1528)
order3 = Order(1784, "Rakhmon Aliev", items1784)
print(order1.amount, order2.amount, order3.amount)