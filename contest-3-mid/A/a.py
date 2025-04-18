import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

N = int(input())
nums = [*map(int, input().split())]

"""
Внешний цикл - точка вставки (идет с конца).
Внутренний цикл - все предыдущие элементы сравниваются с точкой вставки. Если больше - обмен местами. 
"""

def sort_max_from_top(nums, N):
    for insert_idx in range(N-1, 0, -1):
        max_current = nums[insert_idx]
        for check_idx in range(0, insert_idx):
            if nums[check_idx] > max_current:
                max_current = nums[check_idx]
                nums[check_idx], nums[insert_idx] = nums[insert_idx], nums[check_idx]
    return nums

print(*sort_max_from_top(nums, N))