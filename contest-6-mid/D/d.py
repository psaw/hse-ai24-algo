import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input.txt", "r")

"""Шашку - в дамки"""
X, Y = map(int, input().split())

dp = [[0 for _ in range(8)] for _ in range(8)]
dp[8-Y][X-1] = 1  # в перевернутых координатах. Y=1 - низ доски

# print(dp)
for i in range(8-Y-1, -1, -1):  # смотрим только строки выше Y
    for j in range(8):
        dp[i][j] = (dp[i + 1][j + 1] if i < 7 and j < 7 else 0) + (dp[i + 1][j - 1] if i < 7 and j > 0 else 0)

# print(dp)
print(sum(dp[0]))
