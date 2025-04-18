# один из тестов подает на вход 94702
# по-умолчанию максимальная длина числа 4300 - нехватает
# увеличим максимальную длину числа
import sys
sys.set_int_max_str_digits(5000)

def sum_N(K: int):
    """
    Суммарное число цифр во всех "блоках" до K включительно.

    Блок i - это последовательность цифр всех чисел длины i+1.
    Например:
    Блок 0: 0.1.2.3.4.5.6.7.8.9 - 9 цифр
    Блок 1: 10.11.12.13.14.15.16.17.18.19.20 ... 97.98.99 - 180 цифр, running sum = 189
    Блок 2: 100.101.102.103.104.105.106 ... 997.998.999 - 2700 цифр, running sum = 2889
    Блок 3: 1000.1001.1002.1003.1004.1005 ... 9997.9998.9999 - 36000 цифр, running sum = 38889
    Блок 4: 10000.10001.10002.10003.10004 ... 99997.99998.99999 - 50*9000 цифр, sum = 488889

    Я вывел аналитическую формулу:
    sum = 10**(K+1) * K + (2**(K+4) * 5**(K+1) + 1) // 9

    Но очевидна лексическая формула:
    sum = int( str(K) + ("8" * K) + str(9) )
    """
    # return 10**(K+1) * K + (2**(K+4) * 5**(K+1) + 1) // 9
    return int(str(K) + ("8" * K) + str(9))


def bin_search_left(n, func):
    l, r = 0, n // 10
    while l < r:
        mid = (l + r) >> 1
        if func(mid) < n:
            l = mid + 1
        else:
            r = mid
    return l


def solve(n):

    # левый бин.поиск найдет номер блока в котором находися n-я цифра
    block = bin_search_left(n, sum_N)
    # 
    if block == 0:
        return n
    else:
        # порядковый номер цифры внутри блока block
        n1 = n - sum_N(block-1) - 1  # от 0

        # порядковый номер "числа" вида xxxX (длины block+1) внутри блока
        nn = n1 // (block + 1)
        # само число
        num = 10**block + nn

        # порядковый номер цифры в числе
        nr = n1 % (block + 1)
        
        digit = (num // 10**(block - nr)) % 10
    
    return digit

print(solve(int(input())))