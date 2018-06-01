from test_case.models.function import Function
from test_case.models import myunit
from test_case.page import loginPage
import unittest

'''
@ name: 登录测试用例
@ test：1.正确的用户名和密码；
        2.用户名为空、密码为空；
        3.用户名为空、密码有内容；
        4.用户名有4-20位内容、密码为空；
        5.用户名输入小于4位，密码有内容；
        6.用户名输入大于20位，密码有内容；
        7.密码输入小于6位，用户名有4-20位内容；
        8.密码输入大于12位，用户名有4-20位内容；
        9.密码输入非字母数字下划线组合，用户名有4-20位内容；
        10.输入错误的用户名，密码输入正确；
        11.输入错误的密码，用户名正确。
'''


class LoginTest(myunit.MyTest):
    """ 登录测试 """

    def user_login_verify(self, username, password):
        loginPage.Login(self.driver).user_login(username, password)

    def test_login1(self):
        """ 用户名正确、密码正确登录 """
        self.user_login_verify(username="17777786550", password="qwer1234")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_用户名密码正确登录.jpg")
        self.assertTrue(po.user_login_success(), "+")

    def test_login2(self):
        """ 用户名为空、密码为空登录 """
        self.user_login_verify(username="", password="")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_用户名为空密码为空登录.jpg")
        self.assertEqual(po.user_login_fail(), "")


    def test_login3(self):
        """ 用户名为空、密码有内容 """
        self.user_login_verify(username="", password="123456")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_用户名为空密码有内容.jpg")
        self.assertEqual(po.user_login_fail(), "用户名不能为空")

    def test_login4(self):
        """ 用户名有4-20位内容、密码为空 """
        self.user_login_verify(username="1234", password="")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_用户名有4-20位内容密码为空.jpg")
        self.assertEqual(po.user_login_fail(), "密码不能为空")

    def test_login5(self):
        """ 用户名输入小于4位，密码有内容 """
        self.user_login_verify(username="123", password="123")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_用户名输入小于4位密码有内容.jpg")
        self.assertEqual(po.user_login_fail(), "用户名必须由4-20位字母数字组成")

    def test_login6(self):
        """ 用户名输入大于20位，密码有内容 """
        self.user_login_verify(username="123456789012345678901", password="123")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_用户名输入大于20位密码有内容.jpg")
        self.assertEqual(po.user_login_fail(), "用户名必须由4-20位字母数字组成")

    def test_login7(self):
        """ 密码输入小于6位，用户名有4-20位内容 """
        self.user_login_verify(username="12345", password="123")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_密码输入小于6位用户名有4-20位内容.jpg")
        self.assertEqual(po.user_login_fail(), "密码必须是由 6-12位字母数字_ 组合")

    def test_login8(self):
        """ 密码输入大于12位，用户名有4-20位内容 """
        self.user_login_verify(username="12345", password="1234567890123")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_密码输入大于12位用户名有4-20位内容.jpg")
        self.assertEqual(po.user_login_fail(), "密码必须是由 6-12位字母数字_ 组合")

    def test_login9(self):
        """ 密码输入非字母数字下划线组合，用户名有4-20位内容 """
        self.user_login_verify(username="12345", password="12345！@#")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_密码输入非字母数字下划线组合用户名有4-20位内容.jpg")
        self.assertEqual(po.user_login_fail(), "密码必须是由 6-12位字母数字_ 组合")

    def test_login10(self):
        """ 输入错误的用户名，密码输入正确 """
        self.user_login_verify(username="12345", password="123456")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_输入错误的用户名密码输入正确.jpg")
        self.assertEqual(po.user_login_fail(), "用户名或者密码不正确")

    def test_login11(self):
        """ 输入错误的密码，用户名正确 """
        self.user_login_verify(username="17777786550", password="12345678")
        po = loginPage.Login(self.driver)
        Function.insert_img(self.driver, "Login_输入错误的密码用户名正确.jpg")
        self.assertEqual(po.user_login_fail(), "用户名或者密码不正确")

if __name__ == '__main__':
    unittest.main()
