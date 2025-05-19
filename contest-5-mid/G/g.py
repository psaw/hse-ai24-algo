import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

N = int(input())

def hanoi(n, k, m):
    if n == 0: # База индукции 
        return
    p = 6 - k - m  # номер "свободного" стержня
    hanoi(n-1, k, p)
    print(n, k, m)
    hanoi(n-1, p, m)


hanoi(N, 1, 3)
