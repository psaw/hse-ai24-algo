import math
import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')


def find_maximum_subarray(arr):
    """
    Поиск непрерывного подмассива с максимальной суммой (алгоритм Кадане).

    Ключевое свойство: 
    Максимальный подмассив, заканчивающийся на позиции k, либо состоит
    только из элемента arr[k], либо состоит из максимального подмассива,
    заканчивающегося на k-1, к которому добавили arr[k]. 
    
    Алгоритм проверяет оба варианта и выбирает лучший (current_max),
    а затем обновляет глобальный максимум (max_so_far).
    Так как мы проходим все элементы, мы гарантированно найдем и глобальный максимум.

    Args:
        arr: Входной массив целых чисел.

    Returns:
        Кортеж:
        - max_sum: Максимальная сумма подмассива.
        - start_index: Индекс начала подмассива.
        - end_index: Индекс окончания подмассива.
        
        Возвращает (-math.inf, -1, -1) если входной массив пустой.
    """
    if not arr:
        # Handle empty array case
        return -math.inf, -1, -1 # Or (0, -1, -1) depending on requirements

    n = len(arr)
    max_so_far = arr[0]   # максимальная сумма подмассива 
    current_max = arr[0]  # максимальная сумма подмассива, заканчивающегося на данном элементе
    max_start_index = 0
    max_end_index = 0
    current_start_index = 0

    for k in range(1, n):
        # Решаем что выгоднее - продолжить текущий подмассив, или начать новый
        if arr[k] >= current_max + arr[k]:  # так нагляднее, чем "0 >= current_max"
            current_max = arr[k]
            current_start_index = k
        else:  # продолжить текущий подмассив, добавив к сумме arr[k]
            current_max = current_max + arr[k]

        # Обновление глобального максимума
        if current_max > max_so_far:
            max_so_far = current_max
            max_start_index = current_start_index
            max_end_index = k

    return max_so_far, max_start_index, max_end_index


N = int(input())
my_array = [*map(int, input().split())]

max_sum, start, end = find_maximum_subarray(my_array)
print(start, end)