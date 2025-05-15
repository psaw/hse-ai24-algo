import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

n, k = map(int, input().split())
a0, x, y  = map(int, input().split())


def solve1():
    import heapq

    min_heap = []
    
    a_prev = a0
    for i in range(n):
        a_cur = (x * a_prev + y) & 1073741823  # последние 30 бит, т.е. эквив. % 2**30
        print(a_cur, end=" ")
        a_prev = a_cur
        heapq.heappush(min_heap, a_cur)

    print()
    print(min_heap)

    for _ in range(k):
        print(heapq.heappop(min_heap), end=" ")
    print()

def solve2():
    import heapq
    from collections import defaultdict
    num_count = defaultdict(int)  # для подсчета числа вхождений
    min_heap = []  # для упорядоченного перебора ключей словаря

    a_prev = a0
    for i in range(n):  # генерируем числа последовательности
        a_cur = (x * a_prev + y) & (2**30-1)  # это 30 бит, т.е. эквив. % 2**30
        num_count[a_cur] += 1  # считаем сколько раз встретилось
        if num_count[a_cur] == 1:  # добавляем в кучу только первое появление
            heapq.heappush(min_heap, a_cur)
        a_prev = a_cur

    print(num_count)
    print(min_heap)

    out_count = k  # сколько уже вывели (0..k)

    # идем по куче и следим сколько чисел уже вывели
    while min_heap and out_count < k:
        # берем вершину - это текущий очередной последовательности
        a_cur = heapq.heappop(min_heap)
        # проверям сколько раз это число встретилось в последовательности
        if num_count[a_cur] <= k - out_count:
            # если меньше чем еще нужно выводить, то выводим все
            print(*[a_cur] * (num_count[a_cur]), end=" ")
            out_count += num_count[a_cur]
        else:
            # иначе - выводим ровно столько, сколько осталось вывести
            print(*[a_cur] * (k - out_count), end=" ")
            out_count = k

    print()  # для новой строки
    # print(out_count)


def solve3():
    from collections import defaultdict
    num_count = defaultdict(int)  # для подсчета числа вхождений

    a_prev = a0
    max_cur = 0
    in_count = 0
    for i in range(n):  # генерируем числа последовательности
        a_cur = (x * a_prev + y) & (2**30-1)  # это 30 бит, т.е. эквив. % 2**30
        if in_count < k:
            num_count[a_cur] += 1  # считаем сколько раз встретилось
            in_count += 1
            max_cur = max(max_cur, a_cur)
        else:  # ограничиваем размер словаря числом k
            if a_cur < max_cur:
                num_count[a_cur] += 1  # добавляем +1
                num_count[max_cur] -= 1  # и удаляем 1 от максимального
                if num_count[max_cur] == 0:  # если стало 0, то 
                    del num_count[max_cur]   # удаляем запись
                    max_cur = max(num_count.keys())  # и берем новый максимум

        a_prev = a_cur

    # print(num_count)

    out_count = 0  # сколько уже вывели (0..k)
    for a_cur in sorted(num_count.keys()):
    # следим сколько чисел уже вывели
        if out_count >= k:
            break
        # проверям сколько раз это число встретилось в последовательности
        if num_count[a_cur] <= k - out_count:
            # если меньше чем еще нужно выводить, то выводим все
            print(*[a_cur] * (num_count[a_cur]), end=" ")
            out_count += num_count[a_cur]
        else:
            # иначе - выводим ровно столько, сколько осталось вывести
            print(*[a_cur] * (k - out_count), end=" ")
            out_count = k

    print()  # для новой строки
    # print(out_count)

solve3()
