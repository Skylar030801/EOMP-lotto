import unittest

class AgeTest(unittest.TestCase):
 def testage(self):
    age=int(input("enter age"))
    message="false"
    self.assertIn(age,range(18,100))
