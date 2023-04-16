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
