import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.st1 = Stack()

    def tearDown(self):
        del(self.st1)

    def test_push(self):
        self.st1.push(1)
        self.assertIs(self.st1.top(), 1)
        self.assertIs(self.st1.get_size(), 1)
        self.st1.push(True)
        self.assertIs(self.st1.top(), True)
        self.assertIs(self.st1.get_size(), 2)
        self.st1.push('IVAN')
        self.assertIs(self.st1.top(), 'IVAN')
        self.assertIs(self.st1.get_size(), 3)

    def test_pop(self):
        self.st1.push(1)
        self.st1.push(True)
        self.st1.push('IVAN')
        self.assertIs(self.st1.top(), 'IVAN')
        self.assertIs(self.st1.pop(), 'IVAN')
        self.assertIs(self.st1.top(), True)
        self.assertIs(self.st1.pop(), True)
        self.assertIs(self.st1.top(), 1)
        self.assertIs(self.st1.pop(), 1)
        self.assertIs(self.st1.top(), None)
        self.assertIs(self.st1.pop(), None)
        self.assertIs(self.st1.top(), None)

    def test_top(self):
        self.st1.push(1)
        self.st1.push(True)
        self.st1.push('IVAN')
        self.assertIs(self.st1.top(), 'IVAN')
        self.st1.pop()
        self.assertIs(self.st1.top(), True)
        self.st1.pop()
        self.assertIs(self.st1.top(), 1)
        self.st1.pop()
        self.assertIs(self.st1.top(), None)

    def test_size(self):
        self.st1.push(1)
        self.st1.push(True)
        self.st1.push('IVAN')
        self.assertIs(self.st1.get_size(), 3)
        self.st1.pop()
        self.assertIs(self.st1.get_size(), 2)
        self.st1.pop()
        self.assertIs(self.st1.get_size(), 1)
        self.st1.pop()
        self.assertIs(self.st1.get_size(), 0)
        self.st1.pop()
        self.assertIs(self.st1.get_size(), 0)

    def test_clear(self):
        self.st1.push(1)
        self.st1.push(True)
        self.st1.push('IVAN')
        self.st1.clear()
        self.assertIs(self.st1.get_size(), 0)
        self.assertIs(self.st1.top(), None)

if __name__ == '__main__':
    unittest.main()
