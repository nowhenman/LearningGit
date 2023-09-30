import tkinter as tk
from Calc_logic import *


def add_point(event, symb):
    pass


'''
def clear_terminal(event):
    # print('clear')
    entry.delete(0, tk.END)
    # память!
'''

'''
def ins_terminal(event, x):
    # print('ins_terminal', x)
    entry.insert(tk.END, x)
    # данные > память > терминал
'''


def make_lambda(func, *args):
    return lambda ev: func(ev, args[0]) if len(args) > 0 else func(ev)
# ?


# при нажатии числа (0-9) main_memory *= 10 + число
# при нажатии стрелки влево main_memory = main_memory // 10 # todo # проверить тот ли операнд (floor или прочее)
# при нажатии - main_memory копируется в temp_memory, main_memory заменяется на то, что вводится, при наж. = считается
# при нажатии + main_memory копируется в temp_memory, main_memory заменяется на то, что вводится, при наж. = считается
# при нажатии * main_memory копируется в temp_memory, main_memory заменяется на то, что вводится, при наж. = считается
# при нажатии / main_memory копируется в temp_memory, main_memory заменяется на то, что вводится, при наж. = считается

# TRY EXCEPT CUSTOM EXC. ZERODIVISIONERROR!
# при нажатии корень из 2 main_memory = main_memory ** 0.5
# при нажатии ** 2 main_memory = main_memory ** 2
# при нажатии C или CE main_memory = 0 и temp_memory = 0
# при нажатии % -- понятия не имею что это вообще # todo
# при нажатии +- main_memory заменяется с + на - и vice versa
# при нажатии . temp_memory = main_memory, main_memory = ????????????????? # todo
# chislo = float(chislo)
# если ,0 то (где?? -- при обновлении Entry!!) убираем
# при нажатии 1/x надо main_memory = 1/ main_memory


# после процесса все фигачится в терминал!

buttons = {"m_clear": [add_point, 0], "m_add": [add_point, 1], "m_retr": [add_point, 2]}
# словарь из кнопок и их функций


root = tk.Tk()
root.title("Calculator")

menu_bar = tk.Frame(master=root)
menu = tk.Button(master=menu_bar, text="M", width=4, height=1)
menu.pack(side=tk.LEFT)
mode = tk.Label(master=menu_bar, text="Обычный")
mode.pack(side=tk.LEFT)
history = tk.Button(master=menu_bar, text="His", width=4, height=1)
history.pack(side=tk.RIGHT)
menu_bar.pack(fill=tk.X)

terminal = tk.Frame(master=root)
previous = tk.Label(master=terminal, width=43, relief='solid', borderwidth=1, text=temp_memory, anchor='e')
previous.pack()
entry = tk.Entry(master=terminal, width=50, justify='right')  # 50 symb is less than 320 px
entry.pack()
terminal.pack()
entry.focus_set()[]

ctrl_pad = tk.Frame(master=root)
for i in buttons:
    j = tk.Button(text=i)
    j.pack(side=tk.LEFT)
ctrl_pad.pack()

buttons_pad = tk.Frame(master=root)
# code

# используй *args!!
reg_buttons = [
    {"%": [percent], "CE": [ce], "C": [c], "<": [backspace]},
    {"1/x": [one_of_x], "x^2": [x_squared], "x^0.5": [sq_root], "/": [basics, '/']},
    {"7": [number, '7'], "8": [number, '8'], "9": [number, '9'], "*": [basics, '*']},
    {"4": [number, '4'], "5": [number, '5'], "6": [number, '6'], "-": [basics, '-']},
    {"1": [number, '1'], "2": [number, '2'], "3": [number, '3'], "+": [basics, '+']},
    {"+-": [plus_minus], "0": [number, '0'], ",": [point], "=": [equals]}
]
for i in range(len(reg_buttons)):
    j = 0
    for k in reg_buttons[i]:
        func_list = reg_buttons[i].get(k)
        butt = tk.Button(master=buttons_pad, text=k, relief=tk.RAISED, width=10, height=2)
        # func_to_call = func_list[0]
        if len(func_list) > 1:
            butt.bind("<Button-1>", make_lambda(func_list[0], func_list[1]))
        else:
            butt.bind("<Button-1>", make_lambda(func_list[0]))
        butt.grid(row=i + 1, column=j + 1)
        j += 1

# If you would like to make it half the size of the window, use width=root.winfo_width / 2,
# height=winfo_height In the maximum size.
buttons_pad.pack()

# button1.bind("<Button-1>", add_point)
# button2.bind("<Button-1>", add_point)


root.minsize(320, 500)
root.configure(bg='azure2')
root.mainloop()

# максимум 16 символов в поле
# при нажатии на 0-9 проверяем общую длину поля

# регистр общ. переменной влево в 10 раз + кнопка
# и вывод всего этого безобразия в поле

# (16 символов норм, если 17 то научная) умножение сложение
