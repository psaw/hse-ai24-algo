""" 
Сумма чисел в прямоугольной подматрице
"""

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input0.txt', 'r')

N, M, Q = map(int, input().split())

matrix = [[]] * N
for i in range(N):
    matrix[i] = [*map(int, input().split())]

print(matrix)

# подготовка матрицы префиксных суммм
matrix_pref = [[0] * (M+1) for i in range(N+1)]

# зполняем первый столбец
for i in range(1, N+1):
    matrix_pref[i][1] = matrix_pref[i-1][1] + matrix[i-1][0]

# зполняем первую строку
for j in range(1, M+1):
    matrix_pref[1][j] = matrix_pref[1][j-1] + matrix[0][j-1]

# заполняем остальные ячейки
for i in range(2, N+1):
    for j in range(2, M+1):
        matrix_pref[i][j] = matrix[i-1][j-1] + matrix_pref[i-1][j] + matrix_pref[i][j-1] - matrix_pref[i-1][j-1]

print(matrix_pref)

def sum_matrix_n2(matrix, x1, y1, x2, y2):
    """
    Сумма чисел в прямоугольной подматрице.
    Реализация: перебор
    Сложность: O(n^2)

    :param matrix: матрица
    :param x1: левый верхний угол (индексы от 0)
    :param y1: левый верхний угол
    :param x2: правый нижний угол
    :param y2: правый нижний угол
    """
    sum = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            sum += matrix[i][j]
    return sum


def sum_matrix_n(matrix_pref, x1, y1, x2, y2):
    """
    Сумма чисел в прямоугольной подматрице.
    Реализация: префиксные суммы
    Сложность: O(n)

    :param matrix_pref: матрица префиксных сумм - суммы по подматрице (0, 0)-(x, y)
    :param x1: левый верхний угол (индексы от 1)
    :param y1: левый верхний угол
    :param x2: правый нижний угол
    :param y2: правый нижний угол
    """
    
    return matrix_pref[x2][y2] - matrix_pref[x1-1][y2] - matrix_pref[x2][y1-1] + matrix_pref[x1-1][y1-1]


for i in range(Q):
    x1, y1, x2, y2 = map(int, input().split())

    print(sum_matrix_n(matrix_pref, x1, y1, x2, y2))