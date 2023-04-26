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


# эта функция должна быть в классе, не отдельно (понял по self и ошибке интерпретатора)
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
