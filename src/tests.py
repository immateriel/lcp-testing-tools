import unittest
from test1.test11 import Test11
from test1.test12 import Test12
from test2.test21 import Test21
from test2.test22 import Test22


if __name__ == '__main__':
  test11 = unittest.TestLoader().loadTestsFromTestCase(Test11)
  test12 = unittest.TestLoader().loadTestsFromTestCase(Test12)
  test21 = unittest.TestLoader().loadTestsFromTestCase(Test21)
  test22 = unittest.TestLoader().loadTestsFromTestCase(Test22)
  alltests = unittest.TestSuite([test11, test12, test21, test22])
  unittest.TextTestRunner(verbosity=2).run(alltests)
