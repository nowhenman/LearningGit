def bin_search(massiv, num):
    a, b = 0, len(massiv)
    ind = (a + b) // 2
    if a == b:
        if massiv[ind] == num:
            return ind
        else:
            return -1
    else:
        if massiv[ind] == num:
            return ind
        elif massiv[ind] > num:
            b = ind
            return bin_search(massiv[a:b], num)
        elif massiv[ind] < num:
            a = ind
            return ind + bin_search(massiv[a:b+1], num)


orig = [1, 500, -9, 0, 55, 71]
orig.sort()
# print(orig)

# ab = list(map(int, input("Введите список чисел: ").split()))
needed = int(input("искомое число: "))
print(bin_search(orig, needed))
