# import os
# import sys

# path = os.path.dirname(os.path.abspath(__file__))
# sys.stdin = open(path + "/input1.txt", "r")


def solve(n: int) -> None:
    """Имеется калькулятор, который выполняет следующие операции:

    - Умножить число X на 2.
    - Умножить число X на 3.
    - Прибавить к числу X единицу.
    
    Определите, какое наименьшее количество операций требуется, 
    чтобы получить из числа 1 число N.
    """
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(2, n+1):
        if i % 6 == 0:
            dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i-1], dp[i//3]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i-1], dp[i//2]) + 1
        else:
            dp[i] = dp[i-1] + 1
    print(dp[n])  
    # print(*dp)
    res = [n]
    i = n
    while i>1:  # восстановление пути
        if i % 6 == 0:
            m = min(dp[i-1], dp[i//2], dp[i//3])
            if m == dp[i//3]:
                res.append(i//3)
                i //= 3
            elif m == dp[i//2]:
                res.append(i//2)
                i //= 2
            else:
                res.append(i-1)
                i -= 1
        elif i % 3 == 0:
            m = min(dp[i-1], dp[i//3])
            if m == dp[i//3]:
                res.append(i//3)
                i //= 3
            else:
                res.append(i-1)
                i -= 1
        elif i % 2 == 0:
            m = min(dp[i-1], dp[i//2])
            if m == dp[i//2]:
                res.append(i//2)
                i //= 2
            else:
                res.append(i-1)
                i -= 1
        else:
            res.append(i-1)
            i -= 1
    
    print(*res[::-1])


N = int(input())
solve(N)
