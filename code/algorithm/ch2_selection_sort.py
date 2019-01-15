import unittest

def swap(A, i, j):
    temp = A[j]
    A[j] = A[i]
    A[i] = temp
    return A

def selection_sort(A):
  n = len(A)
  for j in range(0, n - 1):
    smallest = j
    for i in range(j + 1, n):
      if A[i] < A[smallest]:
        smallest = i
    swap(A, smallest, j)
  return A

class UnitTest(unittest.TestCase):
  def test_selection_sort1(self):
    A = [3, 1, 2]
    self.assertEqual(selection_sort(A), [1, 2, 3])

  def test_selection_sort2(self):
    A = [3, 1, 4]
    self.assertEqual(selection_sort(A), [1, 3, 4])

if __name__ == '__main__':
    unittest.main()
