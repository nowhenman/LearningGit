"""
Задание 2.
Создать класс Комплексного числа. Поля – действительная и мнимая часть числа. По умолчанию обе части равны 0.
Добавить функционал вывода на экран информации о комплексном числе.
Создать два объекта класса и продемонстрировать работу приложения.
"""


def is_equal(a, b):
    if a.get_real() == b.get_real() and a.get_imag() == b.get_imag():
        return True
    else:
        return False


class ComplexNumber:
    __real = 0
    __imag = 0

    def __str__(self):
        return f"A complex number {self.get_complex()} -- real is {self.__real}, imaginary is {self.__imag}."

    def set_real(self, real):
        self.__real = float(real)  # self!!!!!!

    def set_imag(self, imag):
        self.__imag = float(imag)

    def get_real(self):
        return self.__real

    def get_imag(self):
        return self.__imag

    def get_complex(self):
        if self.__imag > 0:
            return f"{self.__real} + {self.__imag}i"
        elif self.__imag < 0:
            return f"{self.__real}{self.__imag}i"
        else:
            return f"{self.__real}"

    def set_complex(self, real, imag):
        self.__real = float(real)
        self.__imag = float(imag)


