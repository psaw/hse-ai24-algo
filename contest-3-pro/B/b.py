""" 
Отсортируйте данный массив, используя сортировку слиянием.

1. разбить массив на 2 половины
2. рекурсивно вызвать этот же алгоритм для каждой половины
3. отсортированные результаты "слить" в один
"""

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

N = int(input())
arr = [*map(int, input().split())]


def merge(arr_l: list, arr_r: list) -> list:
    """ Слияние """
    n_l = len(arr_l)  # длина левого массива
    n_r = len(arr_r)  # длина правого массива
    res = [0] * (n_l + n_r)  # выходной массив
    l = r = 0  # индексы по левому и правому входным массивам
    while l + r < n_l + n_r:
        if l == n_l:  # если левый закончился, то берем правый
            res[l+r] = arr_r[r]
            r += 1
        elif r == n_r:  # если правый закончился, то берем левый
            res[l+r] = arr_l[l]
            l += 1
        else:  # если еще есть оба, то сравниваем и берем меньший
            if arr_l[l] <= arr_r[r]:
                res[l+r] = arr_l[l]
                l += 1
            else:
                res[l+r] = arr_r[r]
                r += 1
    return res


def merge_sort(arr):
    # базовый случай для рекурсии
    if len(arr) <= 1:
        return arr

    # шаг рекурсии
    # делим массив пополам
    mid = len(arr) // 2
    arr_l = arr[:mid]
    arr_r = arr[mid:]
    # рекурсивно сортируем половинки
    arr_l = merge_sort(arr_l)
    arr_r = merge_sort(arr_r)
    # сливаем вместе
    arr = merge(arr_l, arr_r)
    return arr

# print(*arr)
print(*merge_sort(arr))


