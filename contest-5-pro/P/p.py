import os
import sys


path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def solve(s1: str, s2: str) -> int:
    """
    ### Решение:
    Динамическое программирование.
    Сохраняем в массив макс. длину общей подпоследовательности,
    оканчивающейся в текущей точке.
    """

    # начальные 0
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    # вычисление макс. длин
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    # print(dp)
    print(dp[len(s1)][len(s2)])

    # восстановление
    idx1 = []
    idx2 = []
    i = len(s1)
    j = len(s2)
    while i>0 and j>0 and dp[i][j] != 0:
        if s1[i-1] != s2[j-1]:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        else:
            idx1.append(i)
            idx2.append(j)
            i -= 1
            j -= 1
    
    print(*idx1[::-1])
    print(*idx2[::-1])

s1 = input()
s2 = input()

# print(arr)
solve(s1, s2)
