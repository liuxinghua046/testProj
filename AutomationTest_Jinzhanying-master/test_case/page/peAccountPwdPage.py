from selenium.webdriver.common.by import By
from test_case.page import loginPage, navigationPage
from .base import Page

'''
个人中心 - 账号密码页面
'''


class PersonalAccountPwd(Page):

    password_old_loc = \
        (By.XPATH, "//*[@id='oldPwd']")                            # 旧密码输入框
    password_old_error_loc = \
        (By.XPATH, "//*[@class='peronalDeRight']/div[1]/div")      # 旧密码输入框-错误提示信息
    password_new_loc = \
        (By.XPATH, "//*[@id='newPwd']")                            # 新密码输入框
    password_new_error_loc = \
        (By.XPATH, "//*[@class='peronalDeRight']/div[2]/div")      # 新密码输入框-错误提示信息
    password_confirm_loc = \
        (By.XPATH, "//*[@id='confirmPwd']")                        # 确认密码输入框
    password_confirm_error_loc = \
        (By.XPATH, "//*[@class='peronalDeRight']/div[3]/div")      # 确认密码输入框-错误提示信息
    password_button_loc = \
        (By.XPATH, "//*[@class='peronalDeRight']/div[5]/button")   # 修改密码保存按钮

    account_name_loc = \
        (By.XPATH, "//*[@class='peronalDeLeft']/div[3]/input")     # 真实姓名输入框
    account_name_error_loc = \
        (By.XPATH, "//*[@class='peronalDeLeft']/div[3]/div")       # 真实姓名输入框-错误提示信息
    account_wexin_loc = \
        (By.XPATH, "//*[@class='peronalDeLeft']/div[4]/input")     # 微信号输入框
    account_wexin_error_loc = \
        (By.XPATH, "//*[@class='peronalDeLeft']/div[4]/div")       # 微信号输入框-错误提示信息
    account_email_loc = \
        (By.XPATH, "//*[@class='peronalDeLeft']/div[5]/input")     # 邮箱输入框
    account_email_error_loc = \
        (By.XPATH, "//*[@class='peronalDeLeft']/div[5]/div")       # 邮箱输入框-错误提示信息
    account_phone_loc = \
        (By.XPATH, "//*[@class='peronalDeLeft']/div[6]/input")     # 手机输入框
    account_phone_error_loc = \
        (By.XPATH, "//*[@class='peronalDeLeft']/div[6]/div")       # 手机输入框-错误提示信息
    account_button_loc = \
        (By.XPATH, "//*[@class='peronalDeLeft']/div[8]/button")    # 个人信息保存按钮
    account_success_loc = \
        (By.XPATH, "//*[@class='successLeft']")                    # 个人信息-保存成功信息

    error_close_loc = \
        (By.XPATH, "//*[@class='alertModelbox']/h6/strong/img")    # 弹框错误提示-关闭按钮
    error_button_loc = \
        (By.XPATH, "//*[@class='alertModelBtn']/button")           # 弹框错误提示-确定按钮

    # 旧密码输入框
    def password_old_input(self, password_old):
        self.find_element(*self.password_old_loc).send_keys(password_old)

    # 旧密码输入框-错误提示信息
    def password_old_error_text(self):
        return self.find_element(*self.password_old_error_loc).text

    # 新密码输入框
    def password_new_input(self, password_new):
        self.find_element(*self.password_new_loc).send_keys(password_new)

    # 新密码输入框-错误提示信息
    def password_new_error_text(self):
        return self.find_element(*self.password_new_error_loc).text

    # 确认密码输入框
    def password_confirm_input(self, password_confirm):
        self.find_element(*self.password_confirm_loc).send_keys(password_confirm)

    # 确认密码输入框-错误提示信息
    def password_confirm_error_text(self):
        return self.find_element(*self.password_confirm_error_loc).text

    # 密码保存按钮
    def password_button(self):
        self.find_element(*self.password_button_loc).click()

    # 真实姓名输入框
    def account_name_input(self, name):
        self.find_element(*self.account_name_loc).clear()
        self.find_element(*self.account_name_loc).send_keys(name)

    # 真实姓名输入框-错误提示信息
    def account_name_error_text(self):
        return self.find_element(*self.account_name_error_loc).text

    # 微信号输入框
    def account_wexin_input(self, wexin):
        self.find_element(*self.account_wexin_loc).clear()
        self.find_element(*self.account_wexin_loc).send_keys(wexin)

    # 微信号输入框-错误提示信息
    def account_wexin_error_text(self):
        return self.find_element(*self.account_wexin_error_loc).text

    # 邮箱输入框
    def account_email_input(self, email):
        self.find_element(*self.account_email_loc).clear()
        self.find_element(*self.account_email_loc).send_keys(email)

    # 邮箱输入框-错误提示信息
    def account_email_error_text(self):
        return self.find_element(*self.account_email_error_loc).text

    # 手机输入框
    def account_phone_input(self, phone):
        self.find_element(*self.account_phone_loc).clear()
        self.find_element(*self.account_phone_loc).send_keys(phone)

    # 手机输入框-错误提示信息
    def account_phone_error_text(self):
        return self.find_element(*self.account_phone_error_loc).text

    # 个人信息保存按钮
    def account_button(self):
        self.find_element(*self.account_button_loc).click()

    # 个人信息保存成功文本
    def account_success_text(self):
        return self.find_element(*self.account_success_loc).text

    # 错误弹框信息关闭按钮
    def error_close(self):
        self.find_element(*self.error_close_loc).click()

    # 错误弹框信息确定按钮
    def error_button(self):
        self.find_element(*self.error_button_loc).click()

    # 修改密码统一入口
    def password_unified(self, password_old, password_new, password_confirm):
        self.password_old_input(password_old)
        self.password_new_input(password_new)
        self.password_confirm_input(password_confirm)
        self.password_button()
        self.error_button()

    # 修改个人信息统一入口
    def account_unified(self, name, weixin, email, phone):
        self.front()
        self.account_name_input(name)
        self.account_wexin_input(weixin)
        self.account_email_input(email)
        self.account_phone_input(phone)
        self.account_button()
        return self.account_success_text()

    # 修改个人信息统一入口-真实姓名
    def account_unified_name(self, name):
        self.front()
        self.account_name_input(name)
        self.account_button()
        self.error_button()
        return self.account_name_error_text()

    # 修改个人信息统一入口-微信
    def account_unified_wexin(self, wexin):
        self.front()
        self.account_wexin_input(wexin)
        self.account_button()
        self.error_button()
        return self.account_wexin_error_text()

    # 修改个人信息统一入口-邮箱
    def account_unified_email(self, email):
        self.front()
        self.account_email_input(email)
        self.account_button()
        self.error_button()
        return self.account_email_error_text()

    # 修改个人信息统一入口-手机
    def account_unified_phone(self, phone):
        self.front()
        self.account_phone_input(phone)
        self.account_button()
        self.error_button()
        return self.account_phone_error_text()

    #
    # ============================ #
    # -----  页面用到的方法   —----- #
    # ============================ #

    # 前置登录→账号密码
    def front(self):
        loginPage.Login(self.driver).user_login_front()
        navigationPage.Navigation(self.driver).na_personal_check("账号密码")
