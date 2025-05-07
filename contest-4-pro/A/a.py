"""
Задан массив из n целых чисел.
Определите индекс последнего элемента массива, входящего в бинарную кучу для максимума.
"""

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input2.txt", "r")


def solve_naive():
    N = int(input())
    nums = [*map(int, input().split())]

    last_n = N - 1
    for i in range(N - 1, 0, -1):
        if nums[(i - 1) // 2] < nums[i]:
            last_n = i - 1

    return last_n


def read_next_int(f):
    num_str = ""
    char = ""
    while True:
        char = f.read(1)

        if not char or char == "\n":
            if num_str:
                yield int(num_str)
            break

        if char.isdigit() or char == "-":
            num_str += char

        if char.isspace() and num_str:
            yield int(num_str)
            num_str = ""


def solve():
    N = int(input())
    i = 0
    arr = []
    arr.append(next(read_next_int(sys.stdin)))
    for n in read_next_int(sys.stdin):
        if arr[i // 2] < n:
            break
        arr.append(n)
        i += 1

    return i


print(solve())
