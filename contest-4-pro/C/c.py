import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input2.txt", "r")


N, M = map(int, input().split())

arr = [None] * N

for i in range(N):
    arr[i] = [*map(int, input().split())]


def solve(arr1, arr2, m):
    # объединение сортированных массивов
    merged_array = [None] * (2 * m - 1)
    i, j = 0, 0
    while i < m and j < m:
        if arr1[i] <= arr2[j]:
            merged_array[i + j] = arr1[i]
            i += 1
        else:
            merged_array[i + j] = arr2[j]
            j += 1

    # докопирование хвостов (выполнится только один цикл)
    while i < m:
        merged_array[i + j - 1] = arr1[i]
        i += 1

    while j < m:
        merged_array[i + j - 1] = arr1[j]
        j += 1

    # медиана ровно посередине
    return round((merged_array[m - 1] + merged_array[m]) / 2.0, 5)


for first in range(N - 1):
    for second in range(first + 1, N):
        print(f"{solve(arr[first], arr[second], M):.5f}")
