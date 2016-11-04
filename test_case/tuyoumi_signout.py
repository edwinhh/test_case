#coding:utf-8
#---------------
#   程序：python登录兔有米
#   版本：0.1  
#   作者：icing  
#   日期：2016-04-11
#   语言：Python 2.7  
#   操作：无
#   功能：实现登录兔有米
#----------------

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time

def signout(self):
    browser =self.browser
    name = browser.find_element_by_xpath(".//*[@id='headerWrap']/nav/div[2]/div[7]/div")
    ActionChains(browser).move_to_element(name).perform()
    time.sleep(3)
    browser.find_element_by_xpath(".//*[@id='headerWrap']/nav/div[2]/div[7]/div/div/div[3]").click()
    time.sleep(2)
    print (browser.current_url)
    print ("已经退出登录")