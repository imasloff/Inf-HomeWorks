import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.st1 = Stack()
        self.st2 = Stack()
        self.st3 = Stack()
        self.st1.push(1)
        self.st1.push(2)
        self.st1.push(3)
        self.st2.push(True)
        self.st2.push(False)

    def test_size(self):
        print("test_size")
        self.assertIs(self.st1.get_size(), 3)
        self.assertIs(self.st2.get_size(), 2)
        self.assertIs(self.st3.get_size(), 0)

    def tearDown(self):
        print("tearDown")
        self.st1.clear()
        self.st2.clear()
        self.st3.clear()
        del(self.st1)
        del(self.st2)
        del(self.st3)

    def test_pop(self):
        print("test_pop")
        self.assertIs(self.st1.pop(), 3)
        self.assertIs(self.st2.pop(), False)
        self.assertIs(self.st3.pop(), None)

    def test_top(self):
        print("test_top")
        self.assertIs(self.st1.top(), 3)
        self.assertIs(self.st2.top(), False)
        self.assertIs(self.st3.top(), None)

if __name__ == '__main__':
    unittest.main()
