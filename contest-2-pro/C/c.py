"""
Вам дан отсортированный массив, состоящий только из целых чисел, 
в котором каждый элемент встречается ровно два раза, за исключением
одного элемента, который появляется ровно один раз.

Верните единственный элемент, который появляется только один раз.

Ваше решение должно работать за время O(log n) и в пространстве O(1).

NOTE: сортировка не обязательна. Работает и без нее
"""

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

n = int(input())
nums = [*map(int, input().split())]

print(n)
print(nums)

# "стандартная" версия
def bin_search(nums):
    l = 0
    r = len(nums)
    while l < r - 1:
        mid = (l + r) >> 1
        if mid & 1 == 1:  # если нечетная позиция ..
            if nums[mid-1] == nums[mid]:  # .. и предыдущий элемент равен текущему
                # ... значит nums[l:mid] - все пары. Отбрасываем левую часть.
                l = mid + 1
            else:
                r = mid
        else:  # если четная позиция ..
            if nums[mid-1] != nums[mid]:  # .. и предыдущий НЕ равен текущему
                # .. значит nums[l:mid-1] - все пары.
                l = mid
            else:
                r = mid
    return nums[l]

# "ускоренная" версия
def bin_search_fast(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) >> 1
        # если mid - четное, то mid ^ 1 = mid + 1 и сравнене со следующим
        # если mid - нечетное, то mid ^ 1 = mid - 1 и сравнение с предыдущим
        if nums[mid ^ 1] != nums[mid]:  # если не совпало, то слева был пропуск
            r = mid  # отбрасываем правую часть nums[mid+1:r]
        else:
            l = mid + 1  # иначе - пропуск где-то справа и отбрасываем nums[l:mid]
    return nums[l]

print(bin_search(nums))
print(bin_search_fast(nums))

