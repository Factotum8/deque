"""
There is a double ended queue implementation.
"""
from abc import ABC, abstractmethod


class DequeException(Exception):
    """
    The module base exception
    """


class DequeAbstract(ABC):

    @abstractmethod
    def push_back(self, value):
        pass

    @abstractmethod
    def push_front(self, value):
        pass

    @abstractmethod
    def pop_back(self):
        pass

    @abstractmethod
    def pop_front(self):
        pass


class Deque(DequeAbstract):
    """
    The main class contains double ended queue implementation.
    """
    def __init__(self, max_size=0):
        self._head, self._tail, self._size = 0, 0, 0
        self._max_size = max_size
        self._data = [float('inf')] * max_size

    def __repr__(self):
        return str(self._data)

    def __len__(self):
        return self._size

    @property
    def max_size(self) -> int:
        return self._max_size

    def push_back(self, value):
        if (indx := (self._tail + 1) % self._max_size) == self._head:
            raise DequeException('overflow')

        self._data[self._tail], self._tail = value, indx
        self._size += 1

    def push_front(self, value):
        if self._head == (self._tail + 1) % self._max_size:
            raise DequeException('overflow')

        self._head = (self._head - 1 + self._max_size) % self._max_size
        self._data[self._head] = value
        self._size += 1

    def pop_back(self):
        if self._size == 0:
            raise DequeException('underflow')

        self._tail = (self._tail - 1 + self._max_size) % self._max_size
        self._size -= 1
        return self._data[self._tail]

    def pop_front(self):
        if self._size == 0:
            raise DequeException('underflow')

        self._head, result = (self._head + 1) % self._max_size, self._data[self._head]
        self._size -= 1
        return result
