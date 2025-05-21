import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

A, N, M = map(int, input().split())


"""
Задача: Вычислить 1/a + 2/a^2 + 3/a^3 + ... + n/a^n по модулю m

Для a=1, это просто сумма первых n натуральных чисел: n*(n+1)/2

Для a≠1 вычислим "в лоб" в цикле:
S_0 = 1/a
S_{i+1} = S_i + (i+1)/a^(i+1) = S_i + (i+1) * (1/a) * (1/a^i)

Все деления выполняются с использованием модульных обратных величин.

Общая сложность O(n + log m)  # цикл + поиск обратного по модулю 
"""


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


def gcd(a, b):
    """Наибольший общий делитель `a` и `b` (алгоритм Евклида)"""
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида для нахождения коэффициентов `x`, `y` таких, что:
    ax + by = gcd(a, b)
    Возвращает (gcd, x, y)
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    """
    Модульное обратное к `a` по модулю `m` (расширенный алгоритм Евклида).
    Возвращает None, если модульное обратное не существует (когда gcd(a, m) != 1)
    """
    if gcd(a, m) != 1:
        return None  # Модульное обратное не существует

    _, x, _ = extended_gcd(a, m)
    return (x % m + m) % m  # Обеспечиваем положительный результат


def solve(a, n, m):
    """
    Вычисляет (1/a + 2/a^2 + 3/a^3 + ... + n/a^n) % m
    Возвращает -1, если деление невозможно (когда gcd(a, m) > 1)
    """
    # Проверяем, взаимно простые ли a и m
    if gcd(a, m) > 1:
        return -1  # Деление невозможно

    # Особый случай: a = 1
    if a == 1:
        # Когда a=1, сумма равна 1+2+3+...+n = n*(n+1)/2
        return (n * (n + 1) // 2) % m

    # Получаем модульное обратное для a (оно есть, т.к. уже проверили выше)
    inv_a = mod_inverse(a, m)

    result = 0
    current_term = inv_a  # 1/a

    for i in range(1, n + 1):
        # Добавляем i/a^i к результату
        result = (result + i * current_term) % m
        # Вычисляем следующий член: (i+1)/a^(i+1) = (i+1) * (1/a) * (1/a^i)
        current_term = (current_term * inv_a) % m

    return result


print(solve(A, N, M))
