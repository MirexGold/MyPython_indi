# from math import sqrt
# a, b = int(input()), int(input())
# print(a + b)  # сумму чисел a и b;
# print(a - b)  # разность чисел a и b;
# print(a * b)  # произведение чисел a и b;
# print(a / b)  # частное чисел a и b;
# print(a // b)  # целую часть от деления числа a на b;
# print(a % b)  # остаток от деления числа a на b;
# print(sqrt(a**10 + b**10))  # корень квадратный из суммы их 10-х степеней: sqrt{a^{10} + b^{10}}

# Индекс массы тела
# def my_imt(m, r):
#     imt = m / (r * r)
#     if 18.5 <= imt <= 25:
#         return "Оптимальная масса"
#     elif imt < 18.5:
#         return "Недостаточная масса"
#     elif imt > 25:
#         return "Избыточная масса"
#
#
# m = float(input())
# r = float(input())
#
# print(my_imt(m, r))


# Стоимость строки
# def coast(text):
#     rub = len(text) * 0.6
#     kop = len(text) * 60 % 100
#     return f'{int(rub)} р. {kop} коп.'
#
# stroka = input()
# print(coast(stroka))


# string = input()
# price = 60 * len(string)
#
# print(f'{price // 100} р. {price % 100} коп.')


##Количество слов
# print(len(list(input().split())))

# Зодиак
# sp = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц',
#       'Дракон']
# print(sp[(int(input())-8) % 12])
#
#
# # 8,9,10,11,0,1,2,3,4,5,6,7  - %
# #
# # 0,1,2,3,4,5,6,7,8,9,10,11

# Переворот числа
# a = input()
# if len(a) == 5:
#       print(int(a[::-1]))
# elif len(a) == 6:
#       print(int(a[0]+a[-1:0:-1]))


# Standard American Convention
# print(f"{int(input()):,}")


# Задача Иосифа Флавия 🌶️🌶️
# n, k = int(input()), int(input())
# counter = 0
# for i in range(1, n + 1):
#     counter = (counter + k) % i
# print(counter + 1)


# Координатные четверти
# n = int(input())
# counter1 = counter2 = counter3 = counter4 = 0
# for i in range(n):
#     x, y = map(int, input().split())
#     if x > 0 and y > 0:
#         counter1 += 1
#     elif x < 0 and y > 0:
#         counter2 += 1
#     elif x < 0 and y < 0:
#         counter3 += 1
#     elif x > 0 and y < 0:
#         counter4 += 1
# print(f'Первая четверть: {counter1}')
# print(f'Вторая четверть: {counter2}')
# print(f'Третья четверть: {counter3}')
# print(f'Четвертая четверть: {counter4}')

# Больше предыдущего
# s = list(map(int, input().split()))
# counter = 0
# for i in range(len(s)-1):
#     if s[i+1] > s[i]:
#         counter += 1
# print(counter)


# Назад, вперёд и наоборот
# s = input().split()
# for i in range(0, len(s)-1, 2):
#     s[i], s[i+1] = s[i+1], s[i]
# print(*s, end=' ')

# Сдвиг в развитии
# s = input().split()
# s.insert(0, s[-1])
# del s[-1]
# print(*s)

# Различные элементы
# s = input().split()
# s1 = []
# for i in s:
#     if i not in s1:
#         s1.append(i)
# print(len(s1))

# Произведение чисел
# l = [int(input()) for n in range(int(input()))]
# n = int(input())
# fl = False
#
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] * l[j] == n:
#             fl = True
#             break
#
# print('ДА' if fl == True else 'НЕТ')

# Камень, ножницы, бумага
# t, r = input(), input()
# if t == r:
#     print('ничья')
# elif t == 'камень' and r == 'ножницы' or t == 'ножницы' and r == 'бумага' or t == 'бумага' and r == 'камень':
#     print('Тимур')
# else:
#     print('Руслан')


# Камень, ножницы, бумага, ящерица, Спок 🌶️
# timur = input()
# ruslan = input()
# result = {'камень': ['ножницы', 'ящерица'],
#           'ножницы': ['бумага', 'ящерица'],
#           'бумага': ['камень', 'Спок'],
#           'Спок': ['ножницы', 'камень'],
#           'ящерица': ['бумага', 'Спок']}
# if timur == ruslan:
#     print('ничья')
# else:
#     if ruslan in result[timur]:
#         print('Тимур')
#     else:
#         print('Руслан')

# Орел и решка
# stroka = input().split('О')
# res = max(stroka, key=len)
# print(len(res))

# Кремниевая долина 🌶️🌶️
# for i in range(int(input())):
#     s, virus, x  = input(), 'anton', 0
#     for sym in s:
#         if sym == virus[x]:
#             x += 1
#         if x == 5:
#             print(i + 1, end=' ')
#             break


# Роскомнадзор запретил букву а 🌶️🌶️
# word = input() + ' запретил букву'
# alpha = [chr(i) for i in range(1072, 1104)]
#
# for letter in alpha:
#     if letter in word:
#         print(word, letter)
#         word = word.replace(letter, '').replace('  ', ' ').strip()

# Предикат делимости
# объявление функции
# def func(num1, num2):
#     if num1 % num2 == 0:
#         return True
#
# # считываем данные
# num1, num2 = int(input()), int(input())
#
# # вызываем функцию
# if func(num1, num2):
#     print('делится')
# else:
#     print('не делится')

'''
метод append() добавляет новый элемент в конец списка.
метод extend() расширяет один список другим списком.
метод insert() вставляет значение в список в заданной позиции.
метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению.
метод remove() удаляет первый элемент, значение которого равняется переданному в метод значению.
метод pop() удаляет элемент по указанному индексу и возвращает его.
метод count() возвращает количество элементов в списке, значения которых равны переданному в метод значению.
метод reverse() инвертирует порядок следования значений в списке, то есть меняет его на противоположный.
метод copy() создает поверхностную копию списка.
метод clear() удаляет все элементы из списка.
оператор del позволяет удалять элементы списка по определенному индексу.
Примечание 2. Методы строк, работающие со списками:
метод split() разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов,
символ табуляции (\t) или символ новой строки (\n).
метод join() собирает строку из элементов списка, используя в качестве разделителя строку,
к которой применяется метод.
'''

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# # print(list1)  #-> [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)   #->['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in list1:
#     if max(i) > maximum:
#         maximum = max(i)
# print(maximum)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in list1:
#     i.reverse()
#
# print(list1)  #->[[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in list1:
#     total += sum(i)
#     counter += len(i)
#
#
# print(total)
# print(counter)
# print(total/counter)


# n, m = int(input()), int(input())    # считываем значения n и m
# my_list = [[0] * m for _ in range(n)]
# print(my_list)

# Считывание вложенных списков
# n = 4                                          # количество строк (элементов)
# my_list = []
#
# for _ in range(n):
#     elem = [int(i) for i in input().split()]   # создаем список из элементов строки
#     my_list.append(elem)

# Перебор и вывод элементов вложенного списка
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[i][j], end=' ')   # используем необязательный параметр end
#     print()                             # перенос на новую строку


# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in my_list:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
#     print()


# Обработка вложенных списков
# по индексу
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
# total = 0
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         total += my_list[i][j]
# print(total)

# по значениям
# my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]
# total = 0
# for row in my_list:
#     for elem in row:
#         total += elem
# print(total)


# n = 3
# list1 = []
# for _ in range(n):
#     row = input().split()
#     list1.extend(row)
# print(list1)   #-> ['9', '7', '6', '2', '1', '3', '4', '45', '67']


# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     if max(row) > maximum:
#         maximum = max(row)
#     if min(row) < minimum:
#         minimum = min(row)
#
# print(maximum + minimum)


# Список по образцу 1
# n = int(input())
# matrix = [[i for i in range(1, n + 1)] for j in range(1, n + 1)]
# print(*matrix, sep='\n')

# n = int(input())
# matrix = []
# for i in range(1, n + 1):
#    matrix.append(i)
# for j in range(1, n + 1):
#    print(matrix)

# Список по образцу 2
# n = int(input())
# matrix = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
# print(*matrix, sep='\n')

# n = int(input())
# matrix = []
# for i in range(1, n + 1):
#     matrix.append(i)
#     print(matrix)

