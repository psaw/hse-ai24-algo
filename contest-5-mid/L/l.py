import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида для нахождения коэффициентов `x`, `y` таких, что:
    ax + by = gcd(a, b)
    Возвращает (gcd, x, y)
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return g, x, y


def solve(a, b, c):
    """
    Даны целые числа a, b, c, такие что 1 ≤ a, b, c ≤ 10^9
    Для каждой тройки чисел a, b, c в отдельной строке выведите 
    два целых числа x, y, -10^9 ≤ x, y ≤ 10^9, т.ч. a*x + b*y = c.
    
    Если таких решений несколько, выведите решение с минимально
    возможным неотрицательным целым x. 
    
    Если же решения не существует, выведите в соответствующую строку два нуля.
    """
    # Если c не кратно gcd(a, b), то решения не существует
    g, x0, y0 = extended_gcd(a, b)
    if c % g != 0:
        return 0, 0
    k = c // g
    x0 *= k
    y0 *= k
    
    # Получили одно из решений: 
    # a*x0 + b*y0 = c
    # 
    # Все решения уравнения ax + by = c имеют вид:
    # x = x0 + b_ * t
    # y = y0 - a_ * t
    # где t - целое число
    # и 
    a_ = a // g  # целое, т.к g - НОД
    b_ = b // g  # аналогично
    
    # Найдём t, чтобы x = x0 + b_ * t был минимальным неотрицательным
    t = (-x0) // b_ if b_ != 0 else 0
    while x0 + b_ * t < 0:
        t += 1
    x = x0 + b_ * t
    y = y0 - a_ * t

    # Проверим ограничения
    if not (-10**9 <= x <= 10**9 and -10**9 <= y <= 10**9):
        return 0, 0
        
    return x, y


T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    print(*solve(A, B, C))
