from selenium.webdriver.common.by import By
from test_case.page import loginPage, navigationPage, method
from selenium.webdriver.common.action_chains import ActionChains
from .base import Page

'''
业务统计页面 - 优化版
'''


class Business(Page):

    business_head_title_loc = \
        (By.XPATH, "//*[@class='business']/h3/em")         # 展示区title业务种类获取
    business_keyword_loc = \
        (By.XPATH, "//*[@class='businessSearch']/input")   # 关键词输入框
    business_searchButton_loc = \
        (By.XPATH, "//*[@class='businessSearch']/button")  # 查询按钮

    business_time_loc = \
        (By.XPATH, "//*[@class='businessTermTime']/li")           # 筛选：时间选择
    business_timeCustom_selectStar_loc = \
        (By.XPATH, "//*[@class='month1']/tbody/tr[2]/td[2]/div")  # 筛选：选择时间自定义开始
    business_timeCustom_selectEnd_loc = \
        (By.XPATH, "//*[@class='month1']/tbody/tr[2]/td[4]/div")  # 筛选：选择时间自定义结束
    business_timeCustom_button_loc = \
        (By.XPATH, "//*[@unselectable='on']/div/input")           # 筛选：选择时间自定义确定
    business_source_loc = \
        (By.XPATH, "//*[@class='businessTermMedia']/li")          # 筛选：来源选择
    business_sourceAll_error_text_loc = \
        (By.XPATH, "//*[@class='alertModelbox']/span")            # 筛选：来源全部-弹框文本
    business_sourceAll_error_OK_loc = \
        (By.XPATH, "//*[@class='alertModelBtn']/button")          # 筛选：来源全部-确定按钮
    business_sourceAll_error_close_loc = \
        (By.XPATH, "//*[@class='alertModelbox']/h6/strong/img")   # 筛选：来源全部-关闭按钮
    business_mood_loc = \
        (By.XPATH, "//*[@class='businessDep']/li")                # 筛选：情绪选择
    business_page_moodAll_loc = \
        (By.XPATH, "//*[@class='businessBotMar']")                # 当前页面所有信息情绪

    business_timeSort_loc = \
        (By.XPATH, "//*[@class='businessTableTimes']")                          # 时间正倒排序
    business_message_select_loc = \
        (By.XPATH, "//*[@name='businesCheck']")                                 # 文章信息勾选框选择
    business_message_null_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl/div")                     # 文章信息列表为空文本
    business_message_alarm_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dt/span")              # 文章信息列表告警文本
    business_message_title_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dt/a")                 # 文章列表首条信息标题
    business_message_abstract_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dd[2]/a")              # 文章列表首条信息摘要
    business_message_time_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dd[1]/span")           # 文章列表首条信息时间
    business_message_source_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dd[1]/i[2]")           # 文章列表首条信息来源
    business_message_mood_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dd[3]/b")              # 文章列表首条信息情绪
    business_message_report_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dd[3]/div/button[1]")  # 文章列表首条信息“生成报告”按钮
    business_message_report_input_loc = \
        (By.XPATH, "//*[@class='IndexAddBoxIN']/input")                         # 文章列表首条信息“生成报告”按钮-输入框
    business_message_report_fail_loc = \
        (By.XPATH, "//*[@class='IndexAddBoxIN']/b")                             # 文章列表首条信息“生成报告”按钮-错误提示
    business_message_report_AddBtn_loc = \
        (By.XPATH, "//*[@class='IndexAddBoxBtn']/button")                       # 文章列表首条信息“生成报告”按钮-添加按钮
    business_message_report_CloseBtn_loc = \
        (By.XPATH, "//*[@class='IndexAddBox']/h6/strong/img")                   # 文章列表首条信息“生成报告”按钮-关闭按钮
    business_message_update_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dd[3]/div/button[2]")  # 文章列表首条信息“修正”按钮
    business_message_update_alarm_loc = \
        (By.XPATH, "//*[@class='EditorBox']/div[1]/span[1]")                    # 文章列表首条信息“修正”按钮-状态告警
    business_message_update_normal_loc = \
        (By.XPATH, "//*[@class='EditorBox']/div[1]/span[2]")                    # 文章列表首条信息“修正”按钮-状态正常
    business_message_update_positive_loc = \
        (By.XPATH, "//*[@class='EditorBox']/div[2]/span[1]")                    # 文章列表首条信息“修正”按钮-情绪正
    business_message_update_negative_loc = \
        (By.XPATH, "//*[@class='EditorBox']/div[2]/span[2]")                    # 文章列表首条信息“修正”按钮-情绪负
    business_message_update_neutral_loc = \
        (By.XPATH, "//*[@class='EditorBox']/div[2]/span[3]")                    # 文章列表首条信息“修正”按钮-情绪中
    business_message_update_ok_loc = \
        (By.XPATH, "//*[@class='EditorBoxBtn']/button")                         # 文章列表首条信息“修正”按钮-确定按钮
    business_message_update_close_loc = \
        (By.XPATH, "//*[@class='EditorBox']/h6/strong/img")                     # 文章列表首条信息“修正”按钮-关闭按钮
    business_message_export_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dd[3]/div/button[3]")  # 文章列表首条信息“导出”按钮
    business_message_collect_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dd[3]/div/button[4]")  # 文章列表首条信息“收藏”按钮
    business_message_delete_loc = \
        (By.XPATH, "//*[@class='businessTableBox']/dl[1]/dd[3]/div/button[5]")  # 文章列表首条信息“删除”按钮

    business_page_previousPage_loc = \
        (By.XPATH, "//*[@class='shang']")                         # 翻页-上一页
    business_page_number2_loc = \
        (By.XPATH, "//*[@class='anniu']/li[2]")                   # 翻页-第二页
    business_page_nextPage_loc = \
        (By.XPATH, "//*[@class='xia']")                           # 翻页-下一页
    business_totalNumber_up_loc = \
        (By.XPATH, "//*[@class='businessTermBoxs']/b")            # 页面总条数顶部显示
    business_totalNumber_down_loc = \
        (By.XPATH, "//*[@class='pagemess']")                      # 页面总条数底部显示
    business_pageFoot_all_loc = \
        (By.XPATH, "//*[@class='tabelFooter']/label")             # 页面底部的全选按钮
    business_pageFoot_report_loc = \
        (By.XPATH, "//*[@class='tabelFooter']/button[1]")         # 页面底部的“生成报告”按钮
    business_pageFoot_update_loc = \
        (By.XPATH, "//*[@class='tabelFooter']/button[2]")         # 页面底部的“修正”按钮
    business_pageFoot_update_error_text_loc = \
        (By.XPATH, "//*[@class='alertModelbox']/span")            # 页面底部的“修正”按钮-错误弹框提示文本
    business_pageFoot_update_error_close_loc = \
        (By.XPATH, "//*[@class='alertModelbox']/h6/strong/img")   # 页面底部的“修正”按钮-错误弹框提示关闭按钮
    business_pageFoot_update_error_button_loc = \
        (By.XPATH, "//*[@class='alertModelBtn']/button")          # 页面底部的“修正”按钮-错误弹框提示确定按钮
    business_pageFoot_export_loc = \
        (By.XPATH, "//*[@class='tabelFooter']/button[3]")         # 页面底部的“导出”按钮
    business_pageFoot_collect_loc = \
        (By.XPATH, "//*[@class='tabelFooter']/button[4]")         # 页面底部的“收藏”按钮

    #
    # ============================ #
    # -----  搜索条件 ---------     #
    # ============================ #

    def business_left_navigation1(self, number1):
        """左侧导航栏 - 一级菜单选择, number1.选择一级菜单"""
        number1len = len(self.find_elements(By.XPATH, "//*[@class='businessNav']/ul/li"))
        if int(number1) <= number1len:
            return self.find_element(
                By.XPATH, "//*[@class='businessNav']/ul/li[" + number1 + "]").click()
        else:
            print("Error:输入的一级菜单不存在，请重新输入！")

    def business_left_navigation2(self, number1, number2):
        """左侧导航栏 - 二级菜单选择, number1.选择一级菜单, number2.选择二级菜单"""
        number2len = len(self.find_elements(
            By.XPATH, "//*[@class='businessNav']/ul/li[" + number1 + "]/em/span"))
        if int(number2) <= number2len:
            return self.find_element(
                By.XPATH, "//*[@class='businessNav']/ul/li[" + number1 + "]/em/span[" + number2 + "]").click()
        else:
            print("Error:输入的二级菜单不存在，请重新输入！")

    def business_left_navigation_text(self, number1, number2):
        """左侧导航栏名称获取 - number1.选择一级菜单、number2.选择二级菜单"""
        return self.find_element(
            By.XPATH, "//*[@class='businessNav']/ul/li[" + number1 + "]/em/span[" + number2 + "]").text

    def business_head_title_text(self):
        """展示区title业务种类名称获取"""
        return self.find_element(*self.business_head_title_loc).text

    def business_keyword(self, keyword):
        """ 关键词输入框"""
        self.find_element(*self.business_keyword_loc).send_keys(keyword)

    def business_search_button(self):
        """ 查询按钮 """
        self.find_element(*self.business_searchButton_loc).click()

    def business_time_select_time(self, num):
        """ 时间筛选(0.一天； 1.一周； 2.一月； 3.自定义) """
        self.find_elements(*self.business_time_loc)[num].click()

    def business_time_custom(self):
        """时间筛选自定义（3天）"""
        self.business_time_select_time(3)
        self.find_element(*self.business_timeCustom_selectStar_loc).click()
        self.find_element(*self.business_timeCustom_selectEnd_loc).click()
        self.find_element(*self.business_timeCustom_button_loc).click()

    def business_source_select(self, num):
        """来源筛选(0.全部； 1.新闻； 2.论坛； 3.博客； 4.微博； 5.微信； 6.平媒； 7.APP)"""
        self.find_elements(*self.business_source_loc)[num].click()

    def business_source_all_error_text(self):
        """来源筛选全部，弹框文本内容"""
        return self.find_element(*self.business_sourceAll_error_text_loc).text

    def business_source_all_error_ok(self):
        """来源筛选全部，弹框确定按钮"""
        self.find_element(*self.business_sourceAll_error_OK_loc).click()

    def business_source_all_error_close(self):
        """来源筛选全部，弹框关闭按钮"""
        self.find_element(*self.business_sourceAll_error_close_loc).click()

    def business_mood_all(self, num):
        """情绪筛选(0.全部； 1.正面； 2.中立； 3.负面"""
        self.find_element(*self.business_mood_loc)[num].click()

    def business_page_moodall_number(self):
        """当前页面所有情绪数量"""
        return len(self.find_elements(*self.business_page_moodAll_loc))

    def business_page_moodall_text(self, num):
        """当前页面第几条的情绪文本"""
        return self.find_elements(*self.business_page_moodAll_loc)[num].text

    # 定义统一查询入口
    def business_search(self, keyword="keyword"):
        """定义统一查询入口"""
        self.business_keyword(keyword)
        self.business_search_button()

    #
    # ============================ #
    # -----    文章列表   --------- #
    # ============================ #

    def business_timesort(self):
        """时间排序按钮"""
        self.find_element(*self.business_timeSort_loc).click()

    def business_time_text(self):
        """获取时间排序按钮文字"""
        return self.find_element(*self.business_timeSort_loc).text

    def business_message_select(self, num):
        """文章列表信息勾选框"""
        self.find_elements(*self.business_message_select_loc)[num].click()

    def business_message_null_text(self):
        """文章列表信息为空时提示文本获取"""
        return self.find_element(*self.business_message_null_loc).text

    def business_message_alarm(self, num):
        """获取文章列表信息告警标识获取"""
        return self.find_element(By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dt/span").text

    def business_message_title(self):
        """文章列表首条信息标题点击"""
        self.find_element(*self.business_message_title_loc).click()

    def business_message_title_text(self):
        """文章列表首条信息标题获取"""
        return self.find_element(*self.business_message_title_loc).text

    def business_message_abstract(self):
        """文章列表首条信息摘要点击"""
        self.find_element(*self.business_message_abstract_loc).click()

    def business_message_time(self):
        """文章列表首条信息时间获取"""
        return self.find_element(*self.business_message_time_loc).text

    def business_message_source(self):
        """文章列表首条信息来源获取"""
        return self.find_element(*self.business_message_source_loc).text

    def business_message_mood(self):
        """文章列表首条信息情绪获取"""
        return self.find_element(*self.business_message_mood_loc).text

    def business_message_mood_chains(self):
        """文章列表首条信息情绪 - 鼠标悬浮操作用"""
        return self.find_element(*self.business_message_mood_loc)

    def business_message_report(self):
        """文章列表首条信息“生成报告”按钮"""
        self.find_element(*self.business_message_report_loc).click()

    def business_message_report_input(self, text="text"):
        """文章列表首条信息“生成报告”弹框- 输入框"""
        self.find_element(*self.business_message_report_input_loc).send_keys(text)

    def business_message_report_fail(self):
        """获取文章新建报告文本错误提示"""
        return self.find_element(*self.business_message_report_fail_loc).text

    def business_message_report_addbtn(self):
        """文章列表首条信息“生成报告” 弹框- 添加按钮"""
        self.find_element(*self.business_message_report_AddBtn_loc).click()

    def business_message_report_closebtn(self):
        """文章列表首条信息“生成报告” 弹框- 关闭按钮"""
        self.find_element(*self.business_message_report_CloseBtn_loc).click()

    def business_message_update(self):
        """文章列表首条信息“修正”按钮"""
        self.find_element(*self.business_message_update_loc).click()

    def business_message_update_alarm(self):
        """文章列表首条信息“修正”按钮-状态告警"""
        self.find_element(*self.business_message_update_alarm_loc).click()

    def business_message_update_normal(self):
        """文章列表首条信息“修正”按钮-状态正常"""
        self.find_element(*self.business_message_update_normal_loc).click()

    def business_message_update_positive(self):
        """文章列表首条信息“修正”按钮-情绪正"""
        self.find_element(*self.business_message_update_positive_loc).click()

    def business_message_update_negative(self):
        """文章列表首条信息“修正”按钮-情绪负"""
        self.find_element(*self.business_message_update_negative_loc).click()

    def business_message_update_neutral(self):
        """文章列表首条信息“修正”按钮-情绪中"""
        self.find_element(*self.business_message_update_neutral_loc).click()

    def business_message_update_ok(self):
        """文章列表首条信息“修正”按钮-确定按钮"""
        self.find_element(*self.business_message_update_ok_loc).click()

    def business_message_update_close(self):
        """文章列表首条信息“修正”按钮-关闭按钮"""
        self.find_element(*self.business_message_update_close_loc).click()

    def business_message_export(self):
        """文章列表首条信息“导出”按钮"""
        self.find_element(*self.business_message_export_loc).click()

    def business_message_collect(self):
        """文章列表首条信息“收藏”按钮"""
        self.find_element(*self.business_message_collect_loc).click()

    def business_message_collect_text(self):
        """文章列表首条信息“收藏”按钮-文本获取"""
        return self.find_element(*self.business_message_collect_loc).text

    def business_message_delete(self):
        """文章列表首条信息“删除”按钮"""
        self.find_element(*self.business_message_delete_loc).click()

    #
    # ============================ #
    # -----    页面底部   --------- #
    # ============================ #

    def business_page_previouspage(self):
        """上一页按钮"""
        self.find_element(*self.business_page_previousPage_loc).click()

    def business_page_previouspage_text(self):
        """上一页按钮-文本获取"""
        return self.find_element(*self.business_page_previousPage_loc).text

    def business_page_number2(self):
        """翻页第二页页码"""
        self.find_element(*self.business_page_number2_loc).click()

    def business_page_nextpage(self):
        """下一页按钮"""
        self.find_element(*self.business_page_nextPage_loc).click()

    def business_page_nextpage_text(self):
        """下一页按钮-文本获取"""
        return self.find_element(*self.business_page_nextPage_loc).text

    def business_totalnumber_up_text(self):
        """页面总条数顶部显示获取"""
        return self.find_element(*self.business_totalNumber_up_loc).text

    def business_totalnumber_down_text(self):
        """页面总条数底部显示获取"""
        return self.find_element(*self.business_totalNumber_down_loc).text

    def business_pagefoot_all(self):
        """页面底部的全选按钮"""
        self.find_element(*self.business_pageFoot_all_loc).click()

    def business_pagefoot_report(self):
        """页面底部的“生成报告”按钮"""
        self.find_element(*self.business_pageFoot_report_loc).click()

    def business_pagefoot_update(self):
        """页面底部的“修正”按钮"""
        self.find_element(*self.business_pageFoot_update_loc).click()

    def business_pagefoot_update_error_text(self):
        """页面底部的“修正”按钮-错误提示信息文本"""
        return self.find_element(*self.business_pageFoot_update_error_text_loc).text

    def business_pagefoot_update_error_close(self):
        """页面底部的“修正”按钮-错误提示信息关闭按钮"""
        self.find_element(*self.business_pageFoot_update_error_close_loc).click()

    def business_pagefoot_update_error_button(self):
        """页面底部的“修正”按钮-错误提示信息确定按钮"""
        self.find_element(*self.business_pageFoot_update_error_button_loc).click()

    def business_pagefoot_export(self):
        """页面底部的“导出”按钮"""
        self.find_element(*self.business_pageFoot_export_loc).click()

    def business_pagefoot_collect(self):
        """页面底部的“收藏”按钮"""
        self.find_element(*self.business_pageFoot_collect_loc).click()

    #
    # ============================ #
    # -----  页面用到的方法   —----- #
    # ============================ #

    def front(self):
        """前置登录→业务统计"""
        loginPage.Login(self.driver).user_login_front()
        navigationPage.Navigation(self.driver).na_check("业务统计")

    def bu_keyword(self):
        """简化-前置登录→业务统计→输入关键词"""
        self.front()
        self.business_search(keyword="中国")

    def bu_time(self):
        """简化-前置登录→业务统计→选择一月"""
        self.front()
        self.business_time_select_time(2)

    def bu_time_sourcenull(self):
        """简化-前置登录→业务统计→选择一月→来源为空"""
        self.front()
        self.business_time_select_time(2)
        self.business_source_select(0)
        self.business_source_all_error_ok()

    def bu_time_messagereport(self):
        """简化-前置登录→业务统计→选择一月→点击首条信息生成报告"""
        self.front()
        self.business_time_select_time(2)
        chains = self.business_message_mood_chains()
        ActionChains(self.driver).move_to_element(chains).perform()
        self.business_message_report()

    def bu_time_messageupdate(self):
        """简化-前置登录→业务统计→选择一月→点击首条信息修正"""
        self.front()
        self.business_time_select_time(2)
        chains = self.business_message_mood_chains()
        ActionChains(self.driver).move_to_element(chains).perform()
        self.business_message_update()

    def bu_mood_differ(self):
        """简化-获取当前页面所有信息情绪不一致弹框"""
        mood = []
        num = self.business_page_moodall_number()
        for i in range(num):
            text = self.business_page_moodall_text(i)
            mood.append(text)
        while len(list(set(mood))) == 1:
            method.Method(self.driver).js_bottom()
            self.business_page_nextpage()
            mood = []
            num = self.business_page_moodall_number()
            for i in range(num):
                text = self.business_page_moodall_text(i)
                mood.append(text)
            if len(list(set(mood))) > 1:
                break
        method.Method(self.driver).js_bottom()
        self.business_pagefoot_all()
        self.business_pagefoot_update()

    def bu_mood_equally(self):
        """简化-获取当前页面最后两条信息情绪一致弹框"""
        text1 = self.business_page_moodall_text(13)
        text2 = self.business_page_moodall_text(14)
        while text1 != text2:
            method.Method(self.driver).js_bottom()
            self.business_page_nextpage()
            text1 = self.business_page_moodall_text(13)
            text2 = self.business_page_moodall_text(14)
            if text1 == text2:
                break
        method.Method(self.driver).js_bottom()
        self.business_message_select(13)
        self.business_message_select(14)
        self.business_pagefoot_update()
