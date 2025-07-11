import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

N = int(input())  # число символов
S = input() # набор больших латинских букв (не обязательно различных)

def solve(n: int, input_str: str) -> str:
    '''
    0. Формируем counts - число вхождений каждой буквы (уже отсортировано)
    1. Перебираем counts, формируем "начало" и "середину":
        - Если число больше 0 (встречалась буква), то
            - Если нечетное и еще не выбрали "середину", 
                - берем 1 такую букву для середины палиндрома
            - добавляем половину (//2) штук текущей буквы к "началу"
    2. Возвращаем конкатенацию из
        "начало" + одна "середина" + развернутое "начало"
    
    Такой подход гарантирует, при прочих равных, выбор первого палиндрома 
    в алфавитном порядке, т.к. неявно эксплуатируется упорядоченность
    символов в кодовой таблице.
    '''
    counts = [0] * 26
    for s in input_str:
        counts[ord(s) - 65] += 1

    middle = None
    left = ''

    for i, c in enumerate(counts):
        if c > 0:
            if c % 2 == 1 and middle is None:
                middle = i
            left = left + ( chr(i+65) * (c//2) )
        
    return left + (chr(middle+65) if middle is not None else '') + left[::-1]
    

print(solve(N, S))