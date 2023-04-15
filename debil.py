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

par_1 = given[0]
par_2 = given[1]
mass = ("p", "v")
volume = ("p", "m")
plotnost = ("m", "v")

if par_1[0] and par_2[0] in plotnost:
    print("Плотность равна %d" % 1)
elif par_1[0] and par_2[0] in volume:
    print("Объём равен %d" % 1)
elif par_1[0] and par_2[0] in mass:
    print("Масса равна %d" % 1)
else:
    print("something's wrong")
print(par_1, par_2)
