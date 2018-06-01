from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

'''
个人中心 - 收藏关注页面
'''


class Pca(Page):

    collection_title_loc = \
        (By.XPATH, "//*[@class='pershoucang']/tbody/tr/td[2]/a")   # 收藏列表第一条标题
    collection_number_all_loc = \
        (By.XPATH, "//*[@class='box']/div[5]")   # 收藏列表总条数

    # 收藏列表第一条标题
    def collection_title_text(self):
        return self.find_element(*self.collection_title_loc).text

    # 收藏列表总条数
    def collection_number_all(self):
        return self.find_element(*self.collection_number_all_loc).text
