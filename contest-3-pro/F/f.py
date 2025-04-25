""" 
Даны два множества: отрезки на прямой и точки.
Для каждой точки из второго множества, определите количество отрезков,
которым она принадлежит. Точка считается принадлежащей отрезку, 
если она находится внутри него или на границе.
"""
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

N, M = [*map(int, input().split())]

lines = []
for i in range(N):
    lines.append([*map(int, input().split())])

points =[*map(int, input().split())]

# print(lines)
# print(points)

for p in points:
    count = 0
    for line in lines:
        if  line[0] <= p <= line[1]:
            count += 1
    print(count, end=" ") 