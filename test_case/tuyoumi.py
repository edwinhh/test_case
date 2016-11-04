#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time,unittest
import tuyoumi_login,tuyoumi_signout
import tuyoumi_createGame,tuyoumi_deleteGame

class tuyoumi(unittest.TestCase):
    
    #初始化
    def setUp(self):
        print ("执行初始化函数")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.browser = webdriver.Chrome(chrome_options=self.options)
        self.browser.implicitly_wait(20)
        self.baseurl ="http://test.tuyoumi.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_tuyoumi(self):
        u"""兔有米网站（测试环境）登录+制作游戏+删除游戏+退出"""
        print ("执行登录函数")
        browser =self.browser
        browser.get(self.baseurl)
        #调用登录模块
        tuyoumi_login.login(self)
        #页面截图
        browser.get_screenshot_as_file(r"D:\MyWorkpace\tuyoumi\src\tuyoumi.png")
        print (browser.current_url)
#        for i in range(0,4):
#            print "执行游戏制作函数"
#            tuyoumi_createGame.createGame(self)
#            i +=1
        print ("执行游戏制作函数")
        tuyoumi_createGame.createGame(self)
        print ("执行删除游戏函数")
        tuyoumi_deleteGame.deleteGame(self)
        print ("执行退出函数")
        tuyoumi_signout.signout(self)

        
    def tearDown(self):
        print ("执行浏览器退出")
        self.browser.quit()
        self.assertEqual([], self.verificationErrors)

        
if __name__ == "__main__":
    unittest.main()
    