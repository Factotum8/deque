"""
There is a double ended queue implementation.
"""
from typing import Any
from abc import ABC, abstractmethod


class DequeException(Exception):
    """
    The module base exception
    """


class DequeAbstract(ABC):

    @abstractmethod
    def push_back(self, value: Any):
        pass

    @abstractmethod
    def push_front(self, value: Any):
        pass

    @abstractmethod
    def pop_back(self) -> Any:
        pass

    @abstractmethod
    def pop_front(self) -> Any:
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

    @property
    def is_overflow(self) -> bool:
        return self._size >= self._max_size

    def push_back(self, value: Any):
        if self.is_overflow:
            raise DequeException('overflow')

        self._data[self._tail], self._tail = value, (self._tail + 1) % self._max_size
        self._size += 1

    def push_front(self, value: Any):
        if self.is_overflow:
            raise DequeException('overflow')

        self._head = (self._head - 1 + self._max_size) % self._max_size
        self._data[self._head] = value
        self._size += 1

    def pop_back(self) -> Any:
        if self._size == 0:
            raise DequeException('underflow')

        self._tail = (self._tail - 1 + self._max_size) % self._max_size
        self._size -= 1
        return self._data[self._tail]

    def pop_front(self) -> Any:
        if self._size == 0:
            raise DequeException('underflow')

        self._head, result = (self._head + 1) % self._max_size, self._data[self._head]
        self._size -= 1
        return result
