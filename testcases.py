from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from app_information import desired_caps  # 导入被测试app的信息

import unittest, time, re
import sys


test_result=open('test_result.txt','w')

class NeteaseCloudMusic(unittest.TestCase):
    # 连接Appium Server，初始化自动化环境
    def setUp(self) -> None:
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 设置缺省等待时间
        self.driver.implicitly_wait(6)
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert = True  # 是否继续接受下一个警告#

    def is_element_present(self, how, what):
        """
        判断元素是否存在
        :param how: 定位方式
        :param what: 定位元素的属性值
        :return: True：代表元素存在，False：代表元素不存在
        """
        try:
            self.driver.find_element(how, what)
            print('The result is True', file=test_result)
            return True

        except NoSuchElementException:
            print('The result is False', file=test_result)
            return False

    def test_playmusic(self):
        driver = self.driver
        driver.find_element(By.ID, 'com.netease.cloudmusic:id/a5j').click()  # 点击“每日推荐”
        driver.implicitly_wait(3)
        self.assertTrue(self.is_element_present(By.ID, 'com.netease.cloudmusic:id/apv'))  #判断“播放全部”是否存在,把结果输出到文件


        driver.find_element(By.ID, 'com.netease.cloudmusic:id/apv').click()  # 点击“播放全部”
        time.sleep(10)
        driver.quit()

