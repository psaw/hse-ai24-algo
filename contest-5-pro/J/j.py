import os
import sys


path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def solve(n: int, m: int) -> int:
    """
    ### Решение:
    Динамическое программирование.
    Сохраняем в таблице число вариантов прихода в конкретную точку.
    """

    dp = [[0 for _ in range(m)] for _ in range(n)]

    # начальная точка тоже имеет стоимость
    dp[0][0] = 1

    # вычисление стоимости остальных точек
    # со 1-й строки и толбца, т.к. конь не может остаться на 0-й
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = (dp[i - 1][j - 2] if j >= 2 else 0) + (
                dp[i - 2][j - 1] if i >= 2 else 0
            )

    return dp[n - 1][m - 1]


N, M = map(int, input().split())

print(solve(N, M))
