import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")


#####################################
#                                   #
# Алгоритм Кнута - Морриса - Пратта #
#                                   #
#####################################

P = input()  # шаблон поиска
T = input()  # входная строка


# Вычисление "длин наибольших граней"
def calc_br(s: str) -> list[int]:
    """Вычисление граней строки

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


def calc_brs(s: str) -> list[int]:
    """Вычисление уточненных граней строки s

    Args:
        s (str): Строка

    Returns:
        list[int]: Массив BRS - уточненных граней
    """
    m = len(s)
    br = calc_br(s)
    brs = [0] * m

    for i in range(1, m):
        # тут s[br[i]] - БЕЗ +1 т.к. br[i] - это ДЛИНА, а индексация в s от 0
        if s[br[i]] != (s[i + 1] if i < m - 1 else 0):
            brs[i] = br[i]
        else:
            brs[i] = brs[br[i]]

    return brs


def KMP_search(text: str, pattern: str) -> list[int]:
    """Алгоритм Кнута-Морриса-Пратта для поиска всех вхождений шаблона в строке.

    Args:
        text (str): Строка в которой производится поиск
        pattern (str): Искомая подстрока

    Returns:
        list[int]: Массив номеров позиций с которых начинаются вхождения подстроки.
    """
    n = len(text)
    m = len(pattern)
    brs = calc_brs(pattern)
    k = 0  # число совпадений при текущем "прикладывании" pattern к text
    # оно же - номер сравниваемого символа pattern
    res = []
    for i in range(n):  # идем по буквам text
        # если уже были совпадения, но очередной не совпал
        while k > 0 and pattern[k] != text[i]:
            k = brs[k - 1]  # .. то сдвигаемся на k-brs[k]
        if pattern[k] == text[i]:  # если очередной совпадает
            k += 1  # то переходим к след. символу pattern
            # а цикл сделает переход к i+1 по text
        if k == m:  # если дошли до конца pattern - полное совпадение
            res.append(i - m + 1)  # сохраняем позицию начала совпадения
            k = brs[m - 1]  # и сдвигаем pattern на
    return res


# print(*calc_br(P))
# print(*calc_brs(P))
res = KMP_search(T, P)
print(len(res))
for r in res:
    print(r)
