import os
import sys
import collections

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def solve(c, press, n):
    cc = collections.Counter(press)

    for i in range(1, n + 1, 1):
        if cc.get(i, 0) > c[i - 1]:
            print("yes")
        else:
            print("no")


def solve2(c: list, press: list, n: int) -> None:
    cc = [0] * (n + 1)
    for p in press:
        cc[p] += 1

    for i in range(1, n + 1, 1):
        if cc[i] > c[i - 1]:
            print("yes")
        else:
            print("no")


n = int(input())  # количество клавиш на клавиатуре
c = [*map(int, input().split())]  # макс. количество нажатий каждой клачиши
k = int(input())  # общее количество нажатий
press = [*map(int, input().split())]  # последовательность нажатий

solve2(c, press, n)
