""" 
Вычисление количества нулей на некотором интервале заданного одномерного массива.
Реализуйте эффективную обработку большого числа таких запросов.
"""

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input3.txt', 'r')

N = int(input())
arr = [*map(int, input().split())]
arr0 = [0] * (N+1)

# префиксные суммы
for i in range(1, N+1):
    arr0[i] = arr0[i-1] + (arr[i-1] == 0)

K = int(input())

# разность префиксных сумм
for i in range(K):
    l, r = map(int, input().split())
    print(arr0[r] - arr0[l-1], end=" ")
print("")
