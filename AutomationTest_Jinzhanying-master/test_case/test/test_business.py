import re
from selenium import webdriver
import unittest
from test_case.page import businessPage, navigationPage


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("https://yuqing.wiseweb.com.cn/")
        # self.driver.implicitly_wait(50)
        # self.driver.maximize_window()
        # self.username = '17777786550'
        # self.pwd = '123456'
        # self.driver.find_element_by_css_selector("div.close > img").click()
        # self.driver.find_element_by_id("username").clear()
        # self.driver.find_element_by_id("username").send_keys(self.username)
        # self.driver.find_element_by_id("pwd").clear()
        # self.driver.find_element_by_id("pwd").send_keys(self.pwd)
        # self.driver.find_element_by_id("login").click()

    def tearDown(self):
        self.driver.quit()


class Test(MyTest):

    # 简化-业务统计页面方法简写
    def bu(self):
        return businessPage.Business(self.driver)

    def test_business(self):
        self.bu().front()
        a = self.bu().business_head_title_text()
        print("a" + a)
        b = self.bu().business_left_navigation_text("1", "1")
        print("b" + b)

if __name__ == '__main__':
    unittest.main()
