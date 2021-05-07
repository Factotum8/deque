"""
There is a double ended queue implementation.
"""
from abc import ABC, abstractmethod


class DequeMeta(ABC):
    def __init__(self, mix_size=0):
        self._head, self._tail = None, None
        self._data = [] * mix_size

    @abstractmethod
    def push_back(self, value):
        pass

    @abstractmethod
    def push_front(self, value):
        pass

    @abstractmethod
    def pop_front(self):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Deque(DequeMeta):
    def push_front(self, value):
        pass

    def push_back(self, value):
        pass

    def pop_front(self):
        pass

    def pop_back(self):
        pass


"""
push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
"""
