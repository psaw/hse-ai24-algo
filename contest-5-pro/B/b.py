import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def solve(n: int) -> int:
    """Вычислите n-й член последовательности, заданной формулами:

    a_2n = a_n + a_n-1,
    a_2n+1 = a_n - a_n-1,

    a_0 = 1,
    a_1 = 1.
    """
    dp = [0] * (n + 1)

    for i in range(n + 1):
        if i < 2:
            dp[i] = 1
        else:
            if i & 1:  # i - нечетное
                dp[i] = dp[i // 2] - dp[i // 2 - 1]
            else:
                dp[i] = dp[i // 2] + dp[i // 2 - 1]

    return dp[n]


N = int(input())
print(solve(N))
