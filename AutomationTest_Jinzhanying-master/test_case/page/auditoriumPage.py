from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

'''
报告厅页面
'''


class Auditorium(Page):

    briefing_title_loc = \
        (By.XPATH, "//*[@class='briefing']/div/div[1]")          # 第一条简报名称获取
    briefing_time_loc = \
        (By.XPATH, "//*[@class='briefing']/div/div[3]/b/span")   # 第一条简报时间获取

    # 第一条简报名称获取
    def briefing_title(self):
        return self.find_element(*self.briefing_title_loc).text

    # 第一条简报时间获取
    def briefing_time(self):
        return self.find_element(*self.briefing_time_loc).text
