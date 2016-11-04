#coding:utf-8
#---------------
#   程序：python兔有米
#   版本：0.1  
#   作者：icing  
#   日期：2016-04-11
#   语言：Python 2.7  
#   操作：无
#   功能：兔有米制作游戏
#----------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time,unittest
import tuyoumi_login,tuyoumi_signout

class CreateGame(unittest.TestCase):
    
    #初始化
    def setUp(self):
        print "执行初始化函数"
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.browser = webdriver.Chrome(chrome_options=self.options)
        self.browser.implicitly_wait(20)
        self.baseurl ="http://test.tuyoumi.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_login(self):
        print "执行登录函数"
        browser =self.browser
        browser.get(self.baseurl)
        #调用登录模块
        tuyoumi_login.login(self)
        #页面截图
        browser.get_screenshot_as_file(r"D:\MyWorkpace\tuyoumi\src\tuyoumi.png")
        print browser.current_url
#        print browser.page_source
        print "执行退出函数"
        tuyoumi_signout.signout(self)
        
#    def test_signout(self):
#        print "执行退出函数"
#        browser =self.browser
#        tuyoumi_signout.signout(self)
        
        
    def tearDown(self):
        print "执行浏览器退出"
        self.browser.quit()
        self.assertEqual([], self.verificationErrors)

        
if __name__ == "__main__":
    unittest.main()
    
