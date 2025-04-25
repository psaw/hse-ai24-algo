import sys
import os
import math

test_num = 20
path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + f'/input{test_num}.txt', 'r')
answers20 = open(path + f'/answers{test_num}.txt', 'r').read()
answers = answers20.split("\n")


def ff(r ,g , b):
    return (r-g)**2 + (r-b)**2 + (g-b)**2

def gems(Nr, Ng, Nb, Wr, Wg, Wb):
    """
    Наивное решение - полный перебор
    Слишком медленно - O(n^3)
    """
    f_min = math.inf
    for r in Wr:
        for g in Wg:
            for b in Wb:
                f = (r-g)**2 + (r-b)**2 + (g-b)**2
                if f < f_min:
                    f_min = f
                    min_r, min_g, min_b = r, g, b
    return min_r, min_g, min_b


def gems7(Nr, Ng, Nb, Wr, Wg, Wb):
    """
    Проход по тройкам камней так, чтобы поддерживать минимально возможное
    значение суммы квадратов разностей (СКР).

    Обоснование:
    Из конкретной точки смещаемся в ближайшую точку (+1 координата), 
    в направлении (по координате) минимальной частной производной f.

    1. Отсортируем массивы
    2. Используем 3 указателя (i, j, k) для прохода по массивам
    3. Начинаем с нулевых индексов (начала массивов) и "огромной" суммы
    4. Вычисляем СКР для текущих элементов, сравниваем с текущим минимумом.
    5. Если меньше, то запоминаем текущие элементы и СКР как новые минимальные.
    6. Шаг:
        - проверяем значения СКР при замене ОДНОГО из камней
        - сдвигаем индекс того цвета, где новый камень дает минимум.
        (если одинаковые, то приоритет - i, j, k, но это не важно)
    7. Когда все указатели достигнуи конца массива - конец поиска.

    Очень похоже на градиентный спуск (до момента прохождения минимума)
    """
    Wr = sorted(Wr)  # предположим, что применили одну из сортировок
    Wg = sorted(Wg)  # из прошлых занятий/задач
    Wb = sorted(Wb)  # сложностью O(n log n)
    f_min = math.inf
    i, j, k = 0, 0, 0  # указатели на текущие элементы
    min_r, min_g, min_b = Wr[i], Wg[j], Wb[k]



    def update_f(r, g, b, min_r, min_g, min_b, f_min):
        _f = ff(r ,g , b)
        if _f < f_min:  # если нашли меньшую сумму - запоминаем
            return r, g, b, _f
        else:
            return min_r, min_g, min_b, f_min

    while i < Nr and j < Ng and k < Nb:
        r, g, b = Wr[i], Wg[j], Wb[k]  # текущие элементы
        min_r, min_g, min_b, f_min = update_f(r, g, b, min_r, min_g, min_b, f_min)

        # оценим новые значеия СКР при сдвиге одного камня
        df_dr = ff(Wr[i+1], g, b) if i < Nr - 1 else math.inf
        df_dg = ff(r, Wg[j+1], b) if j < Ng - 1 else math.inf
        df_db = ff(r, g, Wb[k+1]) if k < Nb - 1 else math.inf

        # возьмем минимум
        df_min = min(df_dr, df_dg, df_db)

        # и сдвинем тот камень, который дает минимум
        if df_min == df_dr:
            i += 1
        elif df_min == df_dg:
            j += 1
        else:
            k += 1

        # все 3 индекса равны inf только тогда, когда все дошли до конца
        # в этом случае первый же +=1 приведет к завершению цикла while

    return min_r, min_g, min_b   


T = int(input())  # число под-тестов
for t in range(T):

    Nr, Ng, Nb = map(int, input().split())
    Wr = [*map(int, input().split())]
    Wg = [*map(int, input().split())]
    Wb = [*map(int, input().split())]
    ans = [*map(int, answers[t].split())]

    res = gems7(Nr, Ng, Nb, Wr, Wg, Wb)

    if ans[0]==res[0] and ans[1]==res[1] and ans[2]==res[2]:
    # if ff(*ans) == ff(*res):
        print(".", end="")
    else:
        print(f"\nt={t}")
        print("ans:", *ans, ", f =", ff(*ans))
        print("res:", *res, ", f =", ff(*res))
