from selenium.webdriver.common.by import By
from .base import Page
from .navigationPage import Navigation

'''
用户登录页面
'''


class Login(Page):

    login_notice_close_btn_loc = (By.CSS_SELECTOR, "div.close > img")          # 通告提示关闭按钮
    login_notice_text_loc = (By.CSS_SELECTOR, "div.loginModelBox > h4")        # 通告提示文本
    login_username_input_loc = (By.ID, "username")                             # 用户名输入框
    login_password_input_loc = (By.ID, "pwd")                                  # 密码输入框
    login_button_loc = (By.ID, "login")                                        # 登录按钮
    login_weixin_code_loc = (By.XPATH, "//*[@class='footerdl']/dt/img")        # 微信二维码
    login_app_code_loc = (By.XPATH, "//*[@class='footerLeft']/dl[1]/dt/img")   # app二维码

    user_login_fail_loc = (By.ID, 'Exe')              # 登录错误提示位置

    def login_notice_close_btn_click(self):
        """通告提示关闭按钮点击"""
        self.find_element(*self.login_notice_close_btn_loc).click()

    def login_notice_text(self):
        """通告提示-“尊敬的客户：”文本"""
        return self.find_element(*self.login_notice_text_loc).text

    def login_username_input(self, username):
        """登录用户名文本输入框"""
        self.find_element(*self.login_username_input_loc).send_keys(username)

    def login_password_input(self, password):
        """登录密码文本输入框"""
        self.find_element(*self.login_password_input_loc).send_keys(password)

    def login_button_click(self):
        """登录按钮点击"""
        self.find_element(*self.login_button_loc).click()

    def user_login_fail(self):
        """登录失败-文本获取"""
        return self.find_element(*self.user_login_fail_loc).text

    def user_login_success(self):
        """登录成功-获取首页"+"按钮"""
        Navigation.navigation_add_text(self.driver)

    def user_login(self, username, password):
        """定义统一登录登录入口，打开网页→ 关闭通告提示→ 输入用户名→ 输入密码→ 点击登陆"""
        self.open()
        self.login_notice_close_btn_click()
        self.login_username_input(username)
        self.login_password_input(password)
        self.login_button_click()

    def user_login_front(self):
        """其他页面登入前置，正确的用户名和密码"""
        self.user_login(username="刘兴花", password="a890890890")
