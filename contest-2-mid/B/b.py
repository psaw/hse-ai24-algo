import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + '/input.txt', 'r')

N, M = map(int, input().split())

nums1 = [*map(int, input().split())]
nums2 = [*map(int, input().split())]

print(N, M)
print(nums1)
print(nums2)

# binary search left
def bin_search_l(a, key):
    l = -1
    r = len(a)
    while l < r-1:
        m = (l + r) // 2
        if a[m] < key:
            l = m
        else:
            r = m
    return r

# binary search right
def bin_search_r(a, key):
    l = -1
    r = len(a)
    while l < r-1:
        m = (l + r) // 2
        if a[m] > key:
            r = m
        else:
            l = m
    return l

for n in nums2:
    l = bin_search_l(nums1, n)
    r = bin_search_r(nums1, n)
    if l > r:
        print(0)
    else:
        print(l+1, r+1)
    