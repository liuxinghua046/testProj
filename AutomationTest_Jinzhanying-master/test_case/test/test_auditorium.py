import os
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import time
import unittest
from test_case.models.function import Function

from test_case.page import businessPage, navigationPage, homePage, auditoriumPage


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://yuqing.wiseweb.com.cn/")
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()
        self.username = '17777786550'
        self.pwd = '123456'
        self.driver.find_element_by_css_selector("div.close > img").click()
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(self.username)
        self.driver.find_element_by_id("pwd").clear()
        self.driver.find_element_by_id("pwd").send_keys(self.pwd)
        self.driver.find_element_by_id("login").click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "业务统计").click()
        sleep(3)

    def tearDown(self):
        self.driver.quit()


class Test(MyTest):

    # 简报
    def test_auditorium1(self):
        """  获取简报名称 """
        navigationPage.Navigation(self.driver).na_check('报告厅')
        sleep(2)
        auditoriumPage.Auditorium(self.driver).navigation_add_js()
        text = auditoriumPage.Auditorium(self.driver).briefing_title()
        print("名称是：" + text)
        # 校验在报告厅中是否新建的报告
        self.assertEqual(
            text, "测试新建报告")

if __name__ == '__main__':
    unittest.main()
