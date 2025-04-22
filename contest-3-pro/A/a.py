""" 
Реализовать сортировку Хоара (быструю, quicksort)по неубыванию для заданного
целочисленного массива N элементов с выбором в качестве опорного среднего
элемента обрабатываемой части массива.

Решить данную задачу требуется по классической схеме Хоара:
с двумя индексами и массив делится на 2 части.
"""

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input3.txt', 'r')

N = int(input())
arr = [*map(int, input().split())]

# реализация классической схемы
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# реализация схемы Хоара с двумя индексами, идущими с обеих сторон
def quicksort2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = 0
    right = len(arr) - 1
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return quicksort(arr[:left]) + quicksort(arr[left:])

print(*quicksort2(arr))