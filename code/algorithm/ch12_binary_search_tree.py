import unittest

def Inorder_tree_walk(x):
  if x != null:
    Inorder_tree_walk(x.left)
    print(x.key)
    Inorder_tree_walk(x.right)

  return x

class UnitTest(unittest.TestCase):
  def test_Inorder_tree_walk1(self):
    A = [1, 2, 3]
    # self.assertEqual(Inorder_tree_walk(A), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
