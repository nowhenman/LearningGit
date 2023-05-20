from my_classes.ComplexNumber import *

default = ComplexNumber()

first = ComplexNumber()
first.set_complex(15, -3.8)

second = ComplexNumber()
second.set_real(-15.9)
second.set_imag(0)

two_are_equal = False

if is_equal(first, second):
    two_are_equal = True

# print(first)
# print(second)
print("Hooray" if two_are_equal else "Oh no")
# print("Hooray") if two_are_equal else print("Oh no")
