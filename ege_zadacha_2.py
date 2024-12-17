# Решение (программное) задачи 2 ЕГЭ Информатика 2025
# Миша заполнял таблицу истинности логической функции F (x /\ ¬y) \/ (y ≡ z) \/ ¬ w,
# но успел заполнить лишь фрагмент из трёх различных её строк, даже не указав,
# какому столбцу таблицы соответствует каждая из переменных w, x, y, z
# Определите, какому столбцу таблицы соответствует каждая из переменных w, x, y, z.
# В ответе запишите буквы w, x, y, z в том порядке, в котором идут соответствующие им столбцы (сначала буква, соответствующая первому
# столбцу; затем буква, соответствующая второму столбцу и т.д.). Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.
# -------------------------------
# |  ?  |  ?  |  ?  |  ?  |  F  |
# -------------------------------
# |     |     |  0  |  0  |  0  |
# -------------------------------
# |  1  |  0  |     |  0  |  0  |
# -------------------------------
# |  1  |  0  |  1  |     |  0  |
# -------------------------------

# определим функцию для вычисления значения функции
def f(x, y, z, w):
    return (x and not y) or (y == z) or not w

from itertools import *

# перебор всех пробелов
for a1, a2, a3, a4 in product([0, 1], repeat=4):
    # все наборы
    t = [(a1,a2,0,0),(1,0,a3,0),(1,0,1,a4)]

    # проверка различности всех наборов
    if len(set(t)) != len(t):
        continue

    # перебор всех перестановок имен столбцов
    for p in permutations('xyzw'):
        # проверка на совпадение результата
        if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:  # здесь [0,0,0] - это значения функции из столбца F
            print(*p, sep='')