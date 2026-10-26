import unittest

from src.main import add, greet


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_greet(self):
        self.assertEqual(greet("Alex"), "Hello, Alex!")


if __name__ == "__main__":
    unittest.main()
