from my_classes.Person import Person

John = Person("John", "Smith", "19900805")
John.set_mname("Michael")
print(John.get_fname(), John.get_mname(), John.get_lname(), "is", John.get_age(), "old, his DoB is", John.get_birthday())
