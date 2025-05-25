import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def solve(n: int, m: int) -> int:
    """В прямоугольной таблице NxM в начале игрок находится в левой верхней клетке.
    За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо вниз
    (влево и вверх перемещаться запрещено).

    Посчитайте, сколько есть способов у игрока попасть в правую нижнюю клетку.

    ### Решение:
    Динамическое программирование.
    Сохраняем в таблице число маршрутов прихода в конкретную точку.
    """

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = 1  # начальная точка, значение =1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:  # пропускаем начальную точку
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n][m]


N, M = map(int, input().split())

print(solve(N, M))
