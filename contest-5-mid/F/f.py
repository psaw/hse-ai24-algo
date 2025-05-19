import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

N, K = map(int, input().split())

def solve(n, k):
    if n <= k:
        # База индукции: ящики поместились => +1 грузовик
        return 1
    else:
        # Индуктивный переход: поделим поровну (остаток добавим к одной)
        return solve(n // 2 + n % 2, k) + solve(n // 2, k)

print(solve(N, K))
