import unittest
from src.module1 import script1

class TestModule1(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(script1.greet(), "Hello from Module 1!")

    def test_add(self):
        self.assertEqual(script1.add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
