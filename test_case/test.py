#coding:utf-8

import count
import unittest

class Mytest(unittest.TestCase):
    
    def add(self,a,b):
        return a+b
    
    def setUp(self):
        self.js =count
    
    def test_add(self):
        u""""整数加法"""
        self.assertEqual(self.js.add(2, 3), 5)
    
    def test_add1(self):
        u""""小数加法"""
        self.assertEqual(self.js.add(1.2, 3.5), 4.7)
    def test_add2(self):
        u""""字符串加法"""
        self.assertEqual(self.js.add('hello',' world'), 'hello world')
    
    def tearDown(self):
        print ("ok")
        pass
    
#def suite():
#    suite =unittest.TestSuite()
#    suite.addTest(Mytest("test_add"))
#    suite.addTest(Mytest("test_add1"))
#    suite.addTest(Mytest("test_add2"))
#    return suite
##    return unittest.makeSuite(Mytest, "test")

if __name__ == "__main__":
    unittest.main()
#    unittest.main(defaultTest ="suite")
#    suite = unittest.TestSuite()
#    suite.addTest(Mytest("test_add"))
#    suite.addTest(Mytest("test_add1"))
#    suite.addTest(Mytest("test_add2"))
#    # 执行测试
#    runner = unittest.TextTestRunner()
#    runner.run(suite)
    
    