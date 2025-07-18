import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def solve(n: int, c: list[int]) -> int:
    """Мальчик подошел к платной лестнице.
    Чтобы наступить на любую ступеньку, нужно заплатить указанную на ней сумму.
    Мальчик умеет
    - перешагивать на следующую ступеньку,
    - либо перепрыгивать через ступеньку.

    Требуется узнать, какая наименьшая сумма понадобится мальчику,
    чтобы добраться до верхней ступеньки.

    Args:
      n - число ступеней
      с - список стоимостей ступеней

    Returns:
      Минимальная стоимость подъема на верхнюю ступень.

    ### Решение:
    Динамическое программирование.
    Сохраняем min стоимость достижения каждой ступени от 1 до n.
    """

    dp = [0] * (n + 1)
    dp[0]

    if n > 0:
        # ступени нумеруем 1..N, но массив с ценами 0..N-1
        dp[1] = c[0]

    for i in range(2, n + 1):
        dp[i] = c[i - 1] + min(dp[i - 1], dp[i - 2])

    return dp[n]


N = int(input())
cost = list(map(int, input().split()))
print(solve(N, cost))
