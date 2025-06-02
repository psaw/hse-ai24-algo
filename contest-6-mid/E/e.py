import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input.txt", "r")

"""Ход конем"""
N, M = map(int, input().split())

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = 1 # начальная позиция

# print(dp)
# Перебираем клетки ДИАГОНАЛЯМИ
# Это вариант решения более сложной задачи (из КР для Про),
# где было еще два возможных хода, что требовало заполнения 
# матрицы по диагоналям.
# В этой задаче можно заполнять по строкам, но оставлю так,
# просто уберу два лишних хода (с1 и c4)
for diag in range(N+M-1):  # диагональ с суммой координат diag. 0 - левый верх
    for i in range(diag, -1, -1):   # строка
        j = diag - i                # столбец
        if i==j==0:  # начальная позиция
            continue
        # чтобы не выходить за границы, но и не думать над формулой, cужающей перебор
        if i>=N or j >= M:
            continue

        # все варианты откуда можно прийти в i,j
        # 1: i+1, j-2
        # c1 = dp[i+1][j-2] if N>(i+1)>=0 and M>(j-2)>=0 else 0
        # 2: i-1, j-2
        c2 = dp[i-1][j-2] if N>(i-1)>=0 and M>(j-2)>=0 else 0
        # 3: i-2, j-1
        c3 = dp[i-2][j-1] if N>(i-2)>=0 and M>(j-1)>=0 else 0
        # 4: i-2, j+1
        # c4 = dp[i-2][j+1] if N>(i-2)>=0 and M>(j+1)>=0 else 0

        # dp[i][j] = c1 + c2 + c3 + c4
        dp[i][j] = 0 + c2 + c3 + 0

       
print(dp[N-1][M-1])