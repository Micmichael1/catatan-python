import unittest
from module1 import multiply_by_two

class TestModule1(unittest.TestCase):
    def test_multiply_by_two(self):
        self.assertEqual(multiply_by_two(2), 4)
    def test_multiply_by_two2(self):
        self.assertEqual(multiply_by_two(3), 9)

if __name__ == '__main__':
    unittest.main()