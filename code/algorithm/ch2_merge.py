import unittest
import sys

# A = [2, 3, 1, 4]
# p = 0, q = 1, r = 3
def merge(A, p, q, r):
  lenR = q - p + 1
  lenL = r - q
  L = [0] * lenR
  R = [0] * lenL
  for i in range(0, lenR):
    L[i] = A[p + i]
  for j in range(0, lenL):
    R[j] = A[q + 1 + j]
  L.append(sys.maxsize)
  R.append(sys.maxsize)

  i = 0
  j = 0
  for k in range(p, r + 1):
    if L[i] <= R[j]:
      A[k] = L[i]
      i = i + 1
    else:
      A[k] = R[j]
      j = j + 1

  return A

class UnitTest(unittest.TestCase):
  def test_merge1(self):
    A = [2, 3, 1, 4]
    self.assertEqual(merge(A, 0, 1, len(A) - 1), [1, 2, 3, 4])

  def test_merge2(self):
    A = [2, 4, 8, 9]
    self.assertEqual(merge(A, 0, 1,  len(A) - 1), [2, 4, 8, 9])

  def test_merge3(self):
    A = [2, 3, 1]
    self.assertEqual(merge(A, 0, 1, len(A) - 1), [1, 2, 3])

def merge_firstattempt(A, p, q, r):
  T = [0] * (r-p+1)
  f = p
  s = q + 1
  for i in range(0, r-p+1):
    if f > q:
      first = sys.maxsize
    else:
      first = A[f]

    if s > r:
      second = sys.maxsize
    else:
      second = A[s]

    if first <= second:
      T[i] = first
      f = f + 1
    else:
      T[i] = second
      s = s + 1
 
  for i in range(0, r-p+1):
    A[p + i] = T[i]
  return A

if __name__ == '__main__':
    unittest.main()
