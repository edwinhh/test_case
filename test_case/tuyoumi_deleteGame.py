#coding:utf-8
#---------------
#   程序：python+selenium 删除个人中心游戏+退出登录
#   版本：0.1  
#   作者：icing  
#   日期：2016-04-09
#   语言：Python 2.7  
#   操作：无
#   功能：删除个人中心游戏（http://test.tuyoumi.com/）
#----------------

#用selenium库函数实现（不获取cookie）
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def deleteGame(self):
    browser =self.browser
    #判断游戏是已发布状态还是已下线状态
    gamestatus =browser.find_element_by_xpath('html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div')
    #下面两行都是打印出单个游戏的文字内容
    print (gamestatus.text[0:3])
    print (gamestatus.text.split('\n')[0])

    i=1
    while i <5:
        gamestatus =browser.find_element_by_xpath('html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div').find_element_by_css_selector(".statusTag.onlineTag,.statusTag.offlineTag")
        print (gamestatus.text)
        if gamestatus.text =="已发布":  #根据游戏的状态不同，删除游戏的操作步骤也不同
            browser.find_element_by_xpath('html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div/div[5]').click()
            time.sleep(1)
            browser.find_element_by_xpath(".//*[@id='AlertWindow']/div/div[4]/button[2]").click()
            time.sleep(1)
            browser.find_element_by_xpath(".//*[@id='AlertWindow']/div/div[4]/button[2]").click()
            i +=1
            time.sleep(2)
        else:
            browser.find_element_by_xpath('html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div/div[5]').click()
            time.sleep(1)
            browser.find_element_by_xpath(".//*[@id='AlertWindow']/div/div[4]/button[2]").click()
            time.sleep(2)
            i +=1


