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
    is_max_heap, is_min_heap = True, True
    arr.append(next(read_next_int(sys.stdin)))
    for n in read_next_int(sys.stdin):
        # для исключения варианта достаточно одного нарушения
        if arr[i // 2] < n:  # если потомок больше - это точно не max-heap
            is_max_heap = False
        if arr[i // 2] > n:  # если потомок меньше - это точно не min-heap
            is_min_heap = False

        if not (is_max_heap or is_min_heap):  # ранний выход
            break

        arr.append(n)
        i += 1

    return "YES" if is_max_heap or is_min_heap else "NO"


def solve2():
    N = int(input())

    # в отличие от задачи А, тут большой лимит по памяти (512МБ),
    # поэтому просто считаем все сразу - это гораздо быстрее,
    # чем читать посимвольно и парсить числа
    nums = list(map(int, input().split()))

    if N <= 1:
        return "YES"  # один элемент всегда куча

    is_max_heap, is_min_heap = True, True

    # Проверим свойства кучи для каждого элемента
    # Проверять будем и на max-heap и на min-heap
    for i in range(1, len(nums)):
        parent_idx = (i - 1) // 2

        # для исключения варианта достаточно одного нарушения
        # если потомок больше - это точно не max-heap
        if nums[parent_idx] < nums[i]:
            is_max_heap = False

        # если потомок меньше - это точно не min-heap
        if nums[parent_idx] > nums[i]:
            is_min_heap = False

        if not (is_max_heap or is_min_heap):  # ранний выход
            break

    return "YES" if is_max_heap or is_min_heap else "NO"


print(solve2())
