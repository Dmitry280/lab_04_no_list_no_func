""" Лабораторная работа №4: программа для заданных по варианту функций
выводит таблицу значений этих функций на некотором отрезке и строит график одной из них.
Автор: Дурбале Д.А. ИУ7-31БВ
Вариант №30:
𝑔1 = 𝑎^3−23.8𝑎^2+44.9𝑎−10.34
𝑔2 = 𝑎𝑙𝑛𝑎 − 6
𝑔3 = sqrt(|𝑔1𝑔2|)
𝑎0 = 1.2    h = 0.2  𝑎𝑛 = 6
Оператор: for
Использование пользовательских функций и списков запрещено
Дополнительное задание:
1) определить значение 𝑔1𝑚𝑎𝑥 − 𝑔2𝑚𝑎𝑥.
"""

from math import pow, sqrt, log

# блок ввода
a0 = float(input("Input a0 value: "))
an = float(input("Input an value: "))
h = abs(float(input("Input h (step) value: ")))
while h > an - a0:
    h = abs(float(input(f"Input correct value of h (step) less, than {an - a0:.2g}: ")))

count = round(abs(an - a0) / h)  # вычисляем количество строк в таблице

i = 0
g1 = 0
g2 = 0
g3 = 0
g = 4  # число знаков после запятой
a = a0
# вычисляем максимальную ширину столбца
max_a_width = 0
max_g1_width = 0
max_g2_width = 0
max_g3_width = 0
cycle_count = 0
for i in range(0, count + 1, 1):
    g1 = pow(a, 3) - 23.8 * pow(a, 2) + 44.9 * a - 10.34
    if a < 0 or a == 0:
        g2 = "Not defined"
    else:
        g2 = (a * log(a)) - 6
    if g2 != "Not defined":
        g3 = sqrt(abs(g1 * g2))
    else:
        g3 = "Not defined"
    if len(str(round(a, g))) > max_a_width:
        max_a_width = len(str(round(a, g)))

    if len(str(round(g1, g))) > max_g1_width:
        max_g1_width = len(str(round(g1, g)))

    if g2 != "Not defined":
        if len(str(round(g2, g))) > max_g2_width:
            max_g2_width = len(str(round(g2, g)))

        if len(str(round(g3, g))) > max_g3_width:
            max_g3_width = len(str(round(g3, g)))
    if g2 == "Not defined":
        max_g2_width = len("Not defined")
        max_g3_width = len("Not defined")
    a += h

# блок вывода
# выводим шапку таблицы
print("+", max_a_width * '-',
      "+", max_g1_width * '-',
      "+", max_g2_width * '-',
      "+", max_g3_width * '-',
      "+", sep='-')
print('|', 'a:'.center(max_a_width),  # выравнивание по центру самой широкой ячейки
      '|', 'g1:'.center(max_g1_width),
      '|', 'g2:'.center(max_g2_width),
      '|', 'g3:'.center(max_g3_width), '|',
      sep=' ')
# выводим тело таблицы
a = a0
for i in range(0, count + 1, 1):
    g1 = pow(a, 3) - 23.8 * pow(a, 2) + 44.9 * a - 10.34
    if a <= 0:
        g2 = "Not defined"
    else:
        g2 = (a * log(a)) - 6
    if g2 != "Not defined":
        g3 = sqrt(abs(g1 * g2))
    else:
        g3 = "Not defined"
    if g2 != "Not defined":
        print("+", f"{max_a_width * '-'}",
              "+", f"{max_g1_width * '-'}",
              "+", f"{max_g2_width * '-'}",
              "+", f"{max_g3_width * '-'}",
              "+", sep='-')
        print('|', f"{a:.4g}".center(max_a_width),
              '|', f"{g1:.4g}".center(max_g1_width),
              '|', f"{g2:.4g}".center(max_g2_width),
              '|', f"{g3:.4g}".center(max_g3_width),
              '|')
    else:
        print("+", f"{max_a_width * '-'}",
              "+", f"{max_g1_width * '-'}",
              "+", f"{max_g2_width * '-'}",
              "+", f"{max_g3_width * '-'}",
              "+", sep='-')
        print('|', f"{a:.4g}".center(max_a_width),
              '|', f"{g1:4g}".center(max_g1_width),
              '|', g2.center(max_g2_width),
              '|', g3.center(max_g3_width),
              '|')
    a += h

