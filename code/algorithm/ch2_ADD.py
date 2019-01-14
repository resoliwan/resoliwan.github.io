import unittest

def ADD(A, B):
  carry = 0
  C = [0] * (len(A) + 1)
  for i in reversed(range(0, len(A))):
    # C[C_0, C_1], A[A_0], B[B_0]
    # C[C_1] = A[A_0] + B[B_0]
    s = A[i] + B[i] + carry
    C[i + 1] = s % 2
    carry = int(s / 2)
  C[0] = carry
  return C

class UnitTestADD(unittest.TestCase):
  def test_ADD1(self):
    A = [0,1]
    B = [0,1]
    self.assertEqual(ADD(A, B), [0,1,0])

  def test_ADD2(self):
    A = [1,1]
    B = [0,1]
    self.assertEqual(ADD(A, B), [1,0,0])

  def test_ADD3(self):
    A = [1,1,1]
    B = [1,0,0]
    self.assertEqual(ADD(A, B), [1,0,1,1])

if __name__ == '__main__':
    unittest.main()
