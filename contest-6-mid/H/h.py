import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input.txt", "r")

"""Половина"""
N, K = map(int, input().split())

temp = set()
res = set([N])

for _ in range(K):
    print(*res)
    for a in res:
        if a > 0:
            if int(a) == a and a != 1:  # целое и не 1 (0.5 добавим и так)
                temp.add(a / 2)
            temp.add(a - 0.5)
        else:
            temp.add(a)  # вернуть 0.0
    temp, res = set(), temp

print(len(res))
print(*sorted(res))
