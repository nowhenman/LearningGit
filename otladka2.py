
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

cart1001 = [detergent, catnip, chicken_fillet]
cart1528 = [mango, detergent, iPhone]
cart1784 = [chicken_fillet]

order1 = Order(1001, "Ivan Ivanov", cart1001)
order2 = Order(1528, 'Marina Klyuchik', cart1528)
order3 = Order(1784, "Rakhmon Aliev", cart1784)

all_orders = []
print(order1.amount(), order2.amount(), order3.amount())  # Не забывай скобки!!!

# Вывести на экран, есть ли заказы стоимостью менее 1000 рублей. Вывести общую сумму за все заказы.

less_1000 = False
if