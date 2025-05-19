import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

N, K = map(int, input().split())

def solve(arr, n, k):
    # База индукции: получили длину n - вывод на печать
    if len(arr) == n:
        print(''.join(map(str, arr)))
        return
    
    # Перебор значений для текущей позиции
    for i in range(k):
        # Добавить элемент
        arr.append(i)
        # Рекурсивно достраиваем следующие
        solve(arr, n, k)
        # Удаляем, чтобы в следующем шаге цикла вставить очередной
        arr.pop()

solve([], N, K)
