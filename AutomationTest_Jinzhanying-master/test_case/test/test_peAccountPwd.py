from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

from test_case.page import peAccountPwdPage, navigationPage


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

    def tearDown(self):
        self.driver.quit()


class Test(MyTest):

    # 简化-账号密码页面
    def pap(self):
        return peAccountPwdPage.PersonalAccountPwd(self.driver)

    def test_PeAccountPwd21(self):
        """ 真实姓名输入为空，其他项不做修改，点击保存 """
        navigationPage.Navigation(self.driver).na_personal_check("账号密码")
        self.pap().account_button()
        text = self.pap().account_success_text()
        print("文本是：【" + text + "】")
        # # 校验错误提示是否为“姓名不能为空”
        # self.assertEqual(
        #     text, "姓名不能为空")

if __name__ == '__main__':
    unittest.main()
