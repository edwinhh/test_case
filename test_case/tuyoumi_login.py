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
import unittest,time

def login(self):
    browser =self.browser
    browser.maximize_window()
    time.sleep(2)
    browser.find_element_by_class_name("btn-login").click()
    time.sleep(1)
    browser.switch_to_frame('loginContainer_iframe_killerwhale')
    browser.find_element_by_id("login-email").send_keys("981524415@qq.com")
    browser.find_element_by_xpath("//*[@id=\"login-pwd\"]").send_keys("111111")
    inputs=browser.find_elements_by_tag_name('input')
    for input in inputs:
        if input.get_attribute('type')=='checkbox':
            input.click()
  
    time.sleep(2)
    #下面是两种方法定位submit
    browser.find_element_by_css_selector(".button.j-login-btn").click()
    #browser.find_element_by_xpath("/html/body/div/div/div[5]/div").click()
    time.sleep(2)
    