# Треугольник Паскаля 1 🌶️
# n = int(input())
#
# li = [1]
# for i in range(n):
#     for j in range(len(li) - 1):
#         li[j] = li[j] + li[j + 1]
#     li.insert(0, 1)
#
# print(li)
#
# from math import factorial
# n = int(input())
# b = []
# for i in range(n+1):
#     b.append (int((factorial(n))/(factorial(i)*factorial(n-i))))
# print(b)


# a = [1]
# for i in range(int(input())):
#     a = [x + y for x, y in zip([*a, 0], [0, *a])]
# print(a)

# Треугольник Паскаля 2
# n = int(input())
# P=[]
# for i in range(0,n):
#     row=[1]*(i+1)
#     for j in range(i+1):
#         if j!=0 and j!=i:
#             row[j]=P[i-1][j-1]+P[i-1][j]
#     P.append(row)
#
# for r in P:
#     print(*r)

# # -------------------ФУНКЦИЯ-------------------
# def pascal(n):
#     triangle = [[1]]
#
#     for i in range(n - 1):
#         row = [1]
#         for j in range(1, len(triangle[i])):
#             row += [sum(triangle[i][j - 1: j + 1])]
#         row += [1]
#         triangle.append(row.copy())
#
#     return triangle
#
#
# # --------------------ВЫЗОВ--------------------
# [print(*row) for row in pascal(int(input()))]


# Упаковка дубликатов 🌶️
# res = []
# for el in input().split():
#     if res and el in res[-1]:
#         res[-1].append(el)
#     else:
#         res.append([el])
# print(res)
#
# #Разбиение на чанки 🌶️
# def chunked(st, n):
#     st = st.split()
#     a = [[] for _ in range(0, len(st), n)]
#     for i in range(len(a)):
#         a[i].extend(st[:n])
#         st = st[n:]
#     return a
#
# string = input()
# num = int(input())
#
# print(chunked(string, num))

# Подсписки списка 🌶️🌶️
# n = input().split()
# sp = [[]]
# k = 1
# while k != len(n) + 1:
#     for j in range(len(n)):
#         if len(n[j:j + k]) == k:
#             sp.append(n[j:j + k])
#     k += 1
# print(sp)

# ///////////////////////////////////////////////////////////
# 4.4 Матрицы. Часть 1
##матрицу можно создать с помощью генератора:
# [[input() for _ in range(m)] for _ in range(n)]


# matrix  = [[2, -5, -11, 0],
#            [-9, 4, 6, 13],
#            [4, 7, 12, -2]]
#
# print(matrix[1][2])  # вывод элемента на позиции (2, 3)  -->6

# Перебор элементов матрицы

# перебирая по строкам:
# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()

# перебирая по столбцам
# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
# for c in range(cols):
#     for r in range(rows):
#         print(matrix[r][c], end=' ')
#     print()

# Функции ljust() и rjust()

# Строковый метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста.
# print('a'.ljust(3))
# print('ab'.ljust(3))
# print('abc'.ljust(3))

# Строковый метод ljust() использует вместо пробела другой символ, если передать ему второй аргумент,
# необязательный.
# print('a'.ljust(5, '*'))
# print('ab'.ljust(5, '$'))
# print('abc'.ljust(5, '#'))


# Строковый метод rjust() выравнивает текст по ширине, добавляя пробелы в начало текста.
# print('a'.rjust(3))
# print('ab'.rjust(3))
# print('abc'.rjust(3))

# Строковый метод rjust() использует вместо пробела другой символ,
# если передать ему второй аргумент, необязательный.
# print('a'.rjust(5, '*'))
# print('ab'.rjust(5, '$'))
# print('abc'.rjust(5, '#'))


# Применив метод ljust() для выравнивания столбцов при выводе таблицы мы получим
# rows, cols = 3, 4                # rows - количество строк, cols - количество столбцов
# matrix  = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]
# for r in range(rows):
#     for c in range(cols):
#         print(str(matrix[r][c]).ljust(8), end='')
#     print()

# Элементы с равными индексами i == j находятся на главной диагонали. Такие элементы обозначаются matrix[i][i].
# Элементы с индексами i и j, связанными соотношением i + j + 1 = n (или j = n - i - 1), где n — размерность матрицы,
# находятся на побочной диагонали.

# n = 8
# matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
# for i in range(n):             # заполняем главную диагональ единицами, а побочную двойками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 2
# for r in range(n):             # выводим матрицу
#     for c in range(n):
#         print(matrix[r][c], end=' ')
#     print()

# Индексы i и j элементов на главной диагонали связаны соотношением i = j. Индексы i и jэлементов на
# побочной диагонали связанны соотношением i + j + 1 = n (или  j = n - i - 1), где n — размерность матрицы


## Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
#
## Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)


# n = 3
# a = [[1, 2, 3],             #->  9 8 7
#      [4, 5, 6],             #->  6 5 4
#      [7, 8, 9]]             #->  3 2 1
#
# for i in range(n):
#     for j in range(n):
#         print(a[n - i - 1][n - j - 1], end=' ')
#     print()


# считаем максимальное значение главной диагонали  и минимальной  значение побочной диагонали
# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]
#
# maximum = -1
# minimum = 100
#
# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]
# print(minimum + maximum)   #-->101

# ----------------------------------
# создания матрицы
# ----------------------------------

# N = int(input())
# M = int(input())
# matrix = [[0] * M for i in range(N)]
#
# # Заполнение матрицы произвольными значениями
# for i in range(N):
#     for j in range(M):
#         matrix[i][j] = input()
#
# # вывести матрицу на экран построчно
# for i in range(len(matrix)):  # len(A) - возвращает количество строк в матрице А
#     for j in range(len(matrix[i])):  # len(A[i]) - возвращает количество элементов в строке i
#         print(matrix[i][j], end=' ')
#     print()

# ----------------------------------
# ----------------------------------

# Вывести матрицу 1
# n, m = int(input()), int(input())
# matrix = [[0] * m for i in range(n)]
#
# # Заполнение матрицы
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = input()
#
# # вывести матрицу на экран построчно
# for i in range(len(matrix)):  # возвращает количество строк в матрице
#     for j in range(len(matrix[i])):  # возвращает количество элементов в строке i
#         print(matrix[i][j], end=' ')
#     print()

# # ------------------------------------
# n, m = int(input()), int(input())
# [print(*[input() for i in range(m)]) for i in range(n)]
# # -------------------------------------
# # -------------------------------------
# def input_matrix(rows, cols):
#     matrix = [[input() for _ in range(cols)] for _ in range(rows)]
#     return matrix
#
# def print_matrix(matrix):
#     for r in range(len(matrix)):
#         print(*matrix[r])
#     return None
#
# n, m = int(input()), int(input())
# print_matrix(input_matrix(n, m))
# # -------------------------------------
# # -------------------------------------
# Вывести матрицу 2
# rows, cols = int(input()), int(input())  # rows - количество строк, cols - количество столбцов
# matrix = [[0] * cols for i in range(rows)]
#
# for i in range(rows):
#     for j in range(cols):
#         matrix[i][j] = input()
#
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=' ')
#     print()
# print()
#
# for j in range(cols):
#     for i in range(rows):
#         print(matrix[i][j], end=' ')
#     print()
# -----------------------
# def print_matrix(matrix, rows, cols, width=1):
#     for i in range(rows):
#         for j in range(cols):
#             print(matrix[i][j].ljust(width), end=' ')
#         print()
#
#
# def print_transposed_matrix(matrix, rows, cols, width=1):
#     for j in range(cols):
#         for i in range(rows):
#             print(matrix[i][j].ljust(width), end=' ')
#         print()
#
#
# n, m = int(input()), int(input())
# matrix = [[input() for j in range(m)] for i in range(n)]
# print_matrix(matrix, n, m)
# print()
# print_transposed_matrix(matrix, n, m)

##След матрицы
# n = int(input())
# maximum = 0
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     maximum += matrix[i][i]
# print(maximum)


# res = 0
# for i in range(int(input())):
#     res += int(input().split()[i])
# print(res)

# Больше среднего
# n = int(input())
# counter = 0
# matrix = [list(map(int, input().split())) for _ in range(n)]
# for i in matrix:
#     sr = (sum(list(map(int, i)))) / len(i)
#     for j in i:
#         if int(j) > sr:
#             counter += 1
#     print(counter)
#     counter = 0


