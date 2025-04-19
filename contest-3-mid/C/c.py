"""
Рреализовать сортировку простыми вставками по неубыванию и посчитать количество
элементов, которые при добавлении к сортированной части уже находились на своём
месте, то есть которые не пришлось двигать.
"""

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

N = int(input())
arr = [*map(int, input().split())]
count = 0
for i in range(1, N):
    j = i
    count += (arr[j] >= arr[j-1])
    while j>0 and (arr[j] < arr[j-1]):
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1

print(*arr)
print(count)

