from selenium.webdriver.common.by import By
from .base import Page


class Method(Page):
    """  页面公共类，用于其他页面调用 """

    js = "var q=document.documentElement.scrollTop=10000"       # 滚动条至页面底部

    backHomePage_loc = \
        (By.XPATH, "//*[@class='suspendS']")                    # 回到首页
    homePage_alarmText_loc = \
        (By.XPATH, "//*[@class='homeCapBox']/div[2]/h6")        # 首页“告警信息”文字
    backTop_loc = \
        (By.XPATH, "//*[@class='suspendT']")                    # 回到顶部
    personal_loc = \
        (By.CLASS_NAME, "TouP")                                 # 个人信息位置

    allLibrary_search_loc = ""


    def js_bottom(self):
        """页面滚动条下拉到底"""
        self.script(self.js)

    def back_homepage(self):
        """回到首页按钮"""
        self.find_element(*self.backHomePage_loc).click()

    def back_top(self):
        """回到顶部按钮"""
        self.find_element(*self.backTop_loc).click()

    def personal_text(self):
        """个人信息位置"""
        return self.find_element(*self.personal_loc).text
