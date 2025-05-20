import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

A, B, C, D = map(int, input().split())

def bin_pow_mod(a, b, p):
    res = 1
    while b:
        if b % 2:
            res = (res * a) % p
        a = (a * a) % p
        b //= 2
    return res

def solve(a, b, c, d):
    # 1e9 + 7 - довольно известное простое число
    p = int(1e9 + 7)
    top = (a*d + b*c) % p
    # по теореме Ферма a**(-1) = a**(p-2) mod p , где p - простое число
    bot = bin_pow_mod(b*d, p-2, p)

    return (top * bot) % p


print(solve(A, B, C, D))
