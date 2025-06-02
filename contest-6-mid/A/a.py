import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input.txt", "r")

"""Количество маршрутов в прямоугольной таблице"""
N, M = map(int, input().split())

dp = [[1 for _ in range(M)] for _ in range(N)]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N-1][M-1])