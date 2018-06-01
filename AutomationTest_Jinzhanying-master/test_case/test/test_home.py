from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


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

    def test(self):

        self.driver.find_element(By.LINK_TEXT, "首页").click()
        sleep(3)
        print()

if __name__ == '__main__':
    unittest.main()
