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
        self.driver.find_element_by_css_selector("div.close > img").click()

    def tearDown(self):
        self.driver.quit()


class Test(MyTest):

    def test(self):
        pass

if __name__ == '__main__':
    unittest.main()
