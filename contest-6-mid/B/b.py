import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input.txt", "r")

"""Треугольник Паскаля"""
N = int(input())

if N == 0:
    print("")
else:
    dp = [[] for _ in range(N)]

    for i in range(N):
        dp_row = [0 for _ in range(i+1)]
        for j in range(i+1):
            if j in (0, i):
                dp_row[j] = 1
            else:
                dp_row[j] = dp[i-1][j-1] + dp[i-1][j]
        dp[i] = dp_row
        print(*dp_row)