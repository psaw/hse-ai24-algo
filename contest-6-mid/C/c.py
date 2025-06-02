import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input.txt", "r")

"""Черепашка"""
N, M = map(int, input().split())

dp = [list(map(int, input().split())) for _ in range(N)]

# print(dp)
for i in range(N):
    for j in range(M):
        if (i, j) == (0, 0):
            continue

        dp[i][j] += max(dp[i - 1][j] if i > 0 else 0, dp[i][j - 1] if j > 0 else 0)

print(dp[N - 1][M - 1])
