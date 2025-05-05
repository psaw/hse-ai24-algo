import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


yy, xx = map(int, input().split())

m = []
for _ in range(yy):
    m.append(list([int(x) for x in input().split()]))

smax = 1 # искомый макс размер квадрата. 1 гарантировано есть

# для экономии памяти считаем префиксную сумму и сохраняем в тот же массив
# значения - это максимальный размер квадрата из 1, 
# для которого текущая координата - правый нижний угол
for y in range(1, yy):
    for x in range(1, xx):
        if m[y][x] == 1:  # если 1, то возможно это правый нижний угол
            # если сверху/слева были квадраты, то размер увеличится на 1
            m[y][x] = min(m[y-1][x-1], m[y-1][x], m[y][x-1]) + 1
        # отслеживаем максимум
        smax = max(smax, m[y][x])

print(smax)
