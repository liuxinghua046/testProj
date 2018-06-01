#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from Work.task.function import Function

class Login():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.168.20.12:56366/rdms/login.jsp")
        self.driver.implicitly_wait(20)

    def user_login(self,username,password):
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_class_name("loginButton").click()

    def test_login1(self):
        """ 用户名正确、密码正确登录 """
        self.user_login(username="刘兴花", password="a890890890")
        # Function.insert_img(self.driver, "登录成功.png")
        self.driver.get_screenshot_as_file("D:\pycharm2018.1.2x64\login_succes.png")

    def test_login2(self):
        """ 用户名为空、密码为空登录 """
        self.user_login(username="", password="")
        Function.insert_img(self.driver, "Login_用户名、密码为空.png")

    def test_login3(self):
        """ 用户名为空、密码有内容 """
        self.user_login(username="", password="789456")
        Function.insert_img(self.driver, "Login_用户名为空密码有内容.png")


    def test_login4(self):
        """ 用户名有内容、密码为空 """
        self.user_login(username="1234", password="")
        Function.insert_img(self.driver, "Login_密码为空.png")

    def test_login5(self):
        """ 密码输入非字母数字下划线组合"""
        self.user_login(username="12345", password="$%^^@#")
        Function.insert_img(self.driver, "Login_用户名或密码错误，请重新输入！.png")


    def test_login6(self):
        """ 输入错误的用户名，密码输入正确 """
        self.user_login(username="qwer", password="a890890890")
        Function.insert_img(self.driver, "Login_用户名或密码错误，请重新输入！.png")


    def test_login7(self):
        """ 输入错误的密码，用户名正确 """
        self.user_login(username="刘兴花", password="12345678")
        Function.insert_img(self.driver, "Login_用户名或密码错误，请重新输入！.png")


if __name__ == '__main__':
   Login().test_login1()

