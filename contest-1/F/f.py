""" 
Вася придумал новую метрику по которой он может делать выводы о том,
насколько отсортирована последовательность натуральных чисел. 
Для этого он находит длину наибольшей монотонной подпоследовательности. 
Монотонной подпоследовательностью считается такой фрагмент 
последовательности, в котором все элементы располагаются 
либо в порядке возрастания, либо в порядке убывания. 
Напишите программу, вычисляющую эту метрику.

Решение:
Отслеживаем направление изменения чисел.
При равенстве
- считаем что это новая последовательность из 1 элемента.
- текущая длина = 1
При сохранении направления
- это продолжение последовательности
- текущая длина += 1.
При изменении направления
- это второй элемент последовательности
- текущая длина = 2.
Обновляем текущий максимум длины.
"""

from enum import Enum
import sys
sys.stdin = open(sys.path[0] + "/input.txt", 'r')

class Dir(Enum):
    UP = 1
    DOWN = 2
    FLAT = 3

max_len = 0
cur_len = 0
prev_n = None

while True:
    n = int(input())
    if n == 0:
        break
    if prev_n is None:
        prev_n = n
        cur_len += 1
        dir = Dir.FLAT
    else:
        if n == prev_n:
            cur_len = 1
            dir = Dir.FLAT
        elif n > prev_n:
            match dir:
                case Dir.UP | Dir.FLAT:
                    cur_len += 1
                case Dir.DOWN:
                    cur_len = 2
            dir = Dir.UP
        else:
            match dir:
                case Dir.DOWN | Dir.FLAT:
                    cur_len += 1
                case Dir.UP:
                    cur_len = 2
            dir = Dir.DOWN
        prev_n = n
    max_len = max(max_len, cur_len)

print(max_len)

