"""
Дано n отрезков провода длиной l₁, l₂, ..., lₙ сантиметров. 
Требуется с помощью разрезания получить из них k равных отрезков 
как можно большей длины, выражающейся целым числом сантиметров. 
Если нельзя получить k отрезков длиной даже 1 см, вывести 0.
"""

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

N, K = map(int, input().split())
wires = []
for _ in range(N):
    wires.append(int(input()))

def check_segments(length, wires, k):
    """
    Проверить можно ли получить как минимум k отрезков
    заданной длины length из доступных проводов?
    """
    if length == 0:
        return True
    
    total_segments = 0
    for wire in wires:
        # Сколько отрезков можно получить из текущего провода
        segments_from_wire = wire // length
        total_segments += segments_from_wire
        
        # Если уже достаточно, то выходим раньше
        if total_segments >= k:
            return True
    
    return total_segments >= k

# Бинарный поиск максимальной длины отрезков
# Пространство поиска: от 0 до сумма_всех_проводов // K + 1
left = 0  # минимум 0, чтобы вернуть 0, если нет решения даже для длины 1
right = sum(wires) // K + 1

while left < right:
    mid = (left + right) // 2
    
    if check_segments(mid, wires, K):
        # если можно, то пробуем более длинные (берем правый полуинтервал)
        left = mid + 1
    else:
        # если нет - то пробуем покороче (берем левый полуинтервал)
        right = mid

# -1, т.к. left - первая длина, которая не подошла
print(left - 1)
