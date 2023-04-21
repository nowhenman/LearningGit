# Задание №14 -- вариант 2 -- работает
# С клавиатуры вводится число n. Узнать, является ли n факториалом какого-либо числа? Если да, то вывести это число.

try:
    n = int(input("Enter your number: "))
except ValueError:
    print("integers only")
    exit()
if n <= 0:
    print("No, positive integers only")
    exit()
if n == 1:
    print("1 is the factorial of both 0 and 1")
    exit()
s = 1
j = 1
while j <= n:
    s *= j
    if s == n:
        print("{input} is a factorial of {num}".format(input=n, num=j))
        break
    if s > n:
        print("Apparently, {input} is not a factorial of any number".format(input=n))
        break
    j += 1

# Задание №9 -- вариант 2 -- работает
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
three_d = int(input("Your three-digit number: "))
f_dig, s_dig, t_dig = (three_d // 100), (three_d // 10 % 10), (three_d % 10)
print("The sum is: {sum}".format(sum=(f_dig + s_dig + t_dig)))
print("The multipication is: {mul}".format(mul=(f_dig * s_dig * t_dig)))
