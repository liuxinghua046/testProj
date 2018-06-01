from selenium.webdriver.common.by import By

from test_case.page import loginPage
from .base import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

'''
导航菜单栏位置
'''


class Navigation(Page):

    navigation_logo_loc = \
        (By.XPATH, "//*[@class='header']/a/img")                        # 定位Logo
    navigation_all_numberX_loc = \
        (By.XPATH, "//*[@id='titleNav']/li[@style='display: block;']")  # 导航显示个数
    navigation_all_numberY_loc = \
        (By.XPATH, "//*[@class='headerduo']/li")                        # 导航隐藏个数
    navigation_more_loc = \
        (By.XPATH, "//*[@class='headergeng']/i")                        # 导航“更多”
    navigation_add_loc = \
        (By.XPATH, "//*[@class='header']/b")                            # 导航“+”

    navigation_home_text_loc = \
        (By.XPATH, "//*[@class='homeCapBox']/div[2]/h6")           # 首页“告警信息”文字
    navigation_alarm_text_loc = \
        (By.XPATH, "//*[@class='GiveanAlarm']/a")                  # 舆情告警页面“告警提醒设置”文字
    navigation_monitor_text_loc = \
        (By.XPATH, "//*[@class='noDrag hrefMark']")                # 舆情监控页面“+添加标签”文字
    navigation_auditorium_text_loc = \
        (By.LINK_TEXT, "设置报告模板")                               # 报告厅页面“设置报告模板”文字
    navigation_business_text_loc = \
        (By.XPATH, "//*[@class='businessTableTimes']")             # 业务统计页面“时间”文字
    navigation_analysis_text_loc = \
        (By.LINK_TEXT, "生成专题")                                  # 专题分析页面“生成专题”文字
    navigation_custom_text_loc = \
        (By.XPATH, "//*[@class='biaoqianPosit active']")           # 自定义页面“自定义”文字

    navigation_personal_numberY_loc = \
        (By.XPATH, "//*[@class='Myself']/li")                      # 个人中心隐藏个数
    navigation_username_loc = \
        (By.XPATH, "//*[@class='TouP']/span")                      # 个人中心-用户名称

    navigation_personal_accountPwd_text_loc = \
        (By.XPATH, "//*[@class='peronalDeRight']/h4")              # 个人中心-账号密码-修改密码文字
    navigation_personal_alarmReminding_text_loc = \
        (By.XPATH, "//*[@class='peronalTi']/p/span")               # 个人中心-告警提醒-邮件通知文字
    navigation_personal_collectionAttention_text_loc = \
        (By.XPATH, "//*[@class='pershoucang']/thead/tr/th[5]")     # 个人中心-收藏关注-收藏时间文字
    navigation_personal_customerService_text_loc = \
        (By.XPATH, "//*[@class='persontextLeft']/h5")              # 个人中心-客服帮助-向网智天元反馈问题文字
    navigation_personal_myMeal_text_loc = \
        (By.XPATH, "//*[@class='peronalBox']/div[4]/h5[1]")        # 个人中心-我的套餐-当前套餐内容文字

    navigation_js_more_loc \
        = "document.getElementById('headerduo').style.display='block'"    # 导航隐性转显性
    navigation_js_personal_loc \
        = "document.getElementById('Myself').style.display='block'"       # 个人中心隐性转显性

    #
    # ============================ #
    # -----  导航部分    ---------  #
    # ============================ #

    def navigation_logo(self):
        """logo图标点击"""
        self.find_element(*self.navigation_logo_loc).click()

    def navigation_all_numberx(self):
        """导航-显示的导航数量获取"""
        return len(self.find_elements(*self.navigation_all_numberX_loc))

    def navigation_all_numberx_text(self, num):
        """导航-显示的导航名称获取"""
        return self.find_elements(*self.navigation_all_numberX_loc)[num].text

    def navigation_all_numberx_click(self, num):
        """导航-显示的导航名称点击"""
        self.find_elements(*self.navigation_all_numberX_loc)[num].click()

    def navigation_all_numbery(self):
        """导航-隐藏的导航数量获取"""
        return len(self.find_elements(*self.navigation_all_numberY_loc))

    def navigation_all_numbery_text(self, num):
        """导航-隐藏的导航名称获取"""
        return self.find_elements(*self.navigation_all_numberY_loc)[num].text

    def navigation_all_numbery_click(self, num):
        """导航-隐藏的导航名称点击"""
        self.find_elements(*self.navigation_all_numberY_loc)[num].click()

    def navigation_logo_text(self):
        """logo图标跳转-首页“告警信息”文本获取"""
        return self.find_element(*self.navigation_home_text_loc).text

    def navigation_home_text(self):
        """首页导航跳转-“告警信息”文本获取"""
        return self.find_element(*self.navigation_home_text_loc).text

    def navigation_alarm_text(self):
        """舆情告警导航跳转-“告警提醒设置”文字获取"""
        return self.find_element(*self.navigation_alarm_text_loc).text

    def navigation_monitor_text(self):
        """舆情监控导航跳转-“+添加标签”文字获取"""
        return self.find_element(*self.navigation_monitor_text_loc).text

    def navigation_auditorium_text(self):
        """报告厅导航跳转-“设置报告模板”文字获取"""
        return self.find_element(*self.navigation_auditorium_text_loc).text

    def navigation_business_text(self):
        """业务统计导航跳转-“时间”文字获取"""
        return self.find_element(*self.navigation_business_text_loc).text

    def navigation_analysis_text(self):
        """专题分析导航跳转-“生成专题”文字获取"""
        return self.find_element(*self.navigation_analysis_text_loc).text

    def navigation_custom_text(self):
        """自定义导航跳转-“自定义”文字获取"""
        return self.find_element(*self.navigation_custom_text_loc).text

    def navigation_more(self):
        """"导航-更多"""
        return self.find_element(*self.navigation_more_loc).text

    def navigation_add_text(self):
        """"导航“+”文本获取"""
        return self.find_element(*self.navigation_add_loc).text

    #
    # ============================ #
    # -----  个人中心部分 ---------  #
    # ============================ #

    def navigation_personal_numbery(self):
        """导航-个人中心隐藏数量获取"""
        return len(self.find_elements(*self.navigation_personal_numberY_loc))

    def navigation_personal_text(self, num):
        """导航-个人中心隐藏名称获取"""
        return self.find_elements(*self.navigation_personal_numberY_loc)[num].text

    def navigation_personal_click(self, num):
        """导航-个人中心隐藏名称点击"""
        self.find_elements(*self.navigation_personal_numberY_loc)[num].click()

    def navigation_username_text(self):
        """导航-个人中心用户名称获取"""
        return self.find_elements(*self.navigation_username_loc).text

    def navigation_personal_accountpwd_text(self):
        """个人中心-账号密码-“修改密码”文字获取"""
        return self.find_element(*self.navigation_personal_accountPwd_text_loc).text

    def navigation_personal_alarmreminding_text(self):
        """个人中心-告警提醒-“邮件通知”文字获取"""
        return self.find_element(*self.navigation_personal_alarmReminding_text_loc).text

    def navigation_personal_collectionattention_text(self):
        """个人中心-收藏关注-“收藏时间”文字获取"""
        return self.find_element(*self.navigation_personal_collectionAttention_text_loc).text

    def navigation_personal_customerservice_text(self):
        """个人中心-客服帮助-“向网智天元反馈问题”文字获取"""
        return self.find_element(*self.navigation_personal_customerService_text_loc).text

    def navigation_personal_mymeal_text(self):
        """个人中心-我的套餐-“套餐日志”文字获取"""
        return self.find_element(*self.navigation_personal_myMeal_text_loc).text

    #
    # ============================ #
    # ---  JS转换、鼠标操作部分  ---- #
    # ============================ #

    def navigation_js_more(self):
        """导航更多JS脚本转换（隐性转显性）"""
        self.script(self.navigation_js_more_loc)

    def navigation_js_personal(self):
        """导航个人中心JS脚本转换（隐性转显性）"""
        self.script(self.navigation_js_personal_loc)

    def navigation_more_perform(self):
        """"导航更多按钮鼠标悬浮"""
        above = self.driver.find_element_by_css_selector(".headergeng")
        ActionChains(self.driver).move_to_element(above).perform()

    def navigation_personal_perform(self):
        """导航个人中心鼠标悬浮"""
        above = self.driver.find_element_by_css_selector(".TouP")
        ActionChains(self.driver).move_to_element(above).perform()

    #
    # ============================ #
    # -----  页面用到的方法  ------  #
    # ============================ #

    def login_front(self):
        """简化-前置登录"""
        loginPage.Login(self.driver).user_login_front()

    def na(self):
        """简化-导航部分"""
        return Navigation(self.driver)

    def na_personal(self):
        """简化-个人中心部分 登陆→ 鼠标悬浮个人中心位置"""
        self.login_front()
        self.na().navigation_personal_perform()
        sleep(2)

    def na_show_name(self):
        """获取显示导航名称"""
        show_list = []
        numberx = self.na().navigation_all_numberx()
        for i in range(numberx):
            textx = self.na().navigation_all_numberx_text(i)
            show_list.append(textx)
        return show_list

    def na_hide_name(self):
        """获取隐藏导航名称"""
        hide_list = []
        numbery = self.na().navigation_all_numbery()
        self.na().navigation_more_perform()
        sleep(2)
        for i in range(numbery):
            texty = self.na().navigation_all_numbery_text(i)
            hide_list.append(texty)
        return hide_list

    def na_custom(self):
        """获取自定义导航"""
        custom_list = self.na_show_name() + self.na_hide_name()
        custom_list.remove('首页')
        custom_list.remove('信息监控')
        custom_list.remove('告警预测')
        custom_list.remove('报告厅')
        custom_list.remove('业务统计')
        custom_list.remove('专题分析')
        return custom_list

    def na_check(self, name):
        """导航定位，name为导航名称"""
        if name in self.na_show_name():
            show_index = self.na_show_name().index(name)
            self.na().navigation_all_numberx_click(show_index)
        else:
            hide_index = self.na_hide_name().index(name)
            self.na().navigation_more_perform()
            self.na().navigation_all_numbery_click(hide_index)

    def na_personal_hide_name(self):
        """获取个人中心隐藏名称"""
        hide_list = []
        numbery = self.na().navigation_personal_numbery()
        self.na().navigation_personal_perform()
        sleep(2)
        for i in range(numbery):
            texty = self.na().navigation_personal_text(i)
            hide_list.append(texty)
        return hide_list

    def na_personal_check(self, name):
        """导航个人中心定位，name为个人中心下拉名称"""
        hide_index = self.na_personal_hide_name().index(name)
        self.na().navigation_personal_perform()
        self.na().navigation_personal_click(hide_index)
