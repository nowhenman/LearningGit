from random import randint as ri

class Node:
    def __init__(self, number):
        self.value = number
        self.left = None
        self.right = None


class BinTree:
    def __init__(self):
        self.__root = None

    def insert(self, number):
        if self.__root == None:
            self.__root = Node(number)
        else:
            self.__bin_insert_rec(number, self.__root)

    def __bin_insert_rec(self, number, parent_node):
        if number > parent_node.value:
            if parent_node.right == None:
                parent_node.right = Node(number)
            else:
                self.__bin_insert_rec(number, parent_node.right)
        elif number < parent_node.value:
            if parent_node.left == None:
                parent_node.left = Node(number)
            else:
                self.__bin_insert_rec(number, parent_node.left)

    def search(self, number):
        if self.__root == None:
            return "Your tree is empty"
        else:
            return self.__bin_search_rec(number, self.__root)

    def __bin_search_rec(self, number, node):
        if node == None:
            return False
        if number == node.value:
            return True
        if number > node.value:
            return self.__bin_search_rec(number, node.right)
        if number < node.value:
            return self.__bin_search_rec(number, node.left)

    def print(self):
        self.__print_rec(self.__root)

    def __print_rec(self, node):
        if node != None:
            self.__print_rec(node.left)
            print(node.value, end=' ')
            self.__print_rec(node.right)


my_tree = BinTree()
for i in range(10):
    my_tree.insert(ri(1, 15))

search = ri(0, 5)
print(my_tree.search(search))

my_tree.print()
print()
print(search)