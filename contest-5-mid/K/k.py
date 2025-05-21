import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def bin_pow_mod(a, b, p):
    """
    Бинарное возведение в степень по модулю `p`
    Временная сложность: `O(log b)`
    """
    res = 1
    while b:
        if b % 2:
            res = (res * a) % p
        a = (a * a) % p
        b //= 2
    return res


"""Задача:
Найти для натурального числа `a` такое натуральное число `x`,
не большее 10^9+9, что a*x - 1 делится на 10^9+9.

Решение:
1. 10^9+9 - простое число вида 10n+9 (OEIS A030433, https://oeis.org/A030433)
2. Условия "a * x - 1 делится на 10^9+9" означает, что
a*x = 1 (mod 10^9+9)
3. То есть, x = a^(-1) (mod 10^9+9)
4. По Малой теореме Ферма :
a^(-1) = a^(p-2) (mod p)
"""

T = int(input())
p = int(1e9 + 9)

for _ in range(T):
    A = int(input())
    print(bin_pow_mod(A, p - 2, p))
