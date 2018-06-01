from selenium.webdriver.common.by import By
from test_case.page import loginPage, navigationPage, method
from selenium.webdriver.common.action_chains import ActionChains
from .base import Page

'''
业务统计页面
'''


class Business(Page):

    business_left_navigation_loc = \
        (By.CSS_SELECTOR, ("span[id='24'][cotype='1']"))   # 左侧导航栏中个人储蓄名称获取
    business_head_title_loc = \
        (By.XPATH, "//*[@class='business']/h3/em")         # 展示区title业务种类/人储蓄名称获取
    business_keyword_loc = \
        (By.XPATH, "//*[@class='businessSearch']/input")   # 关键词输入框
    business_searchButton_loc = \
        (By.XPATH, "//*[@class='businessSearch']/button")  # 查询按钮

    business_timeDay_loc = \
        (By.XPATH, "//*[@id='-1']")                               # 筛选：时间一天
    business_timeWeek_loc = \
        (By.XPATH, "//*[@id='-7']")                               # 筛选：时间一周
    business_timeMonth_loc = \
        (By.XPATH, "//*[@id='-30']")                              # 筛选：时间一月
    business_timeCustom_loc = \
        (By.XPATH, "//*[@id='date-range200']")                    # 筛选：时间自定义
    business_timeCustom_selectStar_loc = \
        (By.XPATH, "//*[@class='month1']/tbody/tr[2]/td[2]/div")  # 筛选：选择时间自定义开始
    business_timeCustom_selectEnd_loc = \
        (By.XPATH, "//*[@class='month1']/tbody/tr[2]/td[4]/div")  # 筛选：选择时间自定义结束
    business_timeCustom_button_loc = \
        (By.XPATH, "//*[@unselectable='on']/div/input")           # 筛选：选择时间自定义确定
    business_sourceAll_loc = \
        (By.XPATH, "//*[@class='businessTermMedia']/li[1]")       # 筛选：来源全部
    business_sourceAll_error_text_loc = \
        (By.XPATH, "//*[@class='alertModelbox']/span")            # 筛选：来源全部-弹框文本
    business_sourceAll_error_OK_loc = \
        (By.XPATH, "//*[@class='alertModelBtn']/button")          # 筛选：来源全部-确定按钮
    business_sourceAll_error_close_loc = \
        (By.XPATH, "//*[@class='alertModelbox']/h6/strong/img")   # 筛选：来源全部-关闭按钮
    business_sourceNew_loc = \
        (By.XPATH, "//*[@class='businessTermMedia']/li[2]")       # 筛选：来源新闻
    business_sourceForum_loc = \
        (By.XPATH, "//*[@class='businessTermMedia']/li[3]")       # 筛选：来源论坛
    business_sourceBlog_loc = \
        (By.XPATH, "//*[@class='businessTermMedia']/li[4]")       # 筛选：来源博客
    business_sourceWeiBo_loc = \
        (By.XPATH, "//*[@class='businessTermMedia']/li[5]")       # 筛选：来源微博
    business_sourceWeChat_loc = \
        (By.XPATH, "//*[@class='businessTermMedia']/li[6]")       # 筛选：来源微信
    business_sourceFlatMedia_loc = \
        (By.XPATH, "//*[@class='businessTermMedia']/li[7]")       # 筛选：来源平媒
    business_sourceAPP_loc = \
        (By.XPATH, "//*[@class='businessTermMedia']/li[8]")       # 筛选：来源APP
    business_moodAll_loc = \
        (By.XPATH, "//*[@class='businessDep']/li[1]")             # 筛选：情绪全部
    business_moodPositive_loc = \
        (By.XPATH, "//*[@class='businessDep']/li[2]")             # 筛选：情绪正面
    business_moodNeutral_loc = \
        (By.XPATH, "//*[@class='businessDep']/li[3]")             # 筛选：情绪中立
    business_moodNegative_loc = \
        (By.XPATH, "//*[@class='businessDep']/li[4]")             # 筛选：情绪负面
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

    # 左侧导航名称获取（个人储蓄）
    def business_left_navigation_text(self):
        return self.find_element(*self.business_left_navigation_loc).text

    # 展示区title业务种类/储蓄名称获取
    def business_head_title_text(self):
        return self.find_element(*self.business_head_title_loc).text

    # 关键词输入框
    def business_keyword(self, keyword):
        self.find_element(*self.business_keyword_loc).send_keys(keyword)

    # 查询按钮
    def business_search_button(self):
        self.find_element(*self.business_searchButton_loc).click()

    # 时间筛选一天
    def business_time_day(self):
        self.find_element(*self.business_timeDay_loc).click()

    # 时间筛选一周
    def business_time_week(self):
        self.find_element(*self.business_timeWeek_loc).click()

    # 时间筛选一月
    def business_time_month(self):
        self.find_element(*self.business_timeMonth_loc).click()

    # 时间筛选自定义（3天）
    def business_time_custom(self):
        self.find_element(*self.business_timeCustom_loc).click()
        self.find_element(*self.business_timeCustom_selectStar_loc).click()
        self.find_element(*self.business_timeCustom_selectEnd_loc).click()
        self.find_element(*self.business_timeCustom_button_loc).click()

    # 来源筛选全部
    def business_source_all(self):
        self.find_element(*self.business_sourceAll_loc).click()

    # 来源筛选全部，弹框文本内容
    def business_source_all_error_text(self):
        return self.find_element(*self.business_sourceAll_error_text_loc).text

    # 来源筛选全部，弹框确定按钮
    def business_source_all_error_ok(self):
        self.find_element(*self.business_sourceAll_error_OK_loc).click()

    # 来源筛选全部，弹框关闭按钮
    def business_source_all_error_close(self):
        self.find_element(*self.business_sourceAll_error_close_loc).click()

    # 来源筛选新闻
    def business_source_new(self):
        self.find_element(*self.business_sourceNew_loc).click()

    # 来源筛选论坛
    def business_source_forum(self):
        self.find_element(*self.business_sourceForum_loc).click()

    # 来源筛选博客
    def business_source_blog(self):
        self.find_element(*self.business_sourceBlog_loc).click()

    # 来源筛选微博
    def business_source_weibo(self):
        self.find_element(*self.business_sourceWeiBo_loc).click()

    # 来源筛选微信
    def business_source_wechat(self):
        self.find_element(*self.business_sourceWeChat_loc).click()

    # 来源筛选平媒
    def business_source_flatmedia(self):
        self.find_element(*self.business_sourceFlatMedia_loc).click()

    # 来源筛选APP
    def business_source_app(self):
        self.find_element(*self.business_sourceAPP_loc).click()

    # 情绪筛选全部
    def business_mood_all(self):
        self.find_element(*self.business_moodAll_loc).click()

    # 情绪筛选正面
    def business_mood_positive(self):
        self.find_element(*self.business_moodPositive_loc).click()

    # 情绪筛选中立
    def business_mood_neutral(self):
        self.find_element(*self.business_moodNeutral_loc).click()

    # 情绪筛选负面
    def business_mood_negative(self):
        self.find_element(*self.business_moodNegative_loc).click()

    # 情绪筛选负面
    def business_time_sort(self):
        self.find_element(*self.business_timeSort_loc).click()

    # 当前页面所有情绪数量
    def business_page_moodall_number(self):
        return len(self.find_elements(*self.business_page_moodAll_loc))

    # 当前页面所有情绪文本
    def business_page_moodall_text(self, num):
        return self.find_elements(*self.business_page_moodAll_loc)[num].text

    # 定义统一查询入口
    def business_search(self, keyword="keyword"):
        self.business_keyword(keyword)
        self.business_search_button()

    #
    # ============================ #
    # -----    文章列表   --------- #
    # ============================ #

    # 时间排序按钮
    def business_timesort(self):
        self.find_element(*self.business_timeSort_loc).click()

    # 获取时间排序按钮文字
    def business_time_text(self):
        return self.find_element(*self.business_timeSort_loc).text

    # 文章列表信息勾选框
    def business_message_select(self, num):
        self.find_elements(*self.business_message_select_loc)[num].click()

    # 文章列表信息为空时提示文本获取
    def business_message_null_text(self):
        return self.find_element(*self.business_message_null_loc).text

    # 文章列表首条信息告警标识获取
    # def business_message_alarm(self):
    #     return self.find_element(*self.business_message_alarm_loc).text

    # 文章列表信息告警标识获取
    def business_message_alarm(self, num="获取第几条信息的告警标识"):
        return self.find_element(By.XPATH, "//*[@class='businessTableBox']/dl[" + num + "]/dt/span").text

    # 文章列表首条信息标题点击
    def business_message_title(self):
        self.find_element(*self.business_message_title_loc).click()

    # 文章列表首条信息标题获取
    def business_message_title_text(self):
        return self.find_element(*self.business_message_title_loc).text

    # 文章列表首条信息摘要点击
    def business_message_abstract(self):
        self.find_element(*self.business_message_abstract_loc).click()

    # 文章列表首条信息时间获取
    def business_message_time(self):
        return self.find_element(*self.business_message_time_loc).text

    # 文章列表首条信息来源获取
    def business_message_source(self):
        return self.find_element(*self.business_message_source_loc).text

    # 文章列表首条信息情绪获取
    def business_message_mood(self):
        return self.find_element(*self.business_message_mood_loc).text

    # 文章列表首条信息情绪 - 鼠标悬浮操作用
    def business_message_mood_chains(self):
        return self.find_element(*self.business_message_mood_loc)

    # 文章列表首条信息“生成报告”按钮
    def business_message_report(self):
        self.find_element(*self.business_message_report_loc).click()

    # 文章列表首条信息“生成报告”弹框- 输入框
    def business_message_report_input(self, text="text"):
        self.find_element(*self.business_message_report_input_loc).send_keys(text)

    # 获取文章新建报告文本错误提示
    def business_message_report_fail(self):
        return self.find_element(*self.business_message_report_fail_loc).text

    # 文章列表首条信息“生成报告” 弹框- 添加按钮
    def business_message_report_addbtn(self):
        self.find_element(*self.business_message_report_AddBtn_loc).click()

    # 文章列表首条信息“生成报告” 弹框- 关闭按钮
    def business_message_report_closebtn(self):
        self.find_element(*self.business_message_report_CloseBtn_loc).click()

    # 文章列表首条信息“修正”按钮
    def business_message_update(self):
        self.find_element(*self.business_message_update_loc).click()

    # 文章列表首条信息“修正”按钮-状态告警
    def business_message_update_alarm(self):
        self.find_element(*self.business_message_update_alarm_loc).click()

    # 文章列表首条信息“修正”按钮-状态正常
    def business_message_update_normal(self):
        self.find_element(*self.business_message_update_normal_loc).click()

    # 文章列表首条信息“修正”按钮-情绪正
    def business_message_update_positive(self):
        self.find_element(*self.business_message_update_positive_loc).click()

    # 文章列表首条信息“修正”按钮-情绪负
    def business_message_update_negative(self):
        self.find_element(*self.business_message_update_negative_loc).click()

    # 文章列表首条信息“修正”按钮-情绪中
    def business_message_update_neutral(self):
        self.find_element(*self.business_message_update_neutral_loc).click()

    # 文章列表首条信息“修正”按钮-确定按钮
    def business_message_update_ok(self):
        self.find_element(*self.business_message_update_ok_loc).click()

    # 文章列表首条信息“修正”按钮-关闭按钮
    def business_message_update_close(self):
        self.find_element(*self.business_message_update_close_loc).click()

    # 文章列表首条信息“导出”按钮
    def business_message_export(self):
        self.find_element(*self.business_message_export_loc).click()

    # 文章列表首条信息“收藏”按钮
    def business_message_collect(self):
        self.find_element(*self.business_message_collect_loc).click()

    # 文章列表首条信息“收藏”按钮-文本获取
    def business_message_collect_text(self):
        return self.find_element(*self.business_message_collect_loc).text

    # 文章列表首条信息“删除”按钮
    def business_message_delete(self):
        self.find_element(*self.business_message_delete_loc).click()

    #
    # ============================ #
    # -----    页面底部   --------- #
    # ============================ #

    # 上一页按钮
    def business_page_previouspage(self):
        self.find_element(*self.business_page_previousPage_loc).click()

    # 上一页按钮-文本获取
    def business_page_previouspage_text(self):
        return self.find_element(*self.business_page_previousPage_loc).text

    # 翻页第二页页码
    def business_page_number2(self):
        self.find_element(*self.business_page_number2_loc).click()

    # 下一页按钮
    def business_page_nextpage(self):
        self.find_element(*self.business_page_nextPage_loc).click()

    # 下一页按钮-文本获取
    def business_page_nextpage_text(self):
        return self.find_element(*self.business_page_nextPage_loc).text

    # 页面总条数顶部显示获取
    def business_totalnumber_up_text(self):
        return self.find_element(*self.business_totalNumber_up_loc).text

    # 页面总条数底部显示获取
    def business_totalnumber_down_text(self):
        return self.find_element(*self.business_totalNumber_down_loc).text

    # 页面底部的全选按钮
    def business_pagefoot_all(self):
        self.find_element(*self.business_pageFoot_all_loc).click()

    # 页面底部的“生成报告”按钮
    def business_pagefoot_report(self):
        self.find_element(*self.business_pageFoot_report_loc).click()

    # 页面底部的“修正”按钮
    def business_pagefoot_update(self):
        self.find_element(*self.business_pageFoot_update_loc).click()

    # 页面底部的“修正”按钮-错误提示信息文本
    def business_pagefoot_update_error_text(self):
        return self.find_element(*self.business_pageFoot_update_error_text_loc).text

    # 页面底部的“修正”按钮-错误提示信息关闭按钮
    def business_pagefoot_update_error_close(self):
        self.find_element(*self.business_pageFoot_update_error_close_loc).click()

    # 页面底部的“修正”按钮-错误提示信息确定按钮
    def business_pagefoot_update_error_button(self):
        self.find_element(*self.business_pageFoot_update_error_button_loc).click()

    # 页面底部的“导出”按钮
    def business_pagefoot_export(self):
        self.find_element(*self.business_pageFoot_export_loc).click()

    # 页面底部的“收藏”按钮
    def business_pagefoot_collect(self):
        self.find_element(*self.business_pageFoot_collect_loc).click()

    #
    # ============================ #
    # -----  页面用到的方法   —----- #
    # ============================ #

    # 前置登录→业务统计
    def front(self):
        loginPage.Login(self.driver).user_login_front()
        navigationPage.Navigation(self.driver).na_check("业务统计")

    # 简化-前置登录→业务统计→输入关键词
    def bu_keyword(self):
        self.front()
        self.business_search(keyword="中国")

    # 简化-前置登录→业务统计→选择一月
    def bu_time(self):
        self.front()
        self.business_time_month()

    # 简化-前置登录→业务统计→选择一月→来源为空
    def bu_time_sourcenull(self):
        self.front()
        self.business_time_month()
        self.business_source_all()
        self.business_source_all_error_ok()

    # 简化-前置登录→业务统计→选择一月→点击首条信息生成报告
    def bu_time_messagereport(self):
        self.front()
        self.business_time_month()
        chains = self.business_message_mood_chains()
        ActionChains(self.driver).move_to_element(chains).perform()
        self.business_message_report()

    # 简化-前置登录→业务统计→选择一月→点击首条信息修正
    def bu_time_messageupdate(self):
        self.front()
        self.business_time_month()
        chains = self.business_message_mood_chains()
        ActionChains(self.driver).move_to_element(chains).perform()
        self.business_message_update()

    # 简化-获取当前页面所有信息情绪不一致弹框
    def bu_mood_differ(self):
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

    # 简化-获取当前页面最后两条信息情绪一致弹框
    def bu_mood_equally(self):
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