# Максимальный в области 1
# n = int(input())
# maximum = []
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             maximum.append(matrix[i][j])
# print(max(maximum))


# Максимальный в области 2 🌶️
# n = int(input())
# maximum = []
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if (i >= j and i <= n - 1 -j) or (i <= j and i >= n - 1 -j) or (i == j) or (i + j + 1 == n):
#             maximum.append(matrix[i][j])
# print(max(maximum))

# Суммы четвертей
# n = int(input())
# up = []
# left = []
# down = []
# right = []
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if (i < j and i < n - 1 -j):
#             up.append(matrix[i][j])
#         elif (i > j and i < n - 1 -j):
#             left.append(matrix[i][j])
#         elif (i > j and i > n - 1 -j):
#             down.append(matrix[i][j])
#         elif (i < j and i > n - 1 -j):
#             right.append(matrix[i][j])
# print(f'Верхняя четверть: {sum(up)}')
# print(f'Правая четверть: {sum(right)}')
# print(f'Нижняя четверть: {sum(down)}')
# print(f'Левая четверть: {sum(left)}')


# Таблица умножения
# n, m = int(input()), int(input())
# for i in range(n):
#     mult = []
#     for j in range(m):
#         mult.append(str(i*j).ljust(3))
#     print(*mult)
#
# n, m = int(input()), int(input())
# mult = [[i * j for j in range(m)] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(str(mult[i][j]).ljust(3), end='')
#     print()


# Максимум в таблице
# n, m = int(input()), int(input())
# row, col = 0, 0
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > matrix[row][col]:
#             row, col = i, j
# print(row, col)


# Обмен столбцов
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# a, b = [int(i) for i in input().split()]
#
# for i in range(n):
#     matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
# for i in matrix:
#     print(*i)

# Симметричная матрица
# n = int(input())
# flag = True
# matrix = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[j][i]:
#             flag = False
#     if flag == False:
#         print('NO')
#         break
# else:
#     print('YES')


# Обмен диагоналей
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
#
# for i in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# for row in matrix:
#     print(*row)

#
# # Зеркальное отображение
# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n // 2):
#     matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
# for row in matrix:
#     print(*row)


# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# matrix.reverse()
#
# for row in matrix:
#     print(*row)

# # Поворот матрицы
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
#
# for j in range(n):
#     for i in range(n - 1, -1, -1):
#         print(matrix[i][j], end=' ')
#     print()


# Ходы коня
# col, row = input().strip()
# coor_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# coor_row = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
# arr = [["N" if [i, j] == [coor_row[row], coor_col[col]] else '.' for j in range(8)] for i in range(8)]
# for i in range(8):
#     for j in range(8):
#         if (coor_row[row] - i) * (coor_col[col] - j) in [-2, 2]: arr[i][j] = "*"
# for line in arr:
#     print(*line, sep = ' ')
#
# x, y = input()
# n = 8
# board = [['.'] * n for _ in range(n)]
# x = ord(x) - 97
# y = n - int(y)
# board[y][x] = 'N'
#
# for i in range(n):
#     for j in range(n):
#         if abs(y - i) * abs(x - j) == 2:
#             board[i][j] = '*'
#
# for row in board:
#     print(*row)


# Магический квадрат 🌶️
# n = int(input())
# matrix = [[int(i) for i in input().split()] for j in range(n)]
#
# magic = sum(matrix[0])
# flag = 'YES'
# digits = [i for i in range(1, n ** 2 + 1)]
#
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] in digits:
#             digits.remove(matrix[i][j])
#     if i == n - 1 and j == n - 1 and digits != []:
#         flag = 'NO'
#
# for i in range(n):
#     if sum(matrix[i]) != magic:
#         flag = 'NO'
#         break
#
# for j in range(n):
#     result = 0
#     for i in range(n):
#         result += matrix[i][j]
#         if i == n - 1 and result != magic:
#             flag = 'NO'
#             break
#
# print(flag)

# Шахматная доска
# x, y = [int(i) for i in input().split()]
# matrix = [['.'] * y for _ in range(x)]
#
# for i in range(x):
#     if i == 0 or i % 2 == 0:
#         for j in range(1, y, 2):
#             matrix[i][j] = '*'
#     else:
#         for j in range(0, y, 2):
#             matrix[i][j] = '*'
#
# for row in matrix:
#     print(*row)

# n, m = map(int, input().split())
# for i in range(n):
#     row = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
#     print(*row)

# Побочная диагональ
# n = int(input())
# matrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     matrix[i][n - 1 - i] = 1
#     for j in range(n):
#         if i > n - 1 - j:
#             matrix[i][j] = 2
#         print(matrix[i][j], end=" ")
#     print()

# def matrix(i, j, n):
#     if i == n - j - 1:
#         return 1
#     elif i < n - j - 1:
#         return 0
#     else:
#         return 2
# n = int(input())
# res = [[matrix(i, j, n) for j in range(n)] for i in range(n)]
# for x in res:
#     print(*x)


# Заполнение 1
# n, m = map(int, input().split())
# matrix = []
# counter = 1
#
# for i in range(n):
#     matrix.append([])
#     for j in range(m):
#         matrix[i].append(counter)
#         counter += 1
#
#         print(f'{matrix[i][j]}'.ljust(3), end='')
#     print()

# Заполнение 2
# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for j in range(m):
#     for i in range(n):
#         matrix[i][j] = j * n + i + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# Заполнение 3
# n = int(input())
# matr = [[0] * n for _ in range(n)]
# for i in range(n):
#     matr[i][i] = 1
#     matr[i][n - 1 - i] = 1
# for i in range(n):
#     for j in range(n):
#         print(str(matr[i][j]).ljust(3), end='')
#     print()

# Заполнение 4
# n = int(input())
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if (i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n):
#             matrix[i][j] = 1
#
# for i in range(n):
#     for j in range(n):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# Заполнение 5 🌶️
# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = (i + j) % m + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()


# Заполнение змейкой
# s=input().split()
# n=int(s[0])
# m=int(s[1])
# matrix=[[0 for i in range(m)] for _ in range(n)]
# count =1
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] += count
#         count+=1
# for i in range(n):
#     if i%2==0:
#         print(*matrix[i])
#     else:
#         matrix[i].reverse()
#         print(*matrix[i])


# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1
#     if i % 2:
#         matrix[i].reverse()
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()

# Заполнение диагоналями 🌶️
# n, m = [int(i) for i in input().split()]
# mtx = [[0] * m for _ in range(n)]
# sequence, k = 1, 0
#
# while sequence != n * m + 1:
#     for i in range(n):
#         for j in range(m):
#             if i + j == k:
#                 mtx[i][j] = sequence
#                 sequence += 1
#     k += 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(mtx[i][j]).ljust(3), end='')
#     print()


# n, m = [int(i) for i in input().split()]
#
# matrix = [[1] * m for _ in range(n)]
# row, col, diag = 0, 0, 0
#
# for i in range(1, n * m):
#     col -= 1
#     row += 1
#     if col < 0 or row == n:
#         diag += 1
#         col = diag if diag < m else m - 1
#         row = diag - col
#
#     matrix[row][col] += i
#
# [print(*i) for i in matrix]

# # Принимаем параметры матрицы
# n, m = map(int, input().split())
# # Создаем скелет матрицы
# matrix = [[0] * m for i in range(n)]
# # Задаем отсчет с единицы
# d = 1
#
# for k in range(1, n + m):               # Цикл перебирающий сумму индексов в диагонали
#     for i in range(n):                  # Перебираем строки
#         for j in range(m):              # Перебираем столбцы
#             if i + j + 1 == k:          # Выявляем ячейки, относящиеся к искомой диагонали
#                 matrix[i][j] = d        # Присваиваем обнаруженной ячейке порядковый номер
#                 d += 1                  # Обновляем счетчик
#
# # Распечатываем полученную матрицу
# for row in range(n):
#     for col in range(m):
#         print(str(matrix[row][col]).ljust(3), end=' ')
#     print()


