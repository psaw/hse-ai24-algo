from typing import TypeVar, Generic, List, Iterable, Optional, Union, Iterator

T = TypeVar("T")


class Heap(Generic[T]):
    """
    A binary max-heap implementation in Python.
    This is a parametric (generic) class that can store objects of any type T.
    Only the < operator (which maps to __lt__ in Python) is used for comparing elements.
    """

    def __init__(
        self,
        *args: Union[T, Iterable[T], Iterator[T]],
        end_iterator: Optional[Iterator[T]] = None,
    ):
        """
        Supports multiple constructor patterns:
        - Default constructor: Heap()
        - Iterator constructor: Heap(iterable)
        - Initializer list constructor: Heap(value1, value2, ...)
        - Two iterators constructor: Heap(begin_iterator, end_iterator=end_iterator) where
            - begin_iterator: an iterable that provides elements to include
            - end_iterator: an iterable whose first element marks the stopping point
        """
        self._data: List[T] = []

        if end_iterator is not None and len(args) == 1:
            # Constructor with two iterators (begin and end)
            begin_iterator = args[0]

            self._data = []

            # Get the stopping value (first element of end_iterator)
            try:
                end_iter = iter(end_iterator)
                stop_value = next(end_iter, None)

                # Iterate through begin_iterator and add elements until we reach stop_value
                for item in begin_iterator:
                    if item == stop_value:
                        break
                    self._data.append(item)
            except (StopIteration, TypeError):
                # Handle cases where iterators are exhausted or not comparable
                pass

            self._heapify()
        elif len(args) == 1 and hasattr(args[0], "__iter__"):
            # Constructor with iterable (equivalent to C++ iterator constructor)
            self._data = list(args[0])
            self._heapify()
        elif len(args) > 0:
            # Constructor with variable arguments (equivalent to C++ initializer list)
            self._data = list(args)
            self._heapify()

    def __copy__(self) -> "Heap[T]":
        """
        Copy constructor equivalent.
        """
        new_heap = Heap[T]()
        new_heap._data = self._data.copy()
        return new_heap

    def copy(self) -> "Heap[T]":
        """
        Returns a copy of the heap.
        """
        return self.__copy__()

    def __deepcopy__(self, memo) -> "Heap[T]":
        """
        Deep copy support.
        """
        import copy

        new_heap = Heap[T]()
        new_heap._data = copy.deepcopy(self._data, memo)
        return new_heap

    def __del__(self):
        """
        Destructor equivalent.
        """
        self._data.clear()

    def size(self) -> int:
        """
        Returns the number of elements in the heap.
        """
        return len(self._data)

    def empty(self) -> bool:
        """
        Returns True if the heap is empty, False otherwise.
        """
        return len(self._data) == 0

    def insert(self, value: T) -> None:
        """
        Adds an element to the heap.
        """
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def extract(self) -> T:
        """
        Removes and returns the largest element from the heap.
        Raises IndexError if the heap is empty.
        """
        if self.empty():
            raise IndexError("Cannot extract from an empty heap")

        # Get the maximum value (root of the heap)
        max_value = self._data[0]

        # Replace the root with the last element
        last_element = self._data.pop()

        if self._data:  # If the heap is not empty after popping
            self._data[0] = last_element
            self._sift_down(0)

        return max_value

    def _parent(self, index: int) -> int:
        """
        Returns the parent index of the given index.
        """
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        """
        Returns the left child index of the given index.
        """
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        """
        Returns the right child index of the given index.
        """
        return 2 * index + 2

    def _has_parent(self, index: int) -> bool:
        """
        Returns True if the node at the given index has a parent.
        """
        return index > 0

    def _has_left_child(self, index: int) -> bool:
        """
        Returns True if the node at the given index has a left child.
        """
        return self._left_child(index) < len(self._data)

    def _has_right_child(self, index: int) -> bool:
        """
        Returns True if the node at the given index has a right child.
        """
        return self._right_child(index) < len(self._data)

    def _sift_up(self, index: int) -> None:
        """
        Moves the element at the given index up to its correct position.
        """
        while self._has_parent(index):
            parent_idx = self._parent(index)
            # Using only < operator for comparison as specified
            if self._data[parent_idx] < self._data[index]:
                # Swap with parent if parent is smaller
                self._data[parent_idx], self._data[index] = (
                    self._data[index],
                    self._data[parent_idx],
                )
                index = parent_idx
            else:
                break

    def _sift_down(self, index: int) -> None:
        """
        Moves the element at the given index down to its correct position.
        """
        largest = index

        while True:
            if self._has_left_child(index):
                left_idx = self._left_child(index)
                # Using only < operator for comparison as specified
                if self._data[largest] < self._data[left_idx]:
                    largest = left_idx

            if self._has_right_child(index):
                right_idx = self._right_child(index)
                # Using only < operator for comparison as specified
                if self._data[largest] < self._data[right_idx]:
                    largest = right_idx

            if largest != index:
                # Swap with the largest child
                self._data[index], self._data[largest] = (
                    self._data[largest],
                    self._data[index],
                )
                index = largest
            else:
                break

    def _heapify(self) -> None:
        """
        Builds a heap from an unordered array.
        """
        # Start from the last non-leaf node and sift down
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._sift_down(i)
