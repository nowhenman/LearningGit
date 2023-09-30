class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, number):
        self.__stack.append(number)

    def pop(self):
        return self.__stack.pop() if len(self.__stack) != 0 else "List is empty"

    def show(self):
        if self.__stack:
            print("last added shown on top")
            for elem in self.__stack[::-1]:
                print(elem)
        else:
            print("stack is empty lol")


super_stack = Stack()
print(super_stack.pop())
super_stack.push(15)
super_stack.push(7)
print(super_stack.pop())
super_stack.push(89)
super_stack.show()

aver_stack = Stack()
aver_stack.push(1)
aver_stack.push(0)
aver_stack.pop()
aver_stack.pop()
aver_stack.show()