# Заполнение спиралью 😈😈
# n, m = map(int, input().split())
# l = [[0] * m for _ in range(n)]
# num = 1
# k = 0                                 # уровень квадрата: 0 - внешний, 1 - вложенный и т.д.
# product = n * m + 1                   # вынесено в переменную, т.к. n и m меняются в цикле
#
# while num < product:
#     for j in range(k, m):             # верхняя сторона
#         l[k][j] = num
#         num += 1
#     for i in range(k + 1, n):         # правая сторона
#         l[i][j] = num
#         num += 1
#     if num == product:                # костыль для случаев с маленькими n, m
#         break
#     for j in range(m - 2, k - 1, -1): # нижняя сторона
#         l[i][j] = num
#         num += 1
#     for i in range(n - 2, k, -1):     # левая сторона
#         l[i][j] = num
#         num += 1
#     m -= 1                            # изменяю размер сторон для будущего квадрата
#     n -= 1
#     k += 1
#
# for row in l:
#     for el in row:
#         print(str(el).ljust(3), end='')
#     print()


# 4.7 Операции над матрицами в математике
# Сложение матриц
# n, m = [int(i) for i in input().split()]
# matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
# _ = input()
# matrix2 = [[int(i) for i in input().split()] for _ in range(n)]
# matrix3 = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix3[i][j] += matrix1[i][j] + matrix2[i][j]
#
# for row in matrix3:
#     print(*row)

# n, m = [int(x) for x in input().split()]
# A = [[int(x) for x in input().split()] for _ in range(n)]
# input()
# B = [[int(x) for x in input().split()] for _ in range(n)]
# C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
# [print(*i) for i in C]

# Умножение матриц 🌶️
# n, m = [int(x) for x in input().split()]
# matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
# input()
# m, k = [int(x) for x in input().split()]
# matrix2 = [[int(x) for x in input().split()] for _ in range(m)]
# matrix3 = [[0] * k for i in range(n)]
# for i in range(n):
#     for j in range(k):
#         for q in range(m):
#             matrix3[i][j] += matrix1[i][q] * matrix2[q][j]
# [print(*i) for i in matrix3]


# Возведение в степень каждого элемента матрицы
# n = int(input())
# a = [list(map(int, list(input().split()))) for _ in range(n)]
# m = int(input())
#
# def multi(a, b):
#     n = len(a)
#     b = list(zip(*b))
#     return [[sum([a[i][r] * b[j][r] for r in range(n)]) for j in range(n)] for i in range(n)]
#
# def expo(a, m):
#     c = list(a)
#     for _ in range(m-1):
#         c = multi(c, a)
#     return c
#
# result = expo(a, m)
#
# [print(*row) for row in result]

# Каждый n-ый элемент
# s = input().split()
# n = int(input())
# res = []
# for i in range(n):
#     res.append(s[i::n])
# print(res)

# Максимальный в области 2
# n = int(input())
# arr = []
# maximum = 0
# for i in range(n):
#     arr.append([int(elem) for elem in input().split()])
# for i in range(n):
#     for j in range(n):
#         if i >= n - 1 - j and arr[i][j] > maximum:
#             maximum = arr[i][j]
# print(maximum)

#  берем размер матрицы
# n = int(input())
# #  выпиливаем матрицу из входных данных
# matrix = [[int(x) for x in input().split()] for i in range(n)]
# #  вычисляем больший (элемент) из больших (элементов) в бегущем срезе
# answer = max(max(matrix[i][n-i-1:]) for i in range(n))
# #  закидываем результат
# print(answer)

# Транспонирование матрицы
# import numpy as np
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append([int(elem) for elem in input().split()])
# a_t = np.matrix(arr).transpose().tolist()
# for i in range(n):
#     print(*a_t[i])

# n = int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     for j in range(i, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
# for row in matrix:
#     print(*row)


# Снежинка
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append([])
#     for j in range(n):
#         if i == n//2 or j == n//2 or i == j or i == n-j-1:
#             arr[i].append('*')
#         else:
#             arr[i].append('.')
#
# for i in range(n):
#     print(*arr[i])


# Симметричная матрица
# def is_symmetric(arr, n):
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] != arr[n-j-1][n-i-1]:
#                 return 'NO'
#     return 'YES'
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append([int(elem) for elem in input().split()])
#
# print(is_symmetric(arr, n))

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# res = 'YES'
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if arr[i][j] != arr[n - j - 1][n - i - 1]:
#             res = 'NO'
#             break
#     if res == 'NO':
#         break
# print(res)


# Латинский квадрат 🌶️
# import numpy as np
#
# def is_every_digit_in_arr(arr, n):
#     for i in range(1, n + 1):
#         if i not in arr:
#             return False
#     return True
#
# def is_latin_square(arr, n):
#     result = []
#     a_t = np.matrix(arr).transpose().tolist()
#     for i in range(n):
#         arr[i] = sorted(arr[i])
#         if (result != [] and result != arr[i]) or not is_every_digit_in_arr(arr[i], n):
#             return 'NO'
#         result = arr[i]
#     result = []
#     for i in range(n):
#         a_t[i] = sorted(a_t[i])
#         if (result != [] and result != a_t[i]) or not is_every_digit_in_arr(arr[i], n):
#             return 'NO'
#         result = a_t[i]
#
#     return 'YES'
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append([int(elem) for elem in input().split()])
#
# print(is_latin_square(arr, n))

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# numbers = list(range(1, n + 1))
# result = 'YES'
#
# for i in range(n):
#     row_nums = sorted(matrix[i])
#     col_nums = sorted([matrix[j][i] for j in range(n)])
#     if row_nums != numbers or col_nums != numbers:
#         result = 'NO'
#         break
#
# print(result)

# # Ходы ферзя
# slovarx = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
# slovary = {'8':0, '7':1, '6':2, '5':3, '4':4, '3':5, '2':6, '1':7, '0':8}
#
# position = input()
# arr = []
#
# for i in range(8):
#     arr.append([])
#     for j in range(8):
#         if j == slovarx[position[0]] and i == slovary[position[1]]:
#             arr[i].append('Q')
#         elif j == slovarx[position[0]] or i == slovary[position[1]]:
#             arr[i].append('*')
#         elif abs(slovarx[position[0]] - j) == abs(slovary[position[1]] - i):
#             arr[i].append('*')
#         else:
#             arr[i].append('.')
#
# for i in range(8):
#     print(*arr[i])
#
# # Диагонали параллельные главной
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append([])
#     for j in range(n):
#         arr[i].append(abs(i-j))
#
# for i in range(n):
#     print(*arr[i])

# //////////////////////////////  6.1 Введение в кортежи   //////////////////////////////
# Кортежи поддерживают:
# 
# доступ к элементу по индексу (только для получения значений элементов);
# методы, в частности index(), count();
# встроенные функции, в частности len(), sum(), min() и max();
# срезы;
# оператор принадлежности in;
# операторы конкатенации (+) и повторения (*).

# 6 elementov
# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
# print(primes[:6])

# кроме первых двух.
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[2:])


# # кроме последних трех.
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[:-3])

# кроме двух последних и трех первых.
# countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
# print(countries[3:-2])

# # количество элементов кортежа
# countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
# number = len(countries)
# print(number)

# # сумму минимального и максимального элементов кортежа
# numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
# print(min(numbers)+max(numbers))

# # переменная index содержала индекс элемента «Slovenia»
# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
# index = countries.index('Slovenia')
# print(index)


# # number, содержала количество вхождений «Spain»
# countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
# number = countries.count('Spain')
# print(number)


# # чтобы он вывел кортеж:  (1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13)
# numbers1 = (1, 2, 3)
# numbers2 = (6,)
# numbers3 = (7, 8, 9, 10, 11, 12, 13)
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)
#
# city_name = input()
# city_year = int(input())
# city = (city_name, city_year)
# print(city)


# получить список, содержащий только непустые кортежи
# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# # non_empty_tuples = [tuples[2],tuples[3],tuples[5],tuples[6],tuples[9],tuples[10]]
# non_empty_tuples = [i for i in tuples if i]
# print(non_empty_tuples)

# # Дополните приведенный код так, чтобы переменная new_tuples, содержала список кортежей на основе
# # списка tuples с последним элементом каждого кортежа, замененным на численное значение 100.
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# new_tuples = [i[:-1] + (100,) for i in tuples]
# print(new_tuples)


# # вывел список, содержащий средние арифметические значения чисел каждого вложенного кортежа
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# # tupl = []
# # for i in range(len(numbers)):
# #     tupl.append(sum(numbers[i])/len(numbers[i]))
# # print(tupl)
#
# print([sum(i) / len(i) for i in numbers])

