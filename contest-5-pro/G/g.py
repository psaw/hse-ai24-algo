import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def solve(n: int, t: list[list[int]]) -> int:
    """
    ### Решение:
    Динамическое программирование.
    Сохраняем min время обслуживания всех до i-го покупателя (влючительно).
    """

    dp = [0] * (n + 1)
    dp[0] = 0

    if n > 0:
        # для первого - сам купит 1 билет
        dp[1] = t[1][0]

    if n > 1:
        # для второго:
        # - либо каждый сам купит по 1 билету (t[1][0] + t[2][0])
        # - либо первый купит сразу 2 билета (t[1][1])
        dp[2] = min(t[1][0] + t[2][0], t[1][1])

    for i in range(3, n + 1):
        dp[i] = min(
            dp[i - 1] + t[i][0],  # сам купит 1 билет
            dp[i - 2] + t[i - 1][1],  # предыдущий купит два билета
            dp[i - 3] + t[i - 2][2],  # пред-предыдущий купит три билета
        )
    return dp[n]


N = int(input())
timing = [[0, 0, 0]] * (N + 1)
for i in range(1, N + 1):
    timing[i] = list(map(int, input().split()))

print(solve(N, timing))
