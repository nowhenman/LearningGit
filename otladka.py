def bin_search(massiv, num):
    massiv.sort()
    ind = len(massiv) // 2
    x = massiv[ind]
    if x == num:
        return ind
    elif x > num:
        temp_massiv = massiv[:ind]
        return bin_search(temp_massiv, num)
    elif x < num:
        temp_massiv = massiv[ind:]
        return bin_search(temp_massiv, num)
    return -1


ab = list(map(int, input("Введите список чисел: ").split()))
target_no = int(input("Искомое число: "))
print("Индекс искомого числа -- {ind_1}".format(ind_1=bin_search(ab, target_no)))

# от 0 до n-1 только перестраивать диапазон индексов, а не трогать!
# попробуй на листе бумаги!
# тащить границы диапазона в котором (переобозначать не массив, а его индексы!)