# Вершина параболы
# a, b, c = int(input()), int(input()), int(input()),
# print([(- (b / (2 * a))), (((4 * a * c) - b**2)/ (4 * a))])


# Конкурсный отбор
# n = int(input())
# sp = [input().split() for _ in range(n)]
# for i in sp:
#     print(*i)
# print()
# for i in sp:
#     if i[-1] == '5' or i[-1] == '4':
#         print(*i)
# --
# pup = [input() for _ in range(int(input()))]
# print(*pup, sep='\n')
# print()
# [print(x) for x in pup if int(x[-1]) > 3]

# colors = ('red', 'green', 'blue', 'cyan')
# a, b, c, d = colors
# print(a, d)


# 8.3 Введение в множества в Python
# numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
# print(min(numbers)+max(numbers))

#
# numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
# average = sum(numbers)/len(numbers)
#
# print(average)

# Перебор элементов множества
# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
# for num in numbers:
#     print(num)

# можем использовать операцию распаковки множества.
# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
# print(*numbers, sep='\n')

# # Если нужно гарантировать порядок вывода элементов (по возрастанию / убыванию)
# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
# sorted_numbers = sorted(numbers)
# print(*sorted_numbers, sep='\n')

# numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
# sortnumbers = sorted(numbers, reverse=True)
# print(*sortnumbers, sep='\n')


# сумму квадратов
# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
# summa = 0
# for i in numbers:
#     summa += i ** 2
# print(summa)
#
# print(sum([i*i for i in numbers]))


# элементы множества fruits, каждый на отдельной строке, отсортированные по убыванию
# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# print(*sorted(fruits, reverse=True), sep='\n')

# # Количество различных символов
# print(len(set(input())))

# Неповторимые цифры
# s = list(input())
# print('YES' if len(s) == len(set(s)) else 'NO')

# верно ли, что в записи этих двух строк используются все 10 цифр?
# a, b = input(), input()
# print('YES' if len(set(a+b)) == 10 else 'NO')


# # Одинаковые наборы
# # a, b = input(), input()
# print('YES' if set(input()) == set(input()) else 'NO')

# # Верно ли, что для записи всех трех слов был использован один и тот же набор букв?
# s = input().split()
# print(('NO', 'YES')[set(s[0]) == set(s[1]) == set(s[2])])

# 8.5 Методы множеств. Часть 1
# Для добавления нового элемента в множество используется метод add().
# Метод remove() — удаляет элемент из множества с генерацией исключения (ошибки) в случае, если такого элемента нет.
# Метод discard() — удаляет элемент из множества без генерации исключения (ошибки), если элемент отсутствует.
# Метод pop() — удаляет и возвращает 1ый элемент из множества с генерацией исключения (ошибки) при попытке
# удаления из пустого множества.

# numbers = {1, 2, 3, 4, 5}
#
# print('до удаления:', numbers)
# num = numbers.pop()                 # удаляет 1ый элемент множества, возвращая его
# print('удалённый элемент:', num)
# print('после удаления:', numbers)

# Метод clear() удаляет все элементы из множества.

# Уникальные символы 1
# sp = [input().lower() for _ in range(int(input()))]
# for i in sp:
#     print(len(set(i)))
#
# [print(len(set(input().lower()))) for x in range(int(input()))]

# Уникальные символы 2
# sp = [input().lower() for _ in range(int(input()))]
# s = ''.join(sp)
# print(len(set(s)))

# Количество слов в тексте
# words = [word.lower().strip('.,;:-?!') for word in input().split()]
# print(len(set(words)))

# Встречалось ли число раньше?
# t = input().split()
# m = set()
# for i in t:
#     if i.lstrip('0') in m:
#         print('YES')
#     else:
#         m.add(i)
#         print('NO')

# 8.6 Методы множеств. Часть 2
# Объединение множеств: метод union()
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.union(myset2)
# print(myset3)   #->{1, 2, 3, 4, 5, 6, 7, 8}

# Для объединения двух множеств можно также использовать оператор |
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1 | myset2
# print(myset3)

# Пересечение множеств: метод intersection(), можно также использовать оператор &
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.intersection(myset2)
# print(myset3)  #--> {3, 4}

# Разность множеств: метод difference(), можно также использовать оператор -
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.difference(myset2)
# print(myset3)    #-->{1, 2, 5}

# Симметрическая разность: метод symmetric_difference(), можно также использовать оператор ^
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset3 = myset1.symmetric_difference(myset2)
# print(myset3)   # -->{1, 2, 5, 6, 7, 8}


# Методы union(), intersection(), difference(), symmetric_difference() не изменяют исходные множества,
# а возвращают новые. Часто на практике нужно изменять исходные множества. Для таких целей используются
# парные методы update(), intersection_update(), difference_update(), symmetric_difference_update().


# Метод update() изменяет исходное множество по объединению., |=
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.update(myset2)      # изменяем множество myset1
# print(myset1)   # --> {1, 2, 3, 4, 5, 6, 7, 8}

# Метод intersection_update() изменяет исходное множество по пересечению.
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.intersection_update(myset2)      # изменяем множество myset1
# print(myset1)   # --> {3, 4}

# Метод difference_update() изменяет исходное множество по разности.
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.difference_update(myset2)      # изменяем множество myset1
# print(myset1) # -->{1, 2, 5}

# Метод symmetric_difference_update() изменяет исходное множество по симметрической разности.
# myset1 = {1, 2, 3, 4, 5}
# myset2 = {3, 4, 6, 7, 8}
# myset1.symmetric_difference_update(myset2)      # изменяем множество myset1
# print(myset1)   # --> {1, 2, 5, 6, 7, 8}


# mylist = [2021, 2020, 2019, 2018, 2017, 2016]
# mytuple = (2021, 2020, 2016)
# mystr = 'abcd'
# myset = {2009, 2010, 2016}
# print(myset.union(mystr))              # объединяем со строкой
# print(myset.intersection(mylist))      # пересекаем со списком
# print(myset.difference(mytuple))       # находим разность с кортежем


# A | B , A.union(B) - Возвращает множество, являющееся объединением множеств A и B
# A |= B , A.update(B) - Добавляет в множество A все элементы из множества B
# A & B, A.intersection(B) - Возвращает множество, являющееся пересечением множеств A и B
# A &= B, A.intersection_update(B) - Оставляет в множестве A только те элементы, которые есть в множестве B
# A - B , A.difference(B) - Возвращает разность множеств A и B
# A -= B , A.difference_update(B) - Удаляет из множества A все элементы, входящие в B
# A ^ B , A.symmetric_difference(B) - Возвращает симметрическую разность множеств A и B
# A ^= B,  A.symmetric_difference_update(B) - Записывает в A симметрическую разность множеств A и B

# Количество совпадающих
# a = set(list(map(int, input().split())))
# b = set(list(map(int, input().split())))
# print(len(a.intersection(b)))


# # Общие числа
# a = set(list(map(int, input().split())))
# b = set(list(map(int, input().split())))
# print(*sorted(a.intersection(b)))

# Числа первой строки
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# print(*sorted(a - b))

# Общие цифры
# n = int(input())
# numbers = [input() for _ in range(n)]
#
# num_set = set(numbers[0]).intersection(*numbers)
# print(*sorted(num_set))

# 8.7 Методы множеств. Часть 3
# Для определения, является ли одно из множеств подмножеством другого, используется метод issubset()
# также применяются операторы <= (нестрогое подмножество) и < (строгое подмножество).
# set1 = {2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
# print(set1.issubset(set2))    #--> True
# В этом примере set2 содержит все элементы set1. Это означает,
# что set1 – подмножество set2. Это также означает, что set2 – надмножество set1.


# Для определения, является ли одно из множеств надмножеством другого, используется метод issuperset()
# set1 = {'a', 'b', 'c', 'd', 'e'}
# set2 = {'c', 'e'}
# print(set1.issuperset(set2))    #--> True
# В этом примере set1 содержит все элементы set2. Это означает,
# что set1 – надмножество set2. Это также означает, что set2 – подмножество set1.

# Для определения отсутствия общих элементов в множествах используется метод isdisjoint()
# Данный метод возвращает значение True, если множества не имеют общих элементов, и  False, когда
# множества имеют общие элементы.

