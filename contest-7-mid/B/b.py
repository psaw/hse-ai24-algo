import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


##################################
#                                #
# Префикс-функция (mlds-1)       #
#                                #
##################################

S = input()  # входная строка


def calc_br(s: str) -> list[int]:
    """Вычисление "длин наибольших граней"

    Args:
        s (str): Входная строка

    Returns:
        list[int]: Массив BR - длин наибольших граней подстрок длины i
                   (индексация от 1 до len(s))
    """
    m = len(s)
    br = [0] * m

    for i in range(1, m):
        j = br[i - 1]

        # если символ не совпадает, переходим к предыдущей грани
        while j > 0 and s[i] != s[j]:
            j = br[j - 1]
        if s[i] == s[j]:
            j += 1
        br[i] = j

    return br


print(*calc_br(S))
