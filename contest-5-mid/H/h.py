import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

A = float(input())
N = int(input())

def bin_power(a, n):
    if n == 0: # База индукции 
        return 1
    if n == 1:
        return a
    if n & 1 == 1:
        return a * bin_power(a, n - 1)
    
    # шаг индукции
    return bin_power(a * a, n // 2)


print(bin_power(A, N))
