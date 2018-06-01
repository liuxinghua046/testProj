from selenium.webdriver.common.by import By

from test_case.page import loginPage, navigationPage
from .base import Page

'''
专题分析页面
'''


class Analysis(Page):

    analysis_keyWord_input_loc = \
        (By.XPATH, "//*[@class='businessSearch']/input")      # 关键词输入框
    analysis_search_button_loc = \
        (By.XPATH, "//*[@class='businessSearch']/button")     # 查询按钮
    analysis_screen_time_loc = \
        (By.XPATH, "//*[@class='businessTermTime']/li")       # 时间筛选
    analysis_screen_business_loc = \
        (By.XPATH, "//*[@class='businessTermClass']/li")      # 业务筛选
    analysis_sort_loc = \
        (By.XPATH, "//*[@class='businessTableTop']/li")       # 排序条件

    analysis_message_top_close_loc = \
        (By.XPATH, "//*[@class='stickBox']/h6/strong/img")       # 专题-置顶关闭按钮
    analysis_message_top_cancel_loc = \
        (By.XPATH, "//*[@class='stickBox']/div/button[2]")       # 专题-置顶取消按钮
    analysis_message_top_ok_loc = \
        (By.XPATH, "//*[@class='stickBox']/div/button[1]")       # 专题-置顶确定按钮

    analysis_pageFoot_all_button_loc = \
        (By.XPATH, "//*[@class='tabelFooter']/div/input")     # 全选按钮
    analysis_pageFoot_del_button_loc = \
        (By.XPATH, "//*[@class='tabelFooter']/div/button")    # 批量删除按钮
    analysis_pageFoot_number_loc = \
        (By.XPATH, "//*[@class='pagemess']")                  # 总条数获取

    analysis_generationTopics_button_loc = \
        (By.LINK_TEXT, "生成专题")                                            # 生成专题按钮
    analysis_gt_name_input_loc = \
        (By.XPATH, "//*[@class='businessTerm businessTermName']/input")      # 生成专题页面-专题名称输入框
    analysis_gt_select_time_loc = \
        (By.XPATH, "//*[@class='businessTermTime']/li")                      # 生成专题页面-时间选择
    analysis_gt_select_region_loc = \
        (By.XPATH, "//*[@class='businessTermType']/li")                      # 生成专题页面-地域选择
    analysis_gt_keyWord_input_loc = \
        (By.XPATH, "//*[@class='businessTerm businessTermWord']/input")      # 生成专题页面-关键词输入框
    analysis_gt_select_business_loc = \
        (By.XPATH, "//*[@class=businessTermType businessTermTypeye']/li")    # 生成专题页面-业务分类选择
    analysis_gt_select_media_loc = \
        (By.XPATH, "//*[@class=businessTermMedia']/li")                      # 生成专题页面-媒体类型选择
    analysis_gt_gtButton_loc = \
        (By.XPATH, "//*[@class=creatReqort']/button")                        # 生成专题页面-生成专题按钮

    analysis_situationAnalysis_loc = \
        (By.LINK_TEXT, "态势解析")               # 态势解析按钮

    analysis_back_loc = \
        (By.LINK_TEXT, "返回")                   # 返回按钮

    def analysis_keyword_input(self, keyword="关键词"):
        """关键词输入框"""
        self.find_element(*self.analysis_keyWord_input_loc).send_keys(keyword)

    # 查询按钮
    def analysis_search_button(self):
        self.find_element(*self.analysis_search_button_loc).click()

    # 筛选时间(0.一天； 1.一周； 2.一月； 3.自定义)
    def analysis_screen_time(self, num="0.一天； 1.一周； 2.一月； 3.自定义"):
        self.find_elements(*self.analysis_screen_time_loc)[num].click()

    # 筛选业务(第零个为全部，其他按序号获取)
    def analysis_screen_business(self, num="第零个为全部，其他按序号获取"):
        self.find_elements(*self.analysis_screen_business_loc)[num].click()

    # 排序条件(0.生成时间； 1.开始时间； 2.结束时间； 3.信息数)
    def analysis_sort(self, num="0.生成时间； 1.开始时间； 2.结束时间； 3.信息数"):
        self.find_elements(*self.analysis_sort_loc)[num].click()

    # 专题-单选按钮
    def analysis_message_radio_button(self, num="点击第几条专题的单选按钮"):
        self.find_elements(By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dt/input").click()

    # 专题-标题文本获取
    def analysis_message_title_text(self, num="获取第几条专题的标题信息"):
        return self.find_elements(By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dt/a").text

    # 专题-置顶按钮
    def analysis_message_top_button(self, num="点击第几条专题的置顶按钮"):
        self.find_elements(By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dt/span").click()

    # 专题-置顶文本获取
    def analysis_message_top_text(self, num="获取第几条专题的置顶文本"):
        return self.find_elements(By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dt/span").text

    # 专题-1.生成时间、2.结束时间、3.持续时间、4.状态、5.业务文本获取
    def analysis_message_head_text(self, num="获取第几条专题的置顶文本",
                                   head='1.生成时间、2.结束时间、3.持续时间、4.状态、5.业务'):
        return self.find_elements(
            By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dd[1]/i[" + head + "]").text

    # 专题-关键词文本获取
    def analysis_message_keyword_text(self, num="获取第几条专题的关键词文本"):
        return self.find_elements(By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dd[2]/b[1]").text

    # 专题-1.信息数、2站点文本获取
    def analysis_message_foot_text(self, num="获取第几条专题的关键词文本", foot='1.信息数、2站点'):
        return self.find_elements(
            By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dd[3]/i[" + foot + "]").text

    # 专题-1.删除、2.编辑、3.传播分析按钮
    def analysis_message_foot_button_text(self, num="获取第几条专题的关键词文本",
                                          button='1.删除、2.编辑、3.传播分析'):
        self.find_elements(
            By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dd[3]/button[" + button + "]").click()

    # 全选按钮
    def analysis_pagefoot_all_button(self):
        self.find_element(*self.analysis_pageFoot_all_button_loc).click()

    # 批量删除按钮
    def analysis_pagefoot_del_button(self):
        self.find_element(*self.analysis_pageFoot_del_button_loc).click()

    # 总条数获取
    def analysis_pagefoot_number_loc(self):
        return self.find_element(*self.analysis_pageFoot_number_loc).text

    #
    # ============================ #
    # -----  生成专题页面  -------   #
    # ============================ #

    # 生成专题按钮
    def analysis_generation_topics_button(self):
        self.find_element(*self.analysis_generationTopics_button_loc).click()

    # 专题名称输入框
    def analysis_gt_name_input(self, keyword="专题名称"):
        self.find_element(*self.analysis_gt_name_input_loc).send_keys(keyword)

    # 时间选择(0.一天； 1.一周； 2.一月； 3.自定义)
    def analysis_gt_select_time(self, num="0.一天； 1.一周； 2.一月； 3.自定义"):
        self.find_elements(*self.analysis_gt_select_time_loc)[num].click()

    # 地域选择(第零个为全国，其他按序号获取)
    def analysis_gt_select_region(self, num="第零个为全国，其他按序号获取"):
        self.find_elements(*self.analysis_gt_select_region_loc)[num].click()

    # 关键词输入框(0.与关键词； 1.或关键词； 2.屏蔽词)
    def analysis_gt_keyword_input_loc(self, num="0.与关键词； 1.或关键词； 2.屏蔽词", keyword="关键词"):
        self.find_elements(*self.analysis_gt_keyWord_input_loc)[num].send_keys(keyword)

    # 业务分类选择(按序号从零开始获取)
    def analysis_gt_select_business(self, num="业务分类按序号从零开始获取"):
        self.find_elements(*self.analysis_gt_select_business_loc)[num].click()

    # 媒体类型选择(0.全部； 1.新闻； 2.论坛； 3.博客； 4.微博； 5.微信； 6.平媒； 7.APP)
    def analysis_gt_select_media(self, num="0.全部； 1.新闻； 2.论坛； 3.博客； 4.微博； 5.微信； 6.平媒； 7.APP"):
        self.find_elements(*self.analysis_gt_select_media_loc)[num].click()

    #
    # ============================ #
    # -----  态势解析页面  -------   #
    # ============================ #

    #
    # ============================ #
    # -----  页面用到的方法   —----- #
    # ============================ #

    # 前置登录→业务统计
    def front(self):
        loginPage.Login(self.driver).user_login_front()
        navigationPage.Navigation(self.driver).na_check("专题分析")
