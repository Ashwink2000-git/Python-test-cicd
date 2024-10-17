import unittest
import script1  # Importing script1 directly since it will be in the same directory

class TestModule1(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(script1.greet(), "Hello from Module 1!")

    def test_add(self):
        if(self.assertEqual(script1.add(2, 3), 5)==1)
            {print("The test is passing")
            }
        else 
            print("the test is failed")
        

if __name__ == "__main__":
    unittest.main()

