import os
import sys


path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def solve(n: int, seq: list[int]) -> int:
    """
    ### Решение:
    Динамическое программирование.
    Сохраняем в массив число вариантов подпоследовательности,
    оканчивающихся в текущей точке.
    """

    # все 1, т.к один эл-т - это последовательность длины 1
    dp = [1 for _ in range(n)]

    max_len = 1
    # вычисление стоимости остальных точек
    for i in range(1, n):
        # придется просмотреть все пред.элементы, 
        # чтобы найти все делители
        for j in range(i-1, -1, -1):
            if seq[i] % seq[j] == 0:  # если нашли делитель
                dp[i] = max(dp[i], dp[j] + 1)
                max_len = max(max_len, dp[i])

    # print(dp)
    return max_len


N = int(input())
arr = list(map(int, input().split()))
# print(arr)
print(solve(N, arr))
