import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

import heapq
from collections import defaultdict

# Идея:
# Вместо реализации биномиальной кучи или реализации 
# дорогостоящей операции поиска заданного ключа в min-куче,
# просто будем поддерживать словарь с удаленными элементами,
# которые будем игнорировать при выводе/извлечении минимума.

# Дополнительная память - O(n) для словаря
# Сложность decreaseKey - O(log n), т.к. это один insert

# Уже несколько раз делали min-кучу.
# Сегодня используем готовую реализацию heapq.

class MultiSet:
    def __init__(self):
        self.min_heap = []  # массив для min-кучи
        self.deleted = defaultdict(int)  # словарь для "удаленных" элементов

    def insert(self, x):
        """Добавление целого x в мультимножество."""
        heapq.heappush(self.min_heap, x)

    def getMin(self):
        """Получение минимального эл-та (без удаления)."""
        # Пропускаем удаленные элементы
        while self.min_heap and self.deleted[self.min_heap[0]] > 0:
            min_val = heapq.heappop(self.min_heap)
            self.deleted[min_val] -= 1

        if not self.min_heap:
            return None  # Вообще не должно произойти (по условиям задачи)
        
        return self.min_heap[0]

    def extractMin(self):
        """Извлечение минимального эл-та."""
        # Пропускаем удаленные элементы
        while self.min_heap and self.deleted[self.min_heap[0]] > 0:
            min_val = heapq.heappop(self.min_heap)
            self.deleted[min_val] -= 1

        if not self.min_heap:
            return None  # Вообще не должно произойти (по условиям задачи)

        return heapq.heappop(self.min_heap)

    def decreaseKey(self, x, y):
        """Уменьшить один элемент, равный x, и сделать его равным y (где y ≤ x)."""
        # Проверять вхождение не будем (дорого), т.к. из условий следует, что x есть в S
        # Отметить x "удаленным" +1 раз
        self.deleted[x] += 1
        # Добавить новое значение y
        heapq.heappush(self.min_heap, y)


if __name__ == "__main__":
    q = int(input())

    s = MultiSet()

    for _ in range(q):
        query = input().split()

        if query[0] == "insert":
            x = int(query[1])
            s.insert(x)

        elif query[0] == "getMin":
            print(s.getMin())

        elif query[0] == "extractMin":
            print(s.extractMin())

        elif query[0] == "decreaseKey":
            x, y = int(query[1]), int(query[2])
            s.decreaseKey(x, y)
