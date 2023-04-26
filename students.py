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
