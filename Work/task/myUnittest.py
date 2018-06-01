#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from time import sleep
import os
import time
from HTMLTestRunner import HTMLTestRunner

from Work.task.function import Function
from selenium import webdriver

"""
小任务：
  1.对集成化登录页面进行测试用例编写，然后用自动化脚本进行实现；
  2.每条用例执行需要进行截图保存；
  3.所有用例执行完后，需要把执行结果保存到文件中。
"""

# 创建测试类LoginCase，用unittest的测试框架的格式
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 定义打开浏览器的方法，这里用的是Chrome，火狐为Firfox，IE为Ie，必须在根目录下对应的driver才能调用
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        # 需要测试的网址
        self.driver.get("http://192.168.20.12:56366/rdms/login.jsp")
        self.driver.implicitly_wait(20)

    # 定义登录方法，被测试用例调用
    def user_login(self,username,password):
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_class_name("loginButton").click()


    def test_login1(self):
        """ 用户名正确、密码正确登录 """
        self.user_login(username="刘兴花", password="a890890890")

        # 定义了一个实际值，用谷歌或者火狐F12可以抓取到登陆后显示的用户名，.text是获取地址的文本值
        # assert先判断需要的实际值是否正确，正确，继续运行用例；如果不正确，不继续运行该用例并返回错误
        # assert self.driver.find_element_by_xpath("//*[@id='J-SessionName-Name']").text
        # 将实际值赋值给一个变量login_name，方便比较，可自定义
        login_name=self.driver.find_element_by_xpath("//*[@id='J-SessionName-Name']").text
        self.assertEqual(login_name,'刘兴花')

        # 截图
        Function.insert_img(self.driver, "登录成功.png")
        # self.driver.get_screenshot_as_file("D:\pycharm2018.1.2x64\login_succes.png")

    def test_login2(self):
        """ 用户名为空、密码为空登录 """
        self.user_login(username="", password="")
        error_text = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[2]").text
        Function.insert_img(self.driver, "Login_用户名、密码为空.png")
        # 用assertIn(a,b)方法来断言 a in b
        # 用assertEqual(a,b)方法来断言
        self.assertEqual(error_text,"请输入用户名！请输入密码！123")
        Function.insert_img(self.driver, "Login_用户名、密码为空.png")

    # def test_login3(self):
    #     """ 用户名为空、密码有内容 """
    #     self.user_login(username="", password="789456")
    #     Function.insert_img(self.driver, "Login_用户名为空密码有内容.png")


    # def test_login4(self):
    #     """ 用户名有内容、密码为空 """
    #     self.user_login(username="1234", password="")
    #     Function.insert_img(self.driver, "Login_密码为空.png")
    #
    # def test_login5(self):
    #     """ 密码输入非字母数字下划线组合"""
    #     self.user_login(username="12345", password="$%^^@#")
    #     Function.insert_img(self.driver, "Login_用户名或密码错误，请重新输入！.png")
    #
    #
    # def test_login6(self):
    #     """ 输入错误的用户名，密码输入正确 """
    #     self.user_login(username="qwer", password="a890890890")
    #     Function.insert_img(self.driver, "Login_用户名或密码错误，请重新输入！.png")
    #
    #
    # def test_login7(self):
    #     """ 输入错误的密码，用户名正确 """
    #     self.user_login(username="刘兴花", password="12345678")
    #     Function.insert_img(self.driver, "Login_用户名或密码错误，请重新输入！.png")

    # 每个test_执行完执行一次tearDown()方法
    def tearDown(self):
        sleep(1)
        # refresh()方法为刷新浏览器
        self.driver.refresh()
        print("执行完测试用例")
        self.driver.quit()

if __name__ == '__main__':
    # unittest.main()
    report_title = u'登陆模块测试报告'

    # 定义脚本内容，加u为了防止中文乱码
    desc = u'集成化登陆模块测试报告详情：'

    # 定义date为日期，time为时间
    date = time.strftime("%Y%m%d")
    time = time.strftime("%Y%m%d%H%M%S")

    # 定义path为文件路径，目录级别，可根据实际情况自定义修改
    # path = 'D:/pycharm2018.1.2x64/' + date + "/login/" + time + "/"
    path = 'D:/pycharm2018.1.2x64/Work/report/'


    # 定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    report_path = path + "report.html"
    print("1111111")
    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    # 定义一个测试容器
    testsuite = unittest.TestSuite()

    # 将测试用例添加到容器
    testsuite.addTest(TestLogin("test_login1"))
    testsuite.addTest(TestLogin("test_login2"))
    # testsuite.addTest(TestLogin("test_login3"))
    # testsuite.addTest(TestLogin("test_login4"))
    # testsuite.addTest(TestLogin("test_login5"))
    # testsuite.addTest(TestLogin("test_login6"))
    # testsuite.addTest(TestLogin("test_login7"))

    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)

        # 关闭report，脚本结束
    report.close()
