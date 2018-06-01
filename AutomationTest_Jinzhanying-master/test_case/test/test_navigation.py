from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import unittest

from test_case.page import navigationPage, loginPage


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://yuqing.wiseweb.com.cn/")
        self.driver.implicitly_wait(10)
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

    def tearDown(self):
        self.driver.quit()


class Test(MyTest):
    # 简化-导航部分
    def na(self):
        return navigationPage.Navigation(self.driver)

    # 导航个人中心定位
    def test_navigation25(self):
        """ 点击个人中心我的套餐 """
        self.na().na_personal()
        self.na().na_personal_check("我的套餐")
        # 校验页面数据中是否出现“当前套餐内容”文字
        self.assertEqual(
            self.na().navigation_personal_mymeal_text(), "当前套餐内容")

if __name__ == '__main__':
    unittest.main()
