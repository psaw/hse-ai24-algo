"""
Дана матрица размера n x n, в которой каждая строка и столбец отсортированы
в порядке возрастания, верните k-й наименьший элемент матрицы.

Обратите внимание, что это k-й наименьший элемент в отсортированном порядке
(среди всех элементов).

Вам необходимо найти решение со сложностью памяти лучше O(nˆ2).
"""

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(n)
print(matrix)


def check(matrix, mid, k, n):
    count = 0  # накопительный счетчик "число эл-тов меньше mid"
    i, j  = n - 1, 0  # начиаем обход с нижнего левого угла матрицы
    while i >= 0 and j < n:
        if mid >= matrix[i][j]:  # если текущий эл-т меньше mid
            count += i + 1  # кол-во эл-тов выше текущего, и все они <= mid. Добавим их число к count
            j += 1  # .. и переходим к следующему столбцу
        else:
            i -= 1  # смещаемся на 1 элемент выше
    return count >= k  # нашлось ли число "эл-тов меньше mid" больше k

def kmatrix(matrix, n, k):
    l = matrix[0][0]
    r = matrix[n-1][n-1]
    while l < r:  # левый "бнарный поиск по ответу"
        mid = (l + r) // 2 
        if check(matrix, mid, k, n):
            r = mid
        else:
            l = mid + 1
    return l

print(kmatrix(matrix, n, k))