print("+", f"{max_a_width * '-'}",
      "+", f"{max_g1_width * '-'}",
      "+", f"{max_g2_width * '-'}",
      "+", f"{max_g3_width * '-'}",
      "+", sep='-')

# print("Cycles done: ", cycle_count)

# строим график:
# запрашиваем у пользователя количество засечек на оси g1
marker_count = input("Input the number of marks on g1 axis (4-8): ")
markers_lst = ['4', '5', '6', '7', '8']

# проверяем на корректность введенное количество засечек
while marker_count not in markers_lst:
    marker_count = input("The number of marks should be an integer between 4 and 8: ")
# запрашиваем у пользователя масштаб графика
scale = int(input("Input the graph area scale (width): "))
print()
print("The g1 graph is:".upper().center(scale))
print()
# рассчитываем среднюю длину подписи засечки

# рассчитываем шаг между засечками

g1_min = 0
g1_max = 0
g1_count = 0
a = a0
for i in range(0, count + 1, 1):  # определяем начальное и конечное значение строки засечек
    g1 = pow(a, 3) - 23.8 * pow(a, 2) + 44.9 * a - 10.34
    if g1 < g1_min:
        g1_min = g1
    if g1 > g1_max:
        g1_max = g1
    a += h
    g1_count += 1
# определяем шаг значений засечек
step_len = (g1_max - g1_min) / (int(marker_count) - 1)
dpi = scale / abs(g1_min - g1_max)
# определяем среднюю длину значения засечки
marker_len_sum = 0
marker_len_avg = 0
g1 = g1_min
m_count = 0
for i in range(1, int(marker_count) + 1, 1):
    if abs(round(g1)) < 1000:
        marker_len_sum = marker_len_sum + len(str(round(g1, 2)))
        m_count += 1
        marker_len_avg = round((marker_len_sum / m_count), 4)
        g1 += step_len
    else:
        marker_len_sum = marker_len_sum + len(str(f"{g1:.2e}"))
        m_count += 1
        marker_len_avg = round((marker_len_sum / m_count), 4)
        g1 += step_len
g1 = g1_min
g1_mark_str = ''
max_g1_width = int(scale / (max_g1_width-1))
c = round(scale / (int(marker_count) - 1) - marker_len_avg)
print("c is: ", c)
for i in range(1, int(marker_count) + 1, 1):
    if abs(round(g1)) < 1000:
        g1_mark_str = g1_mark_str + str(round(g1, 2)) + abs(c) * ' '  # формируем строку с засечками
        g1 += step_len
    else:
        g1 = str(f"{g1:.2e}")
        g1_mark_str = g1_mark_str + g1 + abs(c) * ' '  # формируем строку с засечками
        g1 = float(g1)
        g1 += step_len
print((max_a_width + 1) * ' ', g1_mark_str, sep=' ')
print('0'.center(max_a_width + 1), round(marker_len_avg / 2 - 2) * ' ', scale * '-', '>', "g1 axis", sep=' ')

# выводим построчно ось "а" и сам график
a = a0
g1_min = round(g1_min * dpi)
g1_max = round(g1_max * dpi)
for i in range(0, count + 1, 1):
    g1 = pow(a, 3) - 23.8 * pow(a, 2) + 44.9 * a - 10.34
    g1 = round(g1 * dpi)
    if g1 < 0:
        print(f"{round(a, 2)}".center(max_a_width + 1),  # вывод значения аргумента
              round(marker_len_avg / 2) * ' ',
              (abs(g1_min) - abs(g1)) * ' ',
              '*',  # маркер графика
              (abs(g1) - 1) * ' ',
              '|',  # маркер оси
              sep='')

    if g1 > 0:
        print(f"{round(a, 2)}".center(max_a_width + 1),  # вывод значения аргумента
              round(marker_len_avg / 2) * ' ',
              abs(g1_min) * ' ',
              '|',  # маркер оси
              (g1 - 1) * ' ',  # смещение от значения "а" до звездочки
              '*',  # маркер графика
              sep='')
        # i += 1
    a += h
# выводим название оси "а"
print((max_a_width + 1) * ' ', round(marker_len_avg / 2) * ' ', abs(g1_min) * ' ', 'v', sep='')
print((max_a_width + 1) * ' ', round(marker_len_avg / 2) * ' ', abs(g1_min) * ' ', 'a axis', sep='')
