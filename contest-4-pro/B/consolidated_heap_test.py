import unittest
from heap import Heap


# Custom class for testing heap with custom objects
class Person:
    """
    Example custom class that defines its own ordering via the __lt__ method.
    This demonstrates how the Heap class can work with any type that implements __lt__.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __lt__(self, other: "Person") -> bool:
        """
        Define ordering based on age (younger person is "less than" older person).
        This method is used by the Heap class for comparisons.
        """
        return self.age < other.age

    def __eq__(self, other):
        """
        Define equality for testing purposes
        """
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

    def __repr__(self) -> str:
        """
        String representation for debugging.
        """
        return f"Person(name='{self.name}', age={self.age})"


class HeapTest(unittest.TestCase):
    """
    Comprehensive test suite for the Heap class, organized by complexity level.
    """

    #########################################
    # LEVEL 1: Basic Heap Operations Tests  #
    #########################################

    def test_empty_heap(self):
        """Test basic properties of an empty heap"""
        h = Heap()
        self.assertEqual(h.size(), 0)
        self.assertTrue(h.empty())

        # Test extract from empty heap raises IndexError
        with self.assertRaises(IndexError):
            h.extract()

    def test_insert_extract(self):
        """Test basic insert and extract operations"""
        h = Heap()

        # Insert elements
        h.insert(5)
        h.insert(3)
        h.insert(8)
        h.insert(1)
        h.insert(10)

        # Check size and empty status
        self.assertEqual(h.size(), 5)
        self.assertFalse(h.empty())

        # Extract elements and verify max-heap property
        self.assertEqual(h.extract(), 10)
        self.assertEqual(h.extract(), 8)
        self.assertEqual(h.extract(), 5)
        self.assertEqual(h.extract(), 3)
        self.assertEqual(h.extract(), 1)

        # Heap should be empty after all extractions
        self.assertTrue(h.empty())
        self.assertEqual(h.size(), 0)

    #########################################
    # LEVEL 2: Constructor Variants Tests   #
    #########################################

    def test_initializer_list_constructor(self):
        """Test constructor with variable arguments (initializer list)"""
        h = Heap(5, 3, 8, 1, 10)

        self.assertEqual(h.size(), 5)
        self.assertFalse(h.empty())

        # Extract elements and verify max-heap property
        self.assertEqual(h.extract(), 10)
        self.assertEqual(h.extract(), 8)
        self.assertEqual(h.extract(), 5)
        self.assertEqual(h.extract(), 3)
        self.assertEqual(h.extract(), 1)

        self.assertTrue(h.empty())

    def test_iterable_constructor(self):
        """Test constructor with an iterable"""
        h = Heap([7, 2, 9, 4, 1])

        self.assertEqual(h.size(), 5)
        self.assertFalse(h.empty())

        # Extract elements and verify max-heap property
        self.assertEqual(h.extract(), 9)
        self.assertEqual(h.extract(), 7)
        self.assertEqual(h.extract(), 4)
        self.assertEqual(h.extract(), 2)
        self.assertEqual(h.extract(), 1)

        self.assertTrue(h.empty())

    #########################################
    # LEVEL 3: Copy Semantics Tests         #
    #########################################

    def test_copy(self):
        """Test copy constructor and independence of copies"""
        original = Heap(10, 5, 15, 3, 8)
        copied = original.copy()

        # Both heaps should have the same size initially
        self.assertEqual(original.size(), 5)
        self.assertEqual(copied.size(), 5)

        # Modifying the original should not affect the copy
        original.insert(20)
        self.assertEqual(original.size(), 6)
        self.assertEqual(copied.size(), 5)

        # Extract from original and verify max-heap property
        self.assertEqual(original.extract(), 20)
        self.assertEqual(original.extract(), 15)
        self.assertEqual(original.extract(), 10)
        self.assertEqual(original.extract(), 8)
        self.assertEqual(original.extract(), 5)
        self.assertEqual(original.extract(), 3)

        # Extract from copy and verify max-heap property
        self.assertEqual(copied.extract(), 15)
        self.assertEqual(copied.extract(), 10)
        self.assertEqual(copied.extract(), 8)
        self.assertEqual(copied.extract(), 5)
        self.assertEqual(copied.extract(), 3)

    #########################################
    # LEVEL 4: Iterator Constructor Tests   #
    #########################################

    def test_iterator_constructor_with_list_slices(self):
        """Test two iterators constructor with list slices"""
        data = [5, 3, 8, 1, 10, 6, 4, 7, 2, 9]

        # Create a heap with elements from index 0 to 5 (not including 5)
        begin_slice = data[:5]  # [5, 3, 8, 1, 10]
        end_slice = data[5:]  # [6, 4, 7, 2, 9] - 6 is the stopping point

        h = Heap(begin_slice, end_iterator=end_slice)

        self.assertEqual(h.size(), 5)

        # Extract elements and verify max-heap property
        self.assertEqual(h.extract(), 10)
        self.assertEqual(h.extract(), 8)
        self.assertEqual(h.extract(), 5)
        self.assertEqual(h.extract(), 3)
        self.assertEqual(h.extract(), 1)

    def test_iterator_constructor_with_range(self):
        """Test two iterators constructor with range objects"""
        begin_range = range(1, 6)  # 1, 2, 3, 4, 5
        end_range = range(6, 10)  # 6, 7, 8, 9 - 6 is the stopping point

        h = Heap(begin_range, end_iterator=end_range)

        self.assertEqual(h.size(), 5)

        # Extract elements and verify max-heap property
        self.assertEqual(h.extract(), 5)
        self.assertEqual(h.extract(), 4)
        self.assertEqual(h.extract(), 3)
        self.assertEqual(h.extract(), 2)
        self.assertEqual(h.extract(), 1)

    #########################################
    # LEVEL 5: Custom Class Tests           #
    #########################################

    def test_custom_class_basic(self):
        """Test heap with custom class objects - basic operations"""
        # Create some Person objects
        alice = Person("Alice", 30)
        bob = Person("Bob", 25)
        charlie = Person("Charlie", 40)
        david = Person("David", 35)
        eve = Person("Eve", 28)

        # Test default constructor and insert
        h = Heap[Person]()
        h.insert(alice)
        h.insert(bob)
        h.insert(charlie)
        h.insert(david)
        h.insert(eve)

        self.assertEqual(h.size(), 5)
        self.assertFalse(h.empty())

        # Extract elements and verify max-heap property (by age)
        self.assertEqual(h.extract(), charlie)  # Charlie, 40
        self.assertEqual(h.extract(), david)  # David, 35
        self.assertEqual(h.extract(), alice)  # Alice, 30
        self.assertEqual(h.extract(), eve)  # Eve, 28
        self.assertEqual(h.extract(), bob)  # Bob, 25

        self.assertTrue(h.empty())

    def test_custom_class_constructors(self):
        """Test heap with custom class objects - different constructors"""
        # Create some Person objects
        alice = Person("Alice", 30)
        bob = Person("Bob", 25)
        charlie = Person("Charlie", 40)
        david = Person("David", 35)
        eve = Person("Eve", 28)

        # Test iterable constructor
        h1 = Heap[Person]([alice, bob, charlie, david, eve])
        self.assertEqual(h1.size(), 5)

        # Extract elements and verify max-heap property (by age)
        self.assertEqual(h1.extract(), charlie)  # Charlie, 40
        self.assertEqual(h1.extract(), david)  # David, 35
        self.assertEqual(h1.extract(), alice)  # Alice, 30
        self.assertEqual(h1.extract(), eve)  # Eve, 28
        self.assertEqual(h1.extract(), bob)  # Bob, 25

        # Test variable arguments constructor
        h2 = Heap(alice, bob, charlie, david, eve)
        self.assertEqual(h2.size(), 5)

        # Extract elements and verify max-heap property (by age)
        self.assertEqual(h2.extract(), charlie)  # Charlie, 40
        self.assertEqual(h2.extract(), david)  # David, 35
        self.assertEqual(h2.extract(), alice)  # Alice, 30
        self.assertEqual(h2.extract(), eve)  # Eve, 28
        self.assertEqual(h2.extract(), bob)  # Bob, 25

    def test_custom_class_copy(self):
        """Test heap with custom class objects - copy semantics"""
        # Create some Person objects
        alice = Person("Alice", 30)
        bob = Person("Bob", 25)
        charlie = Person("Charlie", 40)
        david = Person("David", 35)
        eve = Person("Eve", 28)

        # Test copy
        h1 = Heap(alice, bob, charlie, david, eve)
        h2 = h1.copy()

        self.assertEqual(h1.size(), 5)
        self.assertEqual(h2.size(), 5)

        # Extract from original
        self.assertEqual(h1.extract(), charlie)  # Charlie, 40
        self.assertEqual(h1.extract(), david)  # David, 35
        self.assertEqual(h1.extract(), alice)  # Alice, 30
        self.assertEqual(h1.extract(), eve)  # Eve, 28
        self.assertEqual(h1.extract(), bob)  # Bob, 25

        # Extract from copy
        self.assertEqual(h2.extract(), charlie)  # Charlie, 40
        self.assertEqual(h2.extract(), david)  # David, 35
        self.assertEqual(h2.extract(), alice)  # Alice, 30
        self.assertEqual(h2.extract(), eve)  # Eve, 28
        self.assertEqual(h2.extract(), bob)  # Bob, 25

    def test_custom_class_iterator_constructor(self):
        """Test heap with custom class objects - two iterators constructor"""
        # Create some Person objects
        people_begin = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 40)]

        people_end = [
            Person("David", 35),  # This is the stopping point
            Person("Eve", 28),
        ]

        h = Heap(people_begin, end_iterator=people_end)

        self.assertEqual(h.size(), 3)

        # Extract elements and verify max-heap property (by age)
        self.assertEqual(h.extract(), Person("Charlie", 40))
        self.assertEqual(h.extract(), Person("Alice", 30))
        self.assertEqual(h.extract(), Person("Bob", 25))


if __name__ == "__main__":
    unittest.main()
