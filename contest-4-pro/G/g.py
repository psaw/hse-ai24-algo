import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

import heapq

N = int(input())
nums  = list(map(int, input().split()))

heapq.heapify(nums)
cost = 0
while nums:
    first = heapq.heappop(nums)
    if nums:
        second = nums[0]
        cost += (first + second) / 20.0
        heapq.heappushpop(nums, first + second)

print(f"{cost:.2f}")