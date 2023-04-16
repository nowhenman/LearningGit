def bin_search(massiv, num):
    massiv.sort()
    ind = len(massiv)//2
    x = massiv[ind]
    if x == num:
        return ind
    elif x > num:
        massiv = massiv[:ind]
        return bin_search(massiv, num)
    elif x < num:
        massiv = massiv[ind:]
        return bin_search(massiv, num)
    return -1


a = list(map(int, input("Введите список чисел: ").split()))
needed = int(input("искомое число: "))
print(bin_search(a, needed))

# от 0 до n-1 только перестраивать диапазон индексов, а не трогать!
# попробуй на листе бумаги!
# тащить границы диапазона в котором (переобозначать не массив, а его индексы!)

