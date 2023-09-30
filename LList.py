class LinkedList:
    def __init__(self):
        self.__len = 0
        self.__head = None
        self.__tail = None

    class __Node:
        def __init__(self, number):
            self.elem = number
            self.prev = None
            self.next = None

    def insert(self, pos, number):
        if pos > self.__len:
            raise IndexError
        elif pos == self.__len:
            self.add(number)
        elif pos > self.__len // 2:
            # go tail-first справа
            current_node = self.__tail
            i = self.__len - 1
            while i > pos:
                current_node = current_node.prev
                i -= 1
            new_node = LinkedList.__Node(number)
            current_node.prev.next = new_node
            new_node.prev = current_node.prev
            current_node.prev = new_node
            new_node.next = current_node
            self.__len += 1

        elif pos != 0:
            # go head-first слева
            current_node = self.__head
            i = 0
            while i < pos - 1:
                current_node = current_node.next
                i += 1
            new_node = LinkedList.__Node(number)
            current_node.next.prev = new_node
            new_node.next = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            self.__len += 1
        else:
            new_node = LinkedList.__Node(number)
            self.__head.prev = new_node
            new_node.next = self.__head
            self.__head = new_node
            self.__len += 1

    def add(self, number):
        new_node = LinkedList.__Node(number)
        if self.__len == 0:
            self.__head = new_node
            self.__tail = self.__head
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
        self.__len += 1

# создал метод -- напиши атрибуты! лолгика потом...
    def remove(self):
        pass

    def len(self):
        return self.__len

    def show(self):
        current_node = self.__head
        while current_node is not None:
            print(current_node.elem, end=' ')
            current_node = current_node.next
        print()


my_ll = LinkedList()
my_ll.add(10)
my_ll.show()
my_ll.add(20)
my_ll.insert(0, 5)
my_ll.show()