"""
На прямой расположены стойла, в которые необходимо расставить коров так,
чтобы минимальное расcтояние между коровами было как можно больше.
"""


import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

N, K = map(int, input().split())  # количество стойл и коров

nums = [*map(int, input().split())]  # координаты стойл

print(N, K)
print(nums)

def check(nums, N, K, l):
    count = 1
    last_pos = nums[0]
    
    for pos in nums[1:]:
        if pos - last_pos >= l:
            count += 1
            last_pos = pos
    
    return count >= K

l = 1
r = nums[-1] - nums[0] + 1

while l < r - 1:
    mid = (l + r) // 2
    if check(nums, N, K, mid):  # правосторонний бинарный поиск
        l = mid
    else:
        r = mid
print(l)




