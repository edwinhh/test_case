#coding:utf-8
#---------------
#   程序：pythontuyoumi制作游戏
#   版本：0.1  
#   作者：icing  
#   日期：2016-04-11
#   语言：Python 2.7  
#   操作：无
#   功能：实现兔有米制作游戏
#----------------

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time

def createGame(self):
    browser =self.browser
    #新建游戏
    #browser.find_element_by_css_selector(".gameBox.createBox").click()
    browser.find_element_by_xpath('html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/a/div').click()   #新建游戏按钮
    time.sleep(2)
    print (browser.current_url)
    #选择游戏模板
    browser.find_element_by_xpath(".//*[@id='templatesList']/li[41]").click()
    #bashi =browser.find_element_by_xpath(".//*[@id='templatesList']/li[22]").click()
    #ActionChains(browser).move_to_element(bashi)
    #bashi.click()
    time.sleep(2)
    browser.find_element_by_class_name('panel-btn-group').click()   #点击开始制作按钮
    time.sleep(4)
    print (browser.current_url)
    browser.find_element_by_class_name('link-publish').click()  #点击发布按钮
    time.sleep(8)
    #两种方式选择行业
    #browser.find_element_by_xpath(".//*[@id='releaseWindow']/div/div[5]/div[1]/select").click()  
    #browser.find_element_by_xpath(".//*[@id='releaseWindow']/div/div[5]/div[1]/select/option[@data-id='acdbb220-d948-11e5-84f4-59367da5b02b']").click()
    aa =browser.find_element_by_xpath(".//*[@id='releaseWindow']/div/div[5]/div[1]/select")
    aa.find_element_by_xpath('//option[7]').click()

    time.sleep(1)
    #browser.find_element_by_class_name("shareTips").click()
    browser.find_element_by_xpath(".//*[@id='releaseWindow']/div/div[5]/div[3]/button").click() #点击确认发布按钮
    time.sleep(4)
    #点击进入个人中心按钮居然是用双击事件！！！
    mycenter =browser.find_element_by_xpath(".//*[@id='releaseWindow']/div/div[7]/div[3]/button")
    ActionChains(browser).double_click(mycenter).perform()
    time.sleep(2)

    print (browser.current_url)
    