# import os
# import sys

# path = os.path.dirname(os.path.abspath(__file__))
# sys.stdin = open(path + "/input1.txt", "r")


def solve(n: int) -> None:
    """Для заданного N посчитайте количество различных строк длины N, 
    которые содержат только буквы 'X' и 'Y' и не содержат 'YY' как подстроку.

    Решение:
    
    Длина / последний символ X или Y / количество:
        1   2        3               4
    _X: X   XX, YX   XXX, YXX, XYX   XXXX, YXXX, XYXX, XXYX, YXYX
    _Y: Y   XY       XXY, YXY        XXXY, YXXY, XYXY
        2   3        5               8
    
    C_X[i] = C_X[i-1] + C_Y[i-1]
    C_Y[i] = C_X[i-1]

    C_X[i] + C_Y[i] = C_X[i-1] + C_Y[i-1] + C_X[i-1] =
                    = C_X[i-1] + C_X[i-2] + C_X[i-1] = 
                    = C_X[i-1] + C_X[i]
    Да это же числа Фибоначчи!

    ответ[i] = F[i+1]
    """
    dp = [-1] * (n+1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])


N = int(input())
solve(N)
