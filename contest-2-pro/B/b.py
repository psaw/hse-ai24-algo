""" 
Дан целочисленный массив nums, отсортированный по возрастанию
(все значения различны).
Элементы массива циклически сдвигаются на некоторое число k
(1 <= k < nums.length), так что результирующий массив имеет вид 
[nums[k], nums[k+1],... , nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(с индексом 0). 
Например, [0,1,2,4,5,6,7] можно сдвинуть на 3 элемента 
и превратить в [4,5,6,7,0,1,2].

Нужно вернуть индекс искомого элемента target в массиве после сдвига.

Вы должны написать алгоритм со сложностью выполнения O(log n).
"""

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input3.txt', 'r')

n = int(input())
nums = [*map(int, input().split())]
t = int(input())

print(n)
print(nums)
print(t)

l = 0
r = n
while l < r - 1:
    mid = (l + r) // 2
    if nums[l] < nums[mid]:
        if nums[l] <= t < nums[mid]:
            r = mid
        else:
            l = mid
    else:
        if t < nums[l] and nums[mid] < t:
            l = mid
        else:
            r = mid

print(l)