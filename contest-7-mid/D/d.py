import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input2.txt", "r")


#####################################
#                                   #
# Расстояние Левенштейна            #
#                                   #
#####################################


def lv_recursive(s: str, t: str) -> int:
    def f(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if s[i - 1] == t[j - 1]:
            return f(i - 1, j - 1)
        return 1 + min(
            f(i - 1, j),  # удаление символа из s
            f(i, j - 1),  # вставка символа в s
            f(i - 1, j - 1),  # замена символа в s символом из t
        )

    return f(len(s), len(t))


def lv_dynamic(s: str, t: str) -> int:
    n = len(s)
    m = len(t)
    # ранний выход, если вырожденный случай
    if n == 0:
        return m
    if m == 0:
        return n

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    # вырожденные случаи уже обработали, но данные нужны
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    # dp для пары "cat", "cats"
    #   _ c a t s
    # _ 0 1 2 3 4
    # c 1 0 1 2 3
    # a 2 1 0 1 2
    # t 3 2 1 0 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:  # в строках индекс от 0
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    # print(dp)
    return dp[-1][-1]


N = int(input())  # число пар строк для сравнения
res = []
for _ in range(N):
    s1 = input()
    s2 = input()
    res.append(lv_dynamic(s1, s2))
print(*res)
