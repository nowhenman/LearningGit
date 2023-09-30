# 7. Write a Python program to create a class representing a linked list data structure.
# Include methods for displaying linked list data, inserting and deleting nodes.

# 8. Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.

# 11. Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions.

class Queue:
    def __init__(self):
        self.__queue = []

    def add(self, elem):
        self.__queue.append(elem)

    def remove(self):
        return self.__queue.pop(0) if len(self.__queue) != 0 else "List is empty"

    def show(self):
        print("last added shown on the right", self.__queue)


a = Queue()
a.add("first")
a.add(2)
a.add(2)
a.show()
print("item removed: ", a.remove())
a.show()
