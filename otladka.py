# Задание №2 -- работает, горжусь
# Перевести число, введенное пользователем, в байты или килобайты в зависимости от его выбора.
# Переводим размер в число байт
user_bytes = input("Введите размер (в формате \"число b/kB/MB/GB/TB\"): ").split()
user_bytes[0] = float(user_bytes[0])
kilo = ("kb", "KB", "kB", "Kb")
mega = ("mb", "MB", "mB", "Mb")
giga = ("gb", "GB", "gB", "Gb")
tera = ("tb", "TB", "tB", "Tb")

if user_bytes[1] in kilo:
    ubytes = int(user_bytes[0]*1000)
    print("{num} kB is {n} bytes (note: kilo- is a power of 10, not 2).".format
          (num=user_bytes[0], n=ubytes))
elif user_bytes[1] in mega:
    ubytes = int(user_bytes[0] * 1000000)
    print("{num} MB is {n} bytes (note: mega- is a power of 10, not 2).".format
          (num=user_bytes[0], n=ubytes))
elif user_bytes[1] in giga:
    ubytes = int(user_bytes[0] * 1000000000)
    print("{num} GB is {n} bytes (note: giga- is a power of 10, not 2).".format
          (num=user_bytes[0], n=ubytes))
elif user_bytes[1] in tera:
    ubytes = int(user_bytes[0] * 1000000000000)
    print("{num} TB is {n} bytes (note: tera- is a power of 10, not 2).".format
          (num=user_bytes[0], n=ubytes))
elif user_bytes[1] == "b":
    ubytes = int(user_bytes[0])
    print("You entered {n} bytes".format(n=ubytes))
else:
    print("incorrect input")
    exit("stopping")

# Переводим байты в иную размерность
response = input("Would you like to convert it? If yes, enter the unit (kB/MB etc.). If no, enter 0: \n")
if response == '0':
    exit("stopping")
elif response in kilo:
    ubytes /= 1000
    if int(ubytes) == ubytes:
        ubytes = int(ubytes)
    print("That's {n} kB.".format(n=ubytes))
elif response in mega:
    ubytes /= 1000000
    if int(ubytes) == ubytes:
        ubytes = int(ubytes)
    print("That's {n} MB".format(n=ubytes))
elif response in giga:
    ubytes /= 1000000000
    if int(ubytes) == ubytes:
        ubytes = int(ubytes)
    print("That's {n} GB".format(n=ubytes))
elif response in tera:
    ubytes /= 1000000000000
    if int(ubytes) == ubytes:
        ubytes = int(ubytes)
    print("That's {n} TB".format(n=ubytes))
else:
    print("incorrect input.")
    exit("stopping")

