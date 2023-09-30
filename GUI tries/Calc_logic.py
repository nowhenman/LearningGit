import re
const = {
    "PLUS": "+",
    "MINUS": "-",
    "MULTIPLY": "*",
    "DIVIDE": "/",
    "EQUALS": "=",
    "PERCENT": "%",
    "ONE_OF": "1/x",
    "SQ_ROOT": "**0.5",
    "POINT": ".",
    "PLUS_MINUS": "+-",
    "SQUARED": "**2"
}


def operand(x, *args):  # возвращает число, которую надо перевести в строку
    if x == '+':
        a, b = args
        return a + b
    elif x == '-':
        a, b = args
        return a - b
    elif x == '/':
        a,b = args
        try:
            return a / b
        except ZeroDivisionError:
            return 'ZeroDivisionError'
    elif x == '*':
        a,b = args
        return a * b


# actions = []

main_memory = ''
temp_memory = ''


# максимум 16 символов в поле (16 символов норм, если 17 то научная) умножение сложение
# при нажатии на 0-9 проверяем общую длину поля

# регистр общ. переменной влево в 10 раз + кнопка
# и вывод всего этого безобразия в поле

def number(mm, x):
    mm += str(x)
    return mm


def int_float_check(x):  # убирает лишние нули  # done
    return x[:-2] if x.endswith(".0") else x


def backspace(mm):  # done  
    mm = mm[:-1]
    return mm


def percent(tm, mm):
    if tm == '':
        return tm, mm
    else:
        mm = tm / 100 * mm  # регулярка на символы!
        tm += mm  # не плюс!
        return tm, mm
    # main заменяется на процент от temp


def ce():  # done
    return ''


def c():  # done
    return '', ''


def one_of_x(tm, mm):
    tm += f'1/({mm})'
    mm = "тут надо tm разобрать и выполнить"  # equals()?..  todo
    return tm, mm


def x_squared(tm, mm):  # done
    tm = f'{tm} sqr({mm})'
    mm = float(mm) ** 2
    return tm, mm


def sq_root(tm, mm):
    tm = f'{tm} √({mm})'
    mm = float(mm)**0.5
    return tm, mm


def plus_minus(mm):
    if float(mm) > 0:
        mm = f'-{mm}'
    elif float(mm) < 0:
        mm = mm[1:]
    return mm


def point(mm):  # done
    mm += '.'
    return mm


def basics(tm, mm,  const_key):  # !!!!!!!11
    tm = mm + ' ' + const[const_key]  # не mm, а результат действий equals
    mm = 0  # todo
    return tm, mm


def equals(tm, mm):
    tm += f' {mm} ='  # ?
    pass  # action
    # должен смотреть на tm и выполнять A operand C из нее, и как-то повторять ещё действие
    # tm = '5 +'
# tm = '5 + (10)'
# operand = re.search('(?<=abc)def', tm)
#
# m.group(0)
# 'def'


'''
# используй *args!!
reg_buttons = [
    {"%": [add_point, 0], "CE": [clear_terminal], "C": [clear_terminal], "<": [add_point, 2]},
    {"1/x": [add_point, 0], "x^2": [add_point, 1], "x^0.5": [add_point, 2], "/": [add_point, 2]},
    {"7": [ins_terminal, 7], "8": [ins_terminal, 8], "9": [ins_terminal, 9], "*": [add_point, 2]},
    {"4": [ins_terminal, 4], "5": [ins_terminal, 5], "6": [ins_terminal, 6], "-": [add_point, 2]},
    {"1": [ins_terminal, 1], "2": [ins_terminal, 2], "3": [ins_terminal, 3], "+": [add_point, 2]},
    {"+-": [add_point, 0], "0": [ins_terminal, 0], ",": [add_point, 2], "=": [add_point, 2]}
]
for i in range(len(reg_buttons)):
    j = 0
    for k in reg_buttons[i]:
        func_list = reg_buttons[i].get(k)
        butt = tk.Button(master=buttons_pad, text=k, relief=tk.RAISED)
        # func_to_call = func_list[0]
        if len(func_list) > 1:
            butt.bind("<Button-1>", make_lambda(func_list[0], func_list[1]))
        else:
            butt.bind("<Button-1>", make_lambda(func_list[0]))
        butt.grid(row=i + 1, column=j + 1)
        j += 1
'''
