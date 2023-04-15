a = 3
print("hi joe" if a == 1 else "oh no")

Python <2.6: "Hello %s" % name
Python 2.6+: "Hello {}".format(name)   (uses str.format)
Python 3.6+: f"{name}"   (uses f-strings)