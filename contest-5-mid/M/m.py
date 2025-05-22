import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

# Повысим лимит на глубину рекурсии (по умолчанию = 1000)
sys.setrecursionlimit(3000)


def solve(arr: list[int], idx: int, n: int, t: int, print_counter: int) -> int:
    """Вывести первые t в лексикографическом порядке перестановок n элементов без неподвижных точек.

    Args:
        arr: Предзаполненное начало перестановки (с предыдущего шага)
        idx: Индекс текущей позиции в перестановке, с которой продолжаем заполнение
        n:   Верхний предел диапазона значений элементов перестановки
        t:   Сколько требуется вывести перестановок (первых, в лексикографич. порядке)
        print_counter: Сколько уже вывели перестановок до текущей итерации

    Returns:
        print_counter: Сколько уже вывели перестановок после текущей итерации
    """
    # Debug print to track recursion depth and state
    # print(f"DEBUG: depth={idx}, arr={arr}, counter={print_counter}")

    # Пребираем все значения для текущей позиции idx
    for i in range(n):
        # если значение == номер позиции или уже использовалось, пропускаем
        if i == idx or i + 1 in arr:
            continue
        arr.append(i + 1) # добавляем значение в перестановку (временно)
        if idx == n - 1: # база рекурсии: текущая позиция - последняя 
            print(*arr)         # печатаем
            print_counter += 1  # и увеличиваем счетчик печати
        else:  # иначе - рекурсивно заполняем следующую позицию
            # счетчик передаем и получаем, чтобы "пронести" его через все вызовы рекурсии
            print_counter = solve(arr, idx + 1, n, t, print_counter)
        arr.pop()  # удаляем текущий (последний) элемент, чтобы перейти к следующему
        if print_counter >= t:  # если все напечатали, то выходим
            return print_counter

    return print_counter


N, T = map(int, input().split())

solve([], 0, N, T, 0)
