""" 
Дано число N, а затем N строк. Необходимо отсортировать строки по возрастанию 
длины, причём строки одинаковой длины должны выводиться в том же порядке, 
в котором они были во вводе.
"""

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

N = int(input())

strings = [""] * N
for i in range(N):
    strings[i] = input()

# Сортировка вставками по возрастанию длины
# Т.к. используется строгое сравнение "<", то сортирвка УСТОЙЧИВАЯ
for i in range(1, N):
    j = i
    while j > 0 and len(strings[j]) < len(strings[j-1]):
        strings[j], strings[j-1] = strings[j-1], strings[j]
        j -= 1

print("\n".join(strings))
