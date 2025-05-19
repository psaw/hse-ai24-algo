from typing import TypeVar, Generic, List, Iterable, Optional, Union, Iterator

T = TypeVar("T")


class Heap(Generic[T]):
    """
    Реализация бинарной макс-кучи на Python.
    Это параметрический (обобщенный) класс, который может хранить объекты любого типа T.
    Для сравнения элементов используется только оператор < (соответствует методу __lt__ в Python).
    """

    def __init__(
        self,
        *args: Union[T, Iterable[T], Iterator[T]],
        end_iterator: Optional[Iterator[T]] = None,
    ):
        """
        Поддерживает несколько шаблонов конструктора:
        - Конструктор по умолчанию: Heap()
        - Конструктор с итератором: Heap(iterable)
        - Конструктор со списком инициализации: Heap(value1, value2, ...)
        - Конструктор с двумя итераторами: Heap(begin_iterator, end_iterator=end_iterator), где
            - begin_iterator: итерируемый объект, предоставляющий элементы для включения
            - end_iterator: итерируемый объект, первый элемент которого обозначает точку остановки
        """
        self._data: List[T] = []

        if end_iterator is not None and len(args) == 1:
            # Конструктор с двумя итераторами (начало и конец)
            begin_iterator = args[0]

            self._data = []

            # Получаем значение остановки (первый элемент end_iterator)
            try:
                end_iter = iter(end_iterator)
                stop_value = next(end_iter, None)

                # Перебираем begin_iterator и добавляем элементы, пока не достигнем stop_value
                for item in begin_iterator: # type: ignore
                    if item == stop_value:
                        break
                    self._data.append(item)
            except (StopIteration, TypeError):
                # Обрабатываем случаи, когда итераторы исчерпаны или несравнимы
                pass

            self._heapify()
        elif len(args) == 1 and hasattr(args[0], "__iter__"):
            # Конструктор с итерируемым объектом (эквивалент конструктора с итератором в C++)
            self._data = list(args[0]) # type: ignore
            self._heapify()
        elif len(args) > 0:
            # Конструктор с переменным числом аргументов (эквивалент списка инициализации в C++)
            self._data = list(args) # type: ignore
            self._heapify()

    def __copy__(self) -> "Heap[T]":
        """
        Эквивалент конструктора копирования.
        """
        new_heap = Heap[T]()
        new_heap._data = self._data.copy()
        return new_heap

    def copy(self) -> "Heap[T]":
        """
        Возвращает копию кучи.
        """
        return self.__copy__()

    def __deepcopy__(self, memo) -> "Heap[T]":
        """
        Поддержка глубокого копирования.
        """
        import copy

        new_heap = Heap[T]()
        new_heap._data = copy.deepcopy(self._data, memo)
        return new_heap

    def __del__(self):
        """
        Эквивалент деструктора.
        """
        self._data.clear()

    def size(self) -> int:
        """
        Возвращает количество элементов в куче.
        """
        return len(self._data)

    def empty(self) -> bool:
        """
        Возвращает True, если куча пуста, иначе False.
        """
        return len(self._data) == 0

    def insert(self, value: T) -> None:
        """
        Добавляет элемент в кучу.
        """
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def extract(self) -> T:
        """
        Удаляет и возвращает наибольший элемент из кучи.
        Вызывает IndexError, если куча пуста.
        """
        if self.empty():
            raise IndexError("Cannot extract from an empty heap")

        # Получаем максимальное значение (корень кучи)
        max_value = self._data[0]

        # Заменяем корень последним элементом
        last_element = self._data.pop()

        if self._data:  # Если куча не пуста после удаления элемента
            self._data[0] = last_element
            self._sift_down(0)

        return max_value

    def _parent(self, index: int) -> int:
        """
        Возвращает индекс родителя для заданного индекса.
        """
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        """
        Возвращает индекс левого потомка для заданного индекса.
        """
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        """
        Возвращает индекс правого потомка для заданного индекса.
        """
        return 2 * index + 2

    def _has_parent(self, index: int) -> bool:
        """
        Возвращает True, если узел с заданным индексом имеет родителя.
        """
        return index > 0

    def _has_left_child(self, index: int) -> bool:
        """
        Возвращает True, если узел с заданным индексом имеет левого потомка.
        """
        return self._left_child(index) < len(self._data)

    def _has_right_child(self, index: int) -> bool:
        """
        Возвращает True, если узел с заданным индексом имеет правого потомка.
        """
        return self._right_child(index) < len(self._data)

    def _sift_up(self, index: int) -> None:
        """
        Перемещает элемент с заданным индексом вверх до его правильной позиции.
        """
        while self._has_parent(index):
            parent_idx = self._parent(index)
            # Используем только оператор < для сравнения, как указано в задании
            if self._data[parent_idx] < self._data[index]: # type: ignore
                # Меняем местами с родителем, если родитель меньше
                self._data[parent_idx], self._data[index] = (
                    self._data[index],
                    self._data[parent_idx],
                )
                index = parent_idx
            else:
                break

    def _sift_down(self, index: int) -> None:
        """
        Перемещает элемент с заданным индексом вниз до его правильной позиции.
        """
        largest = index

        while True:
            if self._has_left_child(index):
                left_idx = self._left_child(index)
                # Используем только оператор < для сравнения, как указано в задании
                if self._data[largest] < self._data[left_idx]: # type: ignore
                    largest = left_idx

            if self._has_right_child(index):
                right_idx = self._right_child(index)
                # Используем только оператор < для сравнения, как указано в задании
                if self._data[largest] < self._data[right_idx]: # type: ignore
                    largest = right_idx

            if largest != index:
                # Меняем местами с наибольшим потомком
                self._data[index], self._data[largest] = (
                    self._data[largest],
                    self._data[index],
                )
                index = largest
            else:
                break

    def _heapify(self) -> None:
        """
        Строит кучу из неупорядоченного массива.
        """
        # Начинаем с последнего не листового узла и просеиваем вниз
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._sift_down(i)

########################################

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(path + "/input1.txt", "r")

N = int(input())

h = Heap()

for _ in range(N):
    inp = input().split()
    match len(inp):
        case 1:
            print(h.extract())
        case 2:
            h.insert(int(inp[1]))
