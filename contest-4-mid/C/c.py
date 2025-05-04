import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

N = int(input())
T = list(map(int, input().split()))

def solve(n: int, t: list):
    stack = []  #  для временного хранения индексов "кандидатов"
    res = []  # для сбора результата
    for i in range(len(t)-1, -1, -1):  # идем с конца

        # если есть "кандидаты", то с конца удаляем те, которые меньше текущего
        # они непонадобятся дальше, т.к. текущий и больше и ближе к следующим
        while (stack and t[stack[-1]] <= t[i]):
            stack.pop()
        
        if stack:
            # если еще остался кандидат, то сохраняем в результат
            # расстояние (т.е. разницу индексов кандитата и текущего)
            res.append(stack[-1] - i)
        else:
            # если кандидатов нет, то сохраняем 0
            res.append(0)
        
        # добавляем текущий в кандидаты для следующих
        stack.append(i)
    
    print(*res[::-1])


solve(N, T)