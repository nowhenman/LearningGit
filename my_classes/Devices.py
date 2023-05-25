# Задание со слайда 18
# Создать два класса Display и Mouse, расширенных от класса Device. Device содержит только один метод showData().
# Добавить в классе Display атрибут resolution(Float), а в класс Mouse wireless(Boolean).
# Переопределить базовый метод вывода информации об устройстве в каждому дочернем классе.

class Device:
    def show_data(self):
        print("Device")


class Display(Device):
    def __init__(self, inches: float, res: dict, price: float):
        self.__res = res
        self.__inches = inches
        self.__price = price

    def show_data(self):
        # Device.show_data(self)
        super().show_data()
        print(f"{self.__res}")


class Mouse(Device):
    def __init__(self, price: float, wireless: bool):
        self.__price = price
        self.__wireless = wireless


new_d = Display(17.3, {"width": 1920, "height": 1080}, 19000)
new_d.show_data()