# set1 <= set2 , set1.issubset(set2) - Возвращает True, если set1 является подмножеством set2
# set1 >= set2 , set1.issuperset(set2) - Возвращает True, если set1 является надмножеством set2
# set1 < set2 - Эквивалентно set1 <= set2 and set1 != set2 (строгое подмножество)
# set1 > set2 - Эквивалентно set1 >= set2 and set1 != set2 (строгое надмножество)


# Одинаковые цифры
# print(("YES", "NO")[set(input()).isdisjoint(input())])

# Все цифры
# print(['NO', 'YES'][set(input()) >= set(input())])

# Урок информатики
# a, b, c = (set(int(i) for i in input().split()) for i in range(3))
# print(*sorted(set(a.intersection(b).difference(c)))[::-1])

# Урок математики
# set1, set2, set3 = [set([int(i) for i in input().split()]) for k in range(3)]
# print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3)))


# Урок физики
# set_1, set_2, set_3 = (set(input().split()) for _ in range(3))
# print(*(sorted(set_3 - (set_1 | set_2), key=int, reverse=True)))

# Урок биологии
# a = set(input().split() + input().split() + input().split())
# b = set(map(str, range(11)))
# print(*sorted(b - a, key=int))

# 8.8 Генераторы множеств и frozenset
# digits = set(input())
# при вводе строки '12345' создает множество символов {'1', '2', '3', '4', '5'},
# а не множество цифр {1, 2, 3, 4, 5}.

# digits = {int(c) for c in input()}
#
# Примеры использования генератора множеств
# 1. Создать множество, заполненное квадратами целых чисел от 0 до 9 можно так:
#
# squares = {i ** 2 for i in range(10)}
# 2. Создать множество, заполненное кубами целых чисел от 10 до 20 можно так:
#
# cubes = {i ** 3 for i in range(10, 21)}
# 3. Создать множество, заполненное символами строки можно так:
#
# chars = {c for c in 'abcdefg'}
#
# В генераторах множеств можно использовать условный оператор. Например, если требуется создать
# множество, заполненное только цифрами некоторой строки, то мы можем написать такой код:
#
# digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}


# получить множество, содержащее первую букву каждого слова (в нижнем регистре) списка words
# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# myset = {int(d) for d in items}
# print(*sorted(myset))
#
#
# получить множество, содержащее первую букву каждого слова (в нижнем регистре) списка words
# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
#          'tangerine', 'Watermelon', 'currant', 'Almond']
# myset = {d[0].lower() for d in words}
# print(*sorted(myset))
#

# получить множество, содержащее уникальные слова (в нижнем регистре) строки sentence
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# myset = {d.lower().strip('.,;:-?!()') for d in sentence.split()}
# print(*sorted(myset))

# получить множество, содержащее уникальные слова строки sentence длиною меньше 4 символов
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# myset = {d.lower().strip('.,:():;!?') for d in sentence.split() if len(d.strip('.,:():;!?')) < 4}
# print(*sorted(myset))

# выбрал из списка files уникальные имена файлов c расширением .png

# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
#          'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
#          'stepik.org', 'kotlin.ko', 'github.git']
# myset = {d.lower() for d in files if d[-3::].lower() == 'png'}
# print(*sorted(myset))

# Frozenset
# Кортеж (тип tuple) – неизменяемая версия списка (тип list), а замороженное множество (тип frozenset) – неизменяемая
# версия обычного множества (тип set).
# myset1 = frozenset({1, 2, 3})                         # на основе множества
# myset2 = frozenset([1, 1, 2, 3, 4, 4, 4, 5, 6, 6])    # на основе списка
# myset3 = frozenset('aabcccddee')                      # на основе строки
#
# print(myset1)
# print(myset2)
# print(myset3)

# Над замороженными множествами можно производить все операции, которые можно производить над обычными множествами:
#
# объединение множеств: метод union() или оператор |;
# пересечение множеств: метод intersection() или оператор &;
# разность множеств: метод difference() или оператор -;
# симметрическая разность множеств: метод symmetric_difference() или оператор ^.
# Приведенный ниже код:
#
# myset1 = frozenset('hello')
# myset2 = frozenset('world')
#
# print(myset1 | myset2)
# print(myset1 & myset2)
# print(myset1 ^ myset2)

# Методы изменяющие множество отсутствуют у замороженных множеств:
# add()
# remove()
# discard()
# pop()
# clear()
# update()
# intersection_update()
# difference_update()
# symmetric_difference_update()


# n = int(input())
# m = int(input())
# k = int(input())
# p = int(input())
#
# print(n+p-m-k)

# arr = [int(elem) for elem in input().split()]
# print(len(arr) - len(set(arr)))

# def is_repeat(arr, n):
#     for i in range(n + 1):
#         s = input()
#         length = len(arr)
#         arr.add(s)
#         if length == len(arr):
#             return 'REPEAT'
#     return 'OK'
#
#
# print(is_repeat(arr, n))


# m = int(input())
# n = int(input())
# library = []
# toRead = []
#
# for i in range(m):
#     library.append(input())
#
# for i in range(n):
#     toRead.append(input())
#
# for elem in toRead:
#     if elem in library:
#         print('YES')
#     else:
#         print('NO')


# arr1 = {int(elem) for elem in input().split()}
# arr2 = {int(elem) for elem in input().split()}
#
# if len(arr1.intersection(arr2)) == 0:
#     print('BAD DAY')
# else:
#     print(*sorted(arr1.intersection(arr2), reverse=True))


# arr1 = {int(elem) for elem in input().split()}
# arr2 = {int(elem) for elem in input().split()}
# if arr1 == arr2:
#     print('YES')
# else:
#     print('NO')


# m = int(input())
# n = int(input())
# maths = set()
# informatics = set()
# for i in range(m):
#     maths.add(input())
# for i in range(n):
#     informatics.add(input())
# print(len(maths.difference(informatics)))


# m = int(input())
# n = int(input())
# maths = set()
# informatics = set()
# for i in range(m):
#     maths.add(input())
# for i in range(n):
#     informatics.add(input())
# if len(maths.symmetric_difference(informatics)) == 0:
#     print('NO')
# else:
#     print(len(maths.symmetric_difference(informatics)))

# ///////////////////////////// 10.1 Введение в словари в Python ////////////////////////////////////
# my_dict = dict{}
# print(my_dict)

# my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3],
#            99.0: {9, 0, 1}}
# print(min(my_dict) + max(my_dict))

# Перебор элементов словаря
# Для вывода ключей словаря каждого на отдельной строке
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key in capitals:
#     print(key)

# Для вывода значений словаря каждого на отдельной строке
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key in capitals:
#     print(capitals[key])

# Для вывода элементов словаря каждого на отдельной строке
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key in capitals:
#     print('Столица', key, '- это', capitals[key])

# Словарный метод keys() возвращает список ключей всех элементов словаря.
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key in capitals.keys():     # итерируем по списку ['Россия', 'Франция', 'Чехия']
#     print(key)

# Словарный метод values() возвращает список значений всех элементов словаря.
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for value in capitals.values():     # итерируем по списку ['Москва', 'Париж', 'Прага']
#     print(value)


# Словарный метод items() возвращает список всех элементов словаря, состоящий из кортежей пар (ключ, значение)
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for item in capitals.items():
#     print(item)


# Используя магию распаковки кортежей, можно писать такой код:
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# for key, value in capitals.items():
#     print(key, '-', value)


# Распаковка ключей словаря
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# print(*capitals, sep='\n')

# Так как словарь состоит из пар, то и отсортировать его можно как по ключам, так и по значениям.
# Сортировка по ключам выполняется с использованием функции sorted().
# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
# for key in sorted(capitals):
#     print(key)

# Для сортировки словаря по значениям можно использовать функцию sorted() вместе с методом items().
# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
# for key, value in sorted(capitals.items(), key = lambda x: x[1]):
#     print(value)

# Проверка наличия ключа в словаре:
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# if 'Россия' in capitals:
#     print('В словаре есть ключ Россия')
#
# Проверка наличия значения в словаре:
# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# if 'Париж' in capitals.values():
#     print('В словаре есть значение Париж')

# вывел имена всех пользователей (в алфавитном порядке), чей номер оканчивается на 88.
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# # sp = []
# # for i in users:
# #     if i['phone'][-1] == '8':
# #         sp.append(i['name'])
# # print(*sorted(sp))
#
# result = [user['name'] for user in users if user['phone'].endswith('8')]
# print(*sorted(result))


