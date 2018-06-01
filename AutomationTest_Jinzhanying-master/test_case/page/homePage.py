from selenium.webdriver.common.by import By
from .base import Page

'''
首页页面
'''


class Home(Page):

    home_business_no1_loc = \
        (By.CSS_SELECTOR, "span[id='a24'][style='cursor: pointer;']")  # 业务分类统计中个人储蓄名称获取
    home_alarm_text_loc = \
        (By.XPATH, "//*[@class='homeCapBox']/div[2]/h6")        # 首页“告警信息”文字

    #
    # ============================ #
    # -----  搜索条件 ---------     #
    # ============================ #

    # 左侧导航名称获取（个人储蓄）
    def home_business_no1_text(self):
        return self.find_element(*self.home_business_no1_loc).text

    # 首页-“告警信息”文本
    def home_alarm_text(self):
        return self.find_element(*self.home_alarm_text_loc).text
