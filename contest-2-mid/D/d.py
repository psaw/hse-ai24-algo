import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

w, h, n = map(int, input().split())  # ширина, высота и количество дипломов

print(w, h, n)

def is_board_bad(w, h, n, size):
    n_w = size // w  # сколько влезет в ширину
    n_h = size // h  # сколько влезет в высоту
    return n_h * n_w < n  # True, если доска не подходит

l = max(w, h)
r = min(w, h) * n

# left binary search
while l < r - 1:
    mid = (l + r) // 2
    if is_board_bad(w, h, n, mid):  # тест, что доска НЕ подойдет
        l = mid
    else:
        r = mid

print(r)