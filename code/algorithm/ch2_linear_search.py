import unittest

def linear_search(A, val):
  index = None
  for i in range(0, len(A)):
    if A[i] == val:
      index = i
  return index

class UnitTest(unittest.TestCase):
  def test_linear_search1(self):
    A = [0, 1]
    val = 1
    self.assertEqual(linear_search(A, val), 1)

  def test_linear_search2(self):
    A = [0, 1]
    val = 3
    self.assertEqual(linear_search(A, val), None)

  def test_linear_search3(self):
    A = [4, 1, 5]
    val = 5 
    self.assertEqual(linear_search(A, val), 2)

if __name__ == '__main__':
    unittest.main()
