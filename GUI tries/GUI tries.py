import tkinter as tk


def add_point(event):
    print(".")


def clear_terminal():
    entry.delete(0, tk.END)


def ins_terminal(x):
    entry.insert(tk.END, x)


main_memory = 0  # главная переменная
temp_memory = 0
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
entry = tk.Entry(master=terminal, width=50)  # 50 symb is less than 320 px
entry.pack()
terminal.pack()
entry.focus_set()

ctrl_pad = tk.Frame(master=root)
for i in buttons:
    j = tk.Button(text=i)
    j.pack(side=tk.LEFT)
ctrl_pad.pack()

buttons_pad = tk.Frame(master=root)
# code

# используй *args!!
reg_buttons = [
    {"%": [add_point, 0], "CE": clear_terminal(), "C": clear_terminal(), "<": [add_point, 2]},
    {"1/x": [add_point, 0], "x^2": [add_point, 1], "x^0.5": [add_point, 2], "/": [add_point, 2]},
    {"7": ins_terminal(7), "8": ins_terminal(8), "9": ins_terminal(7), "*": [add_point, 2]},
    {"4": ins_terminal(4), "5": ins_terminal(5), "6": ins_terminal(6), "-": [add_point, 2]},
    {"1": ins_terminal(1), "2": ins_terminal(2), "3": ins_terminal(3), "+": [add_point, 2]},
    {"+-": [add_point, 0], "0": ins_terminal(0), ",": [add_point, 2], "=": [add_point, 2]}
]
for i in range(len(reg_buttons)):
    j = 0
    for k in reg_buttons[i]:
        butt = tk.Button(master=buttons_pad, text=k, relief=tk.RAISED)
        butt.bind("<Button-1>", reg_buttons[i].get(k))
        butt.grid(row=i+1, column=j+1)
        j += 1


# If you would like to make it half the size of the window, use width=root.winfo_width / 2,
# height=winfo_height In the maximum size.
buttons_pad.pack()


# button1 = tk.Button(text="Нажать!", width=10, height=2)
# button1.pack()
# button2 = tk.Button(text="Не нажимать!", width=10, height=2)
# button2.pack()

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
