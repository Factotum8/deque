from unittest import TestCase

from deque import Deque, DequeException


class TestDeque(TestCase):
    size = 3

    def setUp(self) -> None:
        self.deque = Deque(self.size)
        self.full_deque = Deque(self.size)
        self.full_deque._size = 3
        self.full_deque._data = [i for i in range(self.size)]

    def test_max_size(self):
        self.assertEqual(self.size, self.deque.max_size)

    def test_push_back(self):
        self.assertEqual([float('inf'), float('inf'), float('inf')], self.deque._data)
        self.deque.push_back(1)
        self.assertEqual([1, float('inf'), float('inf')], self.deque._data)
        self.deque.push_back(2)
        self.assertEqual([1, 2, float('inf')], self.deque._data)
        self.deque.push_back(3)
        self.assertEqual([1, 2, 3], self.deque._data)
        with self.assertRaises(DequeException) as context:
            self.deque.push_back(4)
            self.assertTrue('overflow' in context.exception)

    def test_push_front(self):
        self.assertEqual([float('inf'), float('inf'), float('inf')], self.deque._data)
        self.deque.push_front(1)
        self.assertEqual([float('inf'), float('inf'), 1], self.deque._data)
        self.deque.push_front(2)
        self.assertEqual([float('inf'), 2, 1], self.deque._data)
        self.deque.push_front(3)
        self.assertEqual([3, 2, 1], self.deque._data)
        with self.assertRaises(DequeException) as context:
            self.deque.push_front(4)
            self.assertTrue('overflow' in context.exception)

    def test_pop_back(self):
        for i in reversed(range(self.size)):
            self.assertEqual(i, self.full_deque.pop_back())

        with self.assertRaises(DequeException) as context:
            self.deque.pop_back()
            self.assertTrue('underflow' in context.exception)

    def test_pop_front(self):
        for i in range(self.size):
            self.assertEqual(i, self.full_deque.pop_front())

        with self.assertRaises(DequeException) as context:
            self.deque.pop_front()
            self.assertTrue('underflow' in context.exception)


if __name__ == '__main__':
    TestDeque().run()
