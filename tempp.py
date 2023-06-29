class Nigger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shoot(self):
        print("Bang-bang motherfucka!")

    @staticmethod
    def eat_chicken():
        print("Oh these chicken wings!")

    @classmethod
    def steal(cls, obj):
        print(f"I just stole your {obj} nigga!")


d_w = Nigger("Denzel Washington", 23)
print()
d_w.shoot()
d_w.eat_chicken()
d_w.steal("bike")
print()
print()


class NiggaWannabe(Nigger):
    def shoot(self):
        print("Poluchai suka!")

    @staticmethod
    def eat_chicken():
        print("Vkustno...")

    @classmethod
    def steal(cls, obj):
        print(f"Vash {obj} smenil locatsiyu")


j_c = NiggaWannabe("Jim Carrey", 40)
j_c.shoot()
j_c.eat_chicken()
j_c.steal("bicycle")

print()
print()

# NiggaWannabe.shoot() просто функция без объекта не работает
NiggaWannabe.eat_chicken()  # @staticmethod работает
NiggaWannabe.steal("velosiped")  # @classmethod работает


class White:
    pass


t_s = White()

# t_s.shoot()
# t_s.eat_chicken
# t_s.steal("velik")
