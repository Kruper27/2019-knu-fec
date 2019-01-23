import sys
path=sys.argv[0]
import os
os.chdir('\\'.join(path.split('\\')[:-1]))
from Pravdyvy_Galois_arithmetic import add,sub,mul,div
import unittest
class TestAddFunction(unittest.TestCase):
    def testaddinv(self):
        self.assertEqual(0,add(2,2))
    def testadd(self):
        self.assertEqual(203,add(151,92))
class TestSubFunction(unittest.TestCase):
    def testsubinv(self):
        self.assertEqual(0,add(2,2))
    def testsub(self):
        self.assertEqual(203,add(151,92))
class TestMulFunction(unittest.TestCase):
    def testmul(self):
        
        self.assertEqual(29,mul(128,2))
    def testzeromul(self):
        self.assertEqual(0,mul(24,0))
class TestDivFunction(unittest.TestCase):
    def testdiv(self):
        self.assertEqual(128,div(29,2))
    def testzeroabove(self):
        self.assertEqual(0,div(0,34))
    def testzerodivision(self):
        self.assertRaises(ZeroDivisionError)
if __name__=='__main__':
    unittest.main()
        
