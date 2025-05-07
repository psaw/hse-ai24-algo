import unittest
from heap import Heap


# Пользовательский класс для тестирования кучи с пользовательскими объектами
class Person:
    """
    Пример пользовательского класса, который определяет свой порядок через метод __lt__.
    Это демонстрирует, как класс Heap может работать с любым типом, реализующим __lt__.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __lt__(self, other: "Person") -> bool:
        """
        Определяет порядок на основе возраста (более молодой человек "меньше" более старого).
        Этот метод используется классом Heap для сравнений.
        """
        return self.age < other.age

    def __eq__(self, other):
        """
        Определяет равенство для целей тестирования
        """
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

    def __repr__(self) -> str:
        """
        Строковое представление для отладки.
        """
        return f"Person(name='{self.name}', age={self.age})"


class HeapTest(unittest.TestCase):
    """
    Комплексный набор тестов для класса Heap, организованный по уровням сложности.
    """

    ##########################################
    # УРОВЕНЬ 1: Тесты базовых операций кучи #
    ##########################################

    def test_empty_heap(self):
        """Тестирование базовых свойств пустой кучи"""
        h = Heap()
        self.assertEqual(h.size(), 0)
        self.assertTrue(h.empty())

        # Проверка, что извлечение из пустой кучи вызывает IndexError
        with self.assertRaises(IndexError):
            h.extract()

    def test_insert_extract(self):
        """Тестирование базовых операций вставки и извлечения"""
        h = Heap()

        # Вставка элементов
        h.insert(5)
        h.insert(3)
        h.insert(8)
        h.insert(1)
        h.insert(10)

        # Проверка размера и статуса пустоты
        self.assertEqual(h.size(), 5)
        self.assertFalse(h.empty())

        # Извлечение элементов и проверка свойства макс-кучи
        self.assertEqual(h.extract(), 10)
        self.assertEqual(h.extract(), 8)
        self.assertEqual(h.extract(), 5)
        self.assertEqual(h.extract(), 3)
        self.assertEqual(h.extract(), 1)

        # Куча должна быть пустой после всех извлечений
        self.assertTrue(h.empty())
        self.assertEqual(h.size(), 0)

    ###########################################
    # УРОВЕНЬ 2: Тесты вариантов конструктора #
    ###########################################

    def test_initializer_list_constructor(self):
        """Тестирование конструктора с переменным числом аргументов (список инициализации)"""
        h = Heap(5, 3, 8, 1, 10)

        self.assertEqual(h.size(), 5)
        self.assertFalse(h.empty())

        # Извлечение элементов и проверка свойства макс-кучи
        self.assertEqual(h.extract(), 10)
        self.assertEqual(h.extract(), 8)
        self.assertEqual(h.extract(), 5)
        self.assertEqual(h.extract(), 3)
        self.assertEqual(h.extract(), 1)

        self.assertTrue(h.empty())

    def test_iterable_constructor(self):
        """Тестирование конструктора с итерируемым объектом"""
        h = Heap([7, 2, 9, 4, 1])

        self.assertEqual(h.size(), 5)
        self.assertFalse(h.empty())

        # Извлечение элементов и проверка свойства макс-кучи
        self.assertEqual(h.extract(), 9)
        self.assertEqual(h.extract(), 7)
        self.assertEqual(h.extract(), 4)
        self.assertEqual(h.extract(), 2)
        self.assertEqual(h.extract(), 1)

        self.assertTrue(h.empty())

    ##########################################
    # УРОВЕНЬ 3: Тесты семантики копирования #
    ##########################################

    def test_copy(self):
        """Тестирование конструктора копирования и независимости копий"""
        original = Heap(10, 5, 15, 3, 8)
        copied = original.copy()

        # Изначально обе кучи должны иметь одинаковый размер
        self.assertEqual(original.size(), 5)
        self.assertEqual(copied.size(), 5)

        # Изменение оригинала не должно влиять на копию
        original.insert(20)
        self.assertEqual(original.size(), 6)
        self.assertEqual(copied.size(), 5)

        # Извлечение из оригинала и проверка свойства макс-кучи
        self.assertEqual(original.extract(), 20)
        self.assertEqual(original.extract(), 15)
        self.assertEqual(original.extract(), 10)
        self.assertEqual(original.extract(), 8)
        self.assertEqual(original.extract(), 5)
        self.assertEqual(original.extract(), 3)

        # Извлечение из копии и проверка свойства макс-кучи
        self.assertEqual(copied.extract(), 15)
        self.assertEqual(copied.extract(), 10)
        self.assertEqual(copied.extract(), 8)
        self.assertEqual(copied.extract(), 5)
        self.assertEqual(copied.extract(), 3)

    #########################################
    # УРОВЕНЬ 4: Тесты конструктора с итераторами #
    #########################################

    def test_iterator_constructor_with_list_slices(self):
        """Тестирование конструктора с двумя итераторами с использованием срезов списка"""
        data = [5, 3, 8, 1, 10, 6, 4, 7, 2, 9]

        # Создание кучи с элементами от индекса 0 до 5 (не включая 5)
        begin_slice = data[:5]  # [5, 3, 8, 1, 10]
        end_slice = data[5:]  # [6, 4, 7, 2, 9] - 6 это точка остановки

        h = Heap(begin_slice, end_iterator=iter(end_slice))

        self.assertEqual(h.size(), 5)

        # Извлечение элементов и проверка свойства макс-кучи
        self.assertEqual(h.extract(), 10)
        self.assertEqual(h.extract(), 8)
        self.assertEqual(h.extract(), 5)
        self.assertEqual(h.extract(), 3)
        self.assertEqual(h.extract(), 1)

    def test_iterator_constructor_with_range(self):
        """Тестирование конструктора с двумя итераторами с использованием объектов range"""
        begin_range = range(1, 6)  # 1, 2, 3, 4, 5
        end_range = range(6, 10)  # 6, 7, 8, 9 - 6 это точка остановки

        h = Heap(begin_range, end_iterator=iter(end_range))

        self.assertEqual(h.size(), 5)

        # Извлечение элементов и проверка свойства макс-кучи
        self.assertEqual(h.extract(), 5)
        self.assertEqual(h.extract(), 4)
        self.assertEqual(h.extract(), 3)
        self.assertEqual(h.extract(), 2)
        self.assertEqual(h.extract(), 1)

    ###############################################
    # УРОВЕНЬ 5: Тесты с пользовательским классом #
    ###############################################

    def test_custom_class_basic(self):
        """Тестирование кучи с объектами пользовательского класса - базовые операции"""
        # Создание нескольких объектов Person
        alice = Person("Alice", 30)
        bob = Person("Bob", 25)
        charlie = Person("Charlie", 40)
        david = Person("David", 35)
        eve = Person("Eve", 28)

        # Тестирование конструктора по умолчанию и вставки
        h = Heap[Person]()
        h.insert(alice)
        h.insert(bob)
        h.insert(charlie)
        h.insert(david)
        h.insert(eve)

        self.assertEqual(h.size(), 5)
        self.assertFalse(h.empty())

        # Извлечение элементов и проверка свойства макс-кучи (по возрасту)
        self.assertEqual(h.extract(), charlie)  # Чарли, 40
        self.assertEqual(h.extract(), david)  # Дэвид, 35
        self.assertEqual(h.extract(), alice)  # Алиса, 30
        self.assertEqual(h.extract(), eve)  # Ева, 28
        self.assertEqual(h.extract(), bob)  # Боб, 25

        self.assertTrue(h.empty())

    def test_custom_class_constructors(self):
        """Тестирование кучи с объектами пользовательского класса - различные конструкторы"""
        # Создание нескольких объектов Person
        alice = Person("Alice", 30)
        bob = Person("Bob", 25)
        charlie = Person("Charlie", 40)
        david = Person("David", 35)
        eve = Person("Eve", 28)

        # Тестирование конструктора с итерируемым объектом
        h1 = Heap[Person]([alice, bob, charlie, david, eve])
        self.assertEqual(h1.size(), 5)

        # Извлечение элементов и проверка свойства макс-кучи (по возрасту)
        self.assertEqual(h1.extract(), charlie)  # Чарли, 40
        self.assertEqual(h1.extract(), david)  # Дэвид, 35
        self.assertEqual(h1.extract(), alice)  # Алиса, 30
        self.assertEqual(h1.extract(), eve)  # Ева, 28
        self.assertEqual(h1.extract(), bob)  # Боб, 25

        # Тестирование конструктора с переменным числом аргументов
        h2 = Heap(alice, bob, charlie, david, eve)
        self.assertEqual(h2.size(), 5)

        # Извлечение элементов и проверка свойства макс-кучи (по возрасту)
        self.assertEqual(h2.extract(), charlie)  # Чарли, 40
        self.assertEqual(h2.extract(), david)  # Дэвид, 35
        self.assertEqual(h2.extract(), alice)  # Алиса, 30
        self.assertEqual(h2.extract(), eve)  # Ева, 28
        self.assertEqual(h2.extract(), bob)  # Боб, 25

    def test_custom_class_copy(self):
        """Тестирование кучи с объектами пользовательского класса - семантика копирования"""
        # Создание нескольких объектов Person
        alice = Person("Alice", 30)
        bob = Person("Bob", 25)
        charlie = Person("Charlie", 40)
        david = Person("David", 35)
        eve = Person("Eve", 28)

        # Тестирование копирования
        h1 = Heap(alice, bob, charlie, david, eve)
        h2 = h1.copy()

        self.assertEqual(h1.size(), 5)
        self.assertEqual(h2.size(), 5)

        # Извлечение из оригинала
        self.assertEqual(h1.extract(), charlie)  # Чарли, 40
        self.assertEqual(h1.extract(), david)  # Дэвид, 35
        self.assertEqual(h1.extract(), alice)  # Алиса, 30
        self.assertEqual(h1.extract(), eve)  # Ева, 28
        self.assertEqual(h1.extract(), bob)  # Боб, 25

        # Извлечение из копии
        self.assertEqual(h2.extract(), charlie)  # Чарли, 40
        self.assertEqual(h2.extract(), david)  # Дэвид, 35
        self.assertEqual(h2.extract(), alice)  # Алиса, 30
        self.assertEqual(h2.extract(), eve)  # Ева, 28
        self.assertEqual(h2.extract(), bob)  # Боб, 25

    def test_custom_class_iterator_constructor(self):
        """Тестирование кучи с объектами пользовательского класса - конструктор с двумя итераторами"""
        # Создание нескольких объектов Person
        people_begin = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 40)]

        people_end = [
            Person("David", 35),  # Это точка остановки
            Person("Eve", 28),
        ]

        h = Heap(people_begin, end_iterator=iter(people_end))

        self.assertEqual(h.size(), 3)

        # Извлечение элементов и проверка свойства макс-кучи (по возрасту)
        self.assertEqual(h.extract(), Person("Charlie", 40))
        self.assertEqual(h.extract(), Person("Alice", 30))
        self.assertEqual(h.extract(), Person("Bob", 25))


if __name__ == "__main__":
    unittest.main()
