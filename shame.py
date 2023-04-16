# Занятие с плохим преподом: вот он учил меня делать класс:

class Stack:
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.append(element)

    def pop(self):
        last = self.array[len(self.array)-1]
        self.array = self.array[:len(self.array[-1])]
        return last


new_stack = Stack()
new_stack.push("H")
new_stack.push("i")
print(new_stack.pop())

# А ещё он предложил мне решить ханойскую башню
# day = 3
# month = 4
# year = 2023


a = 1
b = 2
c = 3
start = [3, 2, 1]
aux = []
dest = []


def new_func():
    pass


# 32
#
# 1

# 3
# 2
# 1

# 3
# 21
#

#
# 21
# 3

# 1
# 2
# 3
