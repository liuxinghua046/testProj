from selenium.webdriver.common.by import By
from test_case.page import loginPage, method
from .base import Page

'''
新增导航菜单页面
'''


class NavigationAdd(Page):

    navigation_add_loc = \
        (By.XPATH, "//*[@class='header']/b")                # 新增导航“+”按钮
    navigation_add_add_loc = \
        (By.XPATH, "//*[@class='noDrag']")                  # 导航设置中“+”按钮
    navigation_add_len_loc = \
        (By.XPATH, "//*[@class='ui-sortable']/li")          # 导航数量获取
    navigation_add_name_loc = \
        (By.XPATH, "//*[@class='navigationName']/input")    # 导航名称输入框
    navigation_add_label_loc = \
        (By.XPATH, "//*[@class='navigatBIQIzx']/li")        # 选择标签
    navigation_add_button_loc = \
        (By.XPATH, "//*[@class='navigBtn']")                # 底部添加按钮
    navigation_add_fail_loc = \
        (By.XPATH, "//*[@class='IndexAddBoxIN1']/b")        # 弹框错误提示
    navigation_add_fail_null_loc = \
        (By.XPATH, "//*[@class='alertModelbox']/span")      # 弹框错误提示为空
    navigation_add_button_button_loc = \
        (By.XPATH, "//*[@class='IndexAddBoxBtn1']/button")  # 弹框添加按钮

    js = "var q=document.documentElement.scrollTop=10000"   # 滚动条至页面底部

    navigation_add_navigation_loc = \
        (By.XPATH, "//*[@class='ui-sortable']/li")                  # 导航设置中导航
    navigation_add_navigation_del_loc = \
        (By.XPATH, "//*[@class='biaoqianPosit active']/span/img")   # 删除“X”
    navigation_add_navigation_del_button_yes_loc = \
        (By.XPATH, "//*[@class='remove_layer']/span[2]/button[1]")  # 删除弹框“是”
    navigation_add_navigation_del_button_no_loc = \
        (By.XPATH, "//*[@class='remove_layer']/span[2]/button[2]")  # 删除弹框“否”

    #
    # ============================ #
    # -----  新增导航 ---------     #
    # ============================ #

    def navigation_add(self):
        """新增导航菜单“+”按钮点击"""
        self.find_element(*self.navigation_add_loc).click()

    def navigation_add_add(self):
        """导航设置新增“+”按钮点击"""
        self.find_element(*self.navigation_add_add_loc).click()

    def navigation_add_len(self):
        """导航数量获取"""
        return len(self.find_elements(*self.navigation_add_len_loc))

    def navigation_add_len_text(self, num):
        """导航名称获取"""
        return self.find_elements(*self.navigation_add_len_loc)[num].text

    def navigation_add_len_click(self, num):
        """导航名称点击"""
        return self.find_elements(*self.navigation_add_len_loc)[num].click()

    def navigation_add_name(self, name):
        """导航名称输入框"""
        self.find_element(*self.navigation_add_name_loc).send_keys(name)

    def navigation_add_label_number(self):
        """标签数量获取"""
        return len(self.find_elements(*self.navigation_add_label_loc))

    def navigation_add_label_click(self, num):
        """单个标签选择点击"""
        self.find_elements(*self.navigation_add_label_loc)[num].click()

    def navigation_add_label_click_all(self):
        """全部标签选择点击"""
        self.find_element(*self.navigation_add_label_loc)[self.navigation_add_label_number()].click()

    def navigation_add_button(self):
        """底部添加按钮点击"""
        self.find_element(*self.navigation_add_button_loc).click()

    def navigation_add_name_text(self):
        """导航名称输入框文本"""
        return self.find_element(*self.navigation_add_name_loc).text

    def navigation_add_fail_text(self):
        """添加导航错误状态 - 重复、超长、特殊字符文本获取"""
        return self.find_element(*self.navigation_add_fail_loc).text

    def navigation_add_null_text(self):
        """添加导航错误状态 - 为空文本获取"""
        return self.find_element(*self.navigation_add_fail_null_loc).text

    def navigation_add_button_button(self):
        """弹框添加按钮点击"""
        self.find_element(*self.navigation_add_button_button_loc).click()

    def navigation_add_js(self):
        """JS页面滚动条下拉到底"""
        self.script(self.js)

    #
    # ============================ #
    # -----  删除导航 ---------     #
    # ============================ #

    def navigation_add_navigation_del(self):
        """点击删除按钮"""
        self.find_element(*self.navigation_add_navigation_del_loc).click()

    def navigation_add_navigation_del_button_yes(self):
        """删除弹框选择 - 是"""
        self.find_element(*self.navigation_add_navigation_del_button_yes_loc).click()

    def navigation_add_navigation_del_button_no(self):
        """删除弹框选择 - 否"""
        self.find_element(*self.navigation_add_navigation_del_button_no_loc).click()

    #
    # ============================ #
    # -----  页面用到的方法  ------  #
    # ============================ #

    def na_navigation_add(self):
        """简化-前置登录→新增导航"""
        loginPage.Login(self.driver).user_login_front()
        self.navigation_add()

    def na_navigation_add_text_label_btn(self, name):
        """简化-前置登录→新增导航→输入框内容→选择标签→确定"""
        self.na_navigation_add()
        self.navigation_add_name(name)
        self.navigation_add_js()
        self.navigation_add_label_click(1)
        self.navigation_add_button()

    def na_navigation_add_newnavigation_if(self, name):
        """判断新增测试导航是否存在"""
        list1 = []
        number = self.navigation_add_len()
        for i in range(number):
            text = self.navigation_add_len_text(i)
            list1.append(text)
        if name in list1:
            return True
        else:
            return False

    def na_navigation_add_newnavigation_operation(self, name):
        """判断新增测试导航是否存在,然后进行删除、新增操作"""
        self.na_navigation_add()
        list1 = []
        number1 = self.navigation_add_len()
        for i in range(number1):
            text = self.navigation_add_len_text(i)
            list1.append(text)
        if name not in list1:
            self.navigation_add_name(name)
            self.navigation_add_js()
            self.navigation_add_label_click(1)
            self.navigation_add_button()
            self.navigation_add_button_button()
            method.Method(self.driver).back_top()
            # number2 = self.navigation_add_len()
            # for i in range(number2):
            #     text = self.navigation_add_len_text(i)
            #     list1.append(text)
            # index = list1.index(name)
            self.navigation_add_len_click(-1)
            self.navigation_add_navigation_del()
        else:
            index = list1.index(name)
            self.navigation_add_len_click(index)
            self.navigation_add_navigation_del()
