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