# # вывел имена всех пользователей (в алфавитном порядке), у которых нет информации об электронной почте.
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
#
# result = [user['name'] for user in users if len(user) < 3 or user['email'] == '']
# print(*sorted(result))

# Строковое представление
# sp = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
#       '8': 'eight', '9': 'nine'}
# for i in input():
#     print(sp[i], end=' ')


# Информация об учебных курсах
# data = {
#     "CS101": "CS101: 3004, Хайнс, 8:00",
#     "CS102": "CS102: 4501, Альварадо, 9:00",
#     "CS103": "CS103: 6755, Рич, 10:00",
#     "NT110": "NT110: 1244, Берк, 11:00",
#     "CM241": "CM241: 1411, Ли, 13:00"
# }
# print(data[input()])


# Набор сообщений
# d = {".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
#      "A": '2', "B": '22', "C": '222',
#      "D": '3', "E": '33', "F": '333',
#      "G": '4', "H": '44', "I": '444',
#      "J": '5', "K": '55', "L": '555',
#      "M": '6', "N": '66', "O": '666',
#      "P": '7', "Q": '77', "R": '777', "S": '7777',
#      "T": '8', "U": '88', "V": '888',
#      "W": '9', "X": '99', "Y": '999', "Z": '9999',
#      " ": '0', '"':''
#      }
# for i in input().upper():
#     print(d[i], end='')

# Код Морзе
# morze = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
#          'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#          'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
#          '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
#          '9': '----.'}
# for i in input().upper():
#      if i in morze:
#           print(morze[i], end=' ')
# -----------------

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# mydict = dict(zip(letters, morse))
# for i in input().upper():
#      if i in mydict:
#           print(mydict[i], end=' ')


# 10.3 Методы словарей

# метод items() – возвращает словарные пары ключ: значение, как соответствующие им кортежи;
# метод keys() – возвращает список ключей словаря;
# метод values() – возвращает список значений словаря.

# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher'}
# info['name'] = 'Timur'                    # изменяем значение по ключу name
# info['email'] = 'timyr-guev@yandex.ru'    # добавляем в словарь элемент с ключом email
# print(info)

# Решим следующую задачу: пусть задан список чисел numbers , где некоторые числа встречаются неоднократно.
# Нужно узнать, сколько именно раз встречается каждое из чисел.
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
# Первый код, который приходит в голову имеет вид:
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] += 1
# Однако, просто так сделать result[num] += 1 нельзя, так как если ключа num в словаре еще нет,
# то возникнет ошибка KeyError.
#
# Следующий программный код, полностью решает поставленную задачу:
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
# Цикл for перебирает все элементы списка numbers и для каждого проверяет,
# присутствует ли он уже в качестве ключа в словаре result. Если значение отсутствует,
# значит число встретилось впервые и мы инициируем значение result[num] = 1. Если значение
# уже присутствует в словаре, увеличим result[num] на единицу.
#

# Этот код можно улучшить с помощью метода get().
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# Цикл for перебирает все элементы списка numbers и для каждого элемента с помощью метода get() мы
# получаем либо его значение из словаря result, либо значение по умолчанию, равное 0. К данному значению
# прибавляется единица, и результат записывается обратно в словарь по нужному ключу.


# Метод update() – реализует своеобразную операцию конкатенации для словарей. Он объединяет ключи и значения
# одного словаря с ключами и значениями другого. При совпадении ключей в итоге сохранится значение словаря,
# указанного в качестве аргумента метода update().

# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
#
# info1.update(info2)
#
# print(info1)  #--> {'name': 'Bob', 'age': 30, 'job': 'Dev', 'city': 'New York', 'email': 'bob@web.com'}

# В Python 3.9 появились операторы | и |= которые реализуют операцию конкатенации словарей.
# Приведенный ниже код:
#
# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
#
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
#
# info1 |= info2
#
# print(info1)
# аналогичен предыдущему коду.

# Метод setdefault() позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря, если он отсутствует.
# Метод принимает два аргумента:
#      key: ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать.
#      default: значение, которое будет использовано при добавлении нового элемента в словарь.

# В зависимости от значений параметров key и default возможны следующие сценарии работы данного метода.
# Сценарий 1. Если ключ key присутствует в словаре, то метод возвращает значение по заданному ключу
# (независимо от того, передан параметр default или нет).
# Приведенный ниже код:
#
# info = {'name': 'Bob',
#         'age': 25}
#
# name1 = info.setdefault('name')           # параметр default не задан
# name2 = info.setdefault('name', 'Max')    # параметр default задан
# print(name1)
# print(name2)
# выводит:
# Bob
# Bob
# Сценарий 2. Если ключ key отсутствует в словаре, то метод вставляет переданное значение default по заданному ключу.
# Приведенный ниже код:
# info = {'name': 'Bob',
#         'age': 25}
#
# job = info.setdefault('job', 'Dev')
# print(info)
# print(job)
# выводит:
# {'name': 'Bob', 'age': 25, 'job': 'Dev'}
# Dev
# При этом если значение default не передано в метод, то вставится значение None.

# Удаление элементов из словаря
# Существует несколько способов удаления элементов из словаря:
#
# оператор del;
# метод pop();
# метод popitem();
# метод clear().

# С помощью оператора del можно удалять элементы словаря по определенному ключу.
# Следующий программный код:
#
# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher',
#         'email': 'timyr-guev@yandex.ru'}
#
# del info['email']    # удаляем элемент имеющий ключ email
# del info['job']      # удаляем элемент имеющий ключ job
#
# print(info)
# выводит (порядок элементов может отличаться):
## {'name': 'Sam', 'age': 28}

# Оператор del удаляет из словаря элемент по заданному ключу вместе с его значением.
# Если требуется получить само значение удаляемого элемента, то нужен метод pop().
# Следующий программный код:
#
# info = {'name': 'Sam',
#         'age': 28,
#         'job': 'Teacher',
#         'email': 'timyr-guev@yandex.ru'}
#
# email = info.pop('email')          # удаляем элемент по ключу email, возвращая его значение
# job = info.pop('job')              # удаляем элемент по ключу job, возвращая его значение
#
# print(email)
# print(job)
# print(info)
# выводит:
#
# timyr-guev@yandex.ru
# Teacher
# {'name': 'Sam', 'age': 28}

# позволяет реализовать безопасное удаление элемента из словаря:
# surname = info.pop('surname', None)
# Если ключа surname в словаре нет, то в переменной surname будет храниться значение None.

# Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в
# виде кортежа (ключ, значение).
#
# info = {'name': 'Bob',
#      'age': 25,
#      'job': 'Dev'}
#
# info['surname'] = 'Sinclar'
#
# item = info.popitem()
#
# print(item)
# print(info)
# выводит:
#
# ('surname', 'Sinclar')
# {'name': 'Bob', 'age': 25, 'job': 'Dev'}

# Метод clear() удаляет все элементы из словаря.
# Метод copy() создает поверхностную копию словаря.
# Оператор присваивания (=) не копирует словарь, а лишь присваивает ссылку на старый словарь новой переменной.


# Примечание 1. Словарь можно использовать вместо нескольких вложенных условий,
# если вам нужно проверить число на равенство. Например вместо

# num = int(input())
# if num == 1:
#     description = 'One'
# elif num == 2:
#     description = 'Two'
# elif num == 3:
#     description = 'Three'
# else:
#     description = 'Unknown'
# print(description)
#
# можно написать
#
# num = int(input())
# description = {1: 'One', 2: 'Two', 3: 'Three'}
# print(description.get(num, 'Unknown'))


# # чтобы в переменной result хранился словарь, в котором ключи
# # – числа от 1 до 15 (включительно), а значения представляют собой квадраты ключей.
# key = [i for i in range(1,16)]
# value = [i**2 for i in range(1,16)]
# result = dict(zip(key, value))
# print(result)
#
# result = {}
# for i in range(1, 16):
#     result[i] = i * i
#
# result = {}
# result = {i: i**2 for i in range(1, 16)}

# result = {i: i ** 2 for i in range(1, 16)}


# объединил содержимое двух словарей dict1 и dict2 по ключам, складывая значения по одному и тому же ключу,
# # в случае, если ключ присутствует в обоих словарях
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# for key, value in dict2.items():
#     dict1[key] = dict1.setdefault(key, 0) + value
# result = dict1.copy()


