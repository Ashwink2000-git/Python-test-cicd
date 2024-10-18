import unittest
import script1  # Importing script1 directly since it will be in the same directory

class TestModule1(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(script1.greet(), "Hello from Module 1!")

    def test_add(self):
        # Add a test for a hypothetical add function in script1
        self.assertEqual(script1.add(2, 3), 5)  # Assuming you have an add function in script1

if __name__ == "__main__":
    unittest.main()