# Дополните приведенный код так, чтобы в переменной result хранился словарь,
# в котором для каждого символа строки text будет подсчитано количество его вхождений.
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {l: text.count(l) for l in set(text)}
# print(result)


# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
#
# result = {}  # создаем словарь
#
# for i in s.split():  # проводим подсчет слов в тексте
#     result[i] = result.get(i, 0) + 1  # если слова нет то значение = 0 иначе добавляем +1
#
# s = max(result.values())  # узнаем максимальное значение повторяющегося слова и сохраняем его в переменной s
#
# print(min([key for key, value in result.items() if
#            value == s]))  # создаем список в который, способом перебора добовляем слова повторение которых равно значению s, с помощью min узнаем ккакое зи максимально одинаково аовторяются являются меньше в лексикографическом порядке

#
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for p, *name in pets:
#     result.setdefault(tuple(name), []).append(p)

# # Самое редкое слово 🌶️
# li = [word.strip(".,!?:;-").lower() for word in input().split()]
# di = {word: li.count(word) for word in li}
# m = min(di.values())
#
# for k, v in sorted(di.items(), key=lambda t: t[0]):
#     if v == m:
#         print(k)
#         break



# # Исправление дубликатов 🌶️
# d, l = {}, []
#
# for c in input().split():
#     if c not in l:
#         l.append(c)
#     else:
#         d[c] = d.get(c, 0) + 1
#         l.append(c + '_' + str(d[c]))
#
# print(*l)



# # Словарь программиста
# data =  [(input().split(':')) for i in range(int(input()))]
# data = {i[0].lower(): i[1].strip() for i in data}
# for i in [input().lower() for i in range(int(input()))]:
#     print(data.get(i, "Не найдено"))


# Анаграммы 1
# s = sorted(input())
# dct1 = dict(zip(range(len(s)), s))
#
# s = sorted(input())
# dct2 = dict(zip(range(len(s)), s))
#
# print('YES' if dct1 == dct2 else 'NO')

# print('YES' if sorted(input()) == sorted(input()) else 'NO')

# # Анаграммы 2
# s1 = [i for i in input().lower() if i.isalpha()]
# s2 = [i for i in input().lower() if i.isalpha()]
# print('YES' if sorted(s1) == sorted(s2) else 'NO')

# Словарь синонимов
# lovar=dict([[i for i in input().split(' ')] for i in range(int(input()))])
# a=input()
# for key,value in lovar.items():
#     if key==a:
#         print(value)
#     if value==a:
#         print(key)


# # Страны и города
# d = {}
# for _ in range(int(input())):
#     s = input().split()
#     d[s[0]] = s[1:]
# for _ in range(int(input())):
#     city = input()
#     for country, cities in d.items():
#         if city in cities:
#             print(country)

# Телефонная книга
# res = {}
# for i in range(int(input())):
#     a, b = input().lower().split()
#     res[b] = res.get(b, []) + [a]
#
# for i in range(int(input())):
#     name = input().lower()
#     print(*res.get(name, ['абонент не найден']))


# # Секретное слово
# f = input()
# d = {}
# for u in f:
#     d.setdefault(f.count(u), u)
#
# for _ in range(int(input())):
#     key, value = input().split(':')
#     f = f.replace(d[int(value)], key)
# print(f)

# 10.5 Вложенные словари и генераторы словарей
# ids = ['emp1', 'emp2', 'emp3']
# emp_info = [{'name': 'Timur', 'job': 'Teacher'},
#             {'name': 'Ruslan', 'job': 'Developer'},
#             {'name': 'Rustam', 'job': 'Tester'}]
# info = dict(zip(ids, emp_info))


# Чтобы изменить значение определенного элемента во вложенном словаре, необходимо обратиться
# к его ключу и использовать оператор присвоения (=).
#
# Приведенный ниже код:
#
# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# info['emp1']['job'] = 'Manager'
#
# print(info['emp1'])
# выводит:
#
# {'name': 'Timur', 'job': 'Manager'}


# Итерация по вложенным словарям
# Итерации по вложенным словарям осуществляются как правило двумя циклами for (иногда достаточно одного цикла).
#
# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
# for emp in info:
#     print('Employee ID:', emp)
#     for key in info[emp]:
#         print(key + ':', info[emp][key])
#     print()
# выводит:
# Employee ID: emp1
# name: Timur
# job: Teacher
#
# Employee ID: emp2
# name: Ruslan
# job: Developer
#
# Employee ID: emp3
# name: Rustam
# job: Tester
#


# Аналогичного результата можно было добиться с помощью метода items():
#
# info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
#         'emp2': {'name': 'Ruslan', 'job': 'Developer'},
#         'emp3': {'name': 'Rustam', 'job': 'Tester'}}
#
# for emp, inf in info.items():
#     print('Employee ID:', emp)
#     for key in inf:
#         print(key + ':', inf[key])
#     print()


# Генераторы словарей
# squares = {i: i**2 for i in range(6)}
# {ключ: значение for переменная in последовательность}

## 1. Генератор словаря при итерировании по строке.
# dct = {c: c * 3 for c in 'ORANGE'}
# print(dct)  #--> {'O': 'OOO', 'R': 'RRR', 'A': 'AAA', 'N': 'NNN', 'G': 'GGG', 'E': 'EEE'}


##2. Для вычисления ключа и значения в генераторе словаря могут быть использованы выражения.
# lst = ['ReD', 'GrEeN', 'BlUe']
# dct = {c.lower(): c.upper() for c in lst}
# print(dct)   #-->  {'red': 'RED', 'green': 'GREEN', 'blue': 'BLUE'}

# ##3. Извлечение из словаря элементов с определенными ключами.
# dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
# selected_keys = [0, 2, 5]
# dict2 = {k: dict1[k] for k in selected_keys}
# print(dict2)   #-->  {0: 'A', 2: 'C', 5: 'F'}

##Условия в генераторе словарей
# squares = {i: i**2 for i in range(10) if i % 2 == 0}
# print(squares)


##Генераторы вложенных словарей
# squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}
# for value in squares.values():
#     print(value)
# выводит:
#
# {0: 0}
# {0: 0, 1: 1}
# {0: 0, 1: 1, 2: 4}
# {0: 0, 1: 1, 2: 4, 3: 9}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#


# получить словарь result , в котором ключом будет позиция числа в списке numbers (начиная с 00),
# а значением – его квадрат.
# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i:numbers[i]**2 for i in range(len(numbers))}
# print(result)


# # получить словарь result, состоящий из всех элементов словаря colors, кроме тех,
# # у которых значением является None.
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
# result = {key: value for key, value in colors.items() if value != None}


# получить словарь result, состоящий из всех элементов словаря favorite_numbers ,
# значения которых являются двузначными числами.
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
# result = {i: favorite_numbers[i] for i in favorite_numbers if int(favorite_numbers[i]/10)  in range(1, 10)}


# # получить словарь result, состоящий из всех элементов словаря months,
# # в которых ключ и значение поменялись местами.
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# result = {value: key for key, value in months.items()}


# # В переменной s хранится строка пар число:слово. Дополните приведенный код, используя генератор,
# # # чтобы получить словарь result, в котором числа будут ключами, а слова – значениями.
# #
# # s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# # result = {int(key): value for key, value in (a.split(':') for a in s.split())}


# # спользуя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент
# # списка numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 1.
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {key: sorted([n for n in range(1, key + 1) if key % n == 0]) for key in numbers}


# # получить словарь result, в котором ключом будет строка – элемент списка words, а значением – список соответствующих
# # кодов ASCII символов данной строки
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {word: [ord(w) for w in word] for word in words}


# получить словарь result, состоящий из всех элементов словаря letters , за исключением тех, ключи которых
# есть в списке remove_keys.
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {key: value for key, value in letters.items() if key not in remove_keys}


# # олучить словарь result, состоящий из всех элементов словаря students,
# # где указан рост больше 167 см, а вес меньше 75 кг.
# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
# result = {key: value for key, value in students.items() if value[0] > 167 and value[1] < 75}



# # получить словарь result, в котором ключом является первый элемент каждого кортежа, а значением – кортеж
# # из оставшихся двух элементов.
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# result = {k: tuple(v) for k, *v in tuples}


# # получить список result, содержащий вложенные словари в соответствии с образцом:
# # [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
# result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_ids))]






