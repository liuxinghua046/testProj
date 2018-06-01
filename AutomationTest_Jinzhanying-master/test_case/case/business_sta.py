from time import sleep

from test_case.models import myunit
from test_case.models.function import Function
from test_case.page import homePage, navigationPage, businessPage, auditoriumPage, loginPage, method
from test_case.page import peCollectionAttentionPage as pca
from selenium.webdriver.common.action_chains import ActionChains
import unittest

'''
@ name: 业务统计页面测试用例
@ test：1.关联名称校验：
          1.1 检验展示区名称（个人储蓄）是否和左侧导航栏名称（个人储蓄）一致；
          1.2 检验展示区名称（个人储蓄）是否和首页业务统计中个人储蓄名称一致。
        2.关键词输入框校验：
          2.1 关键输入“中国”；
        3.筛选
          3.1时间选择：
              3.1.1 选择一周；
              3.1.2 选择一月；
              3.1.3 选择一天；
              3.1.4 选择自定义。    
          3.2.情绪选择：
              3.2.1 查看全部条数和正面、中立、全部是否一致;
              3.2.2 选择正面；
              3.2.3 选择中立；
              3.2.4 选择负面；
              3.2.5 选择全部。
          3.3来源选择：          
              3.3.1 来源选择全部取消:
                3.3.1.1 弹窗提示；
                3.3.1.2 弹窗确认；
                3.3.1.3 弹窗关闭。
              3.3.2 来源选择新闻；
              3.3.3 来源选择论坛； 
              3.3.4 来源选择博客；   
              3.3.5 来源选择微博；   
              3.3.6 来源选择微信；
              3.3.7 来源选择平媒；  
              3.3.8 来源选择APP；    
              3.3.9 来源进行组合查询；
              3.3.10选择全部。      
        4.时间排序：
          4.1 时间选择正序排序；
          4.2 时间选择倒序排序。
        5.文章列表单条
          5.1生成报告：
              5.1.1 弹框点击关闭按钮；
              5.1.2 输入小于10位的数字、字母、中文组合，选择任意标签，点击添加按钮；
              5.1.3 输入框为空，点击添加按钮；
              5.1.4 输入空格，点击添加按钮；
              5.1.5 输入框输入大于十位字符，点击添加按钮；
              5.1.6 输入框输入特殊字符，点击添加按钮。
          5.2修正：
              5.2.1 弹框点击关闭按钮；
              5.2.2 状态选择告警，点击确认按钮；
              5.2.3 状态选择正常，点击确认按钮；
              5.2.4 情绪选择正，点击确认按钮；
              5.2.5 情绪选择负，点击确认按钮；
              5.2.6 情绪选择中，点击确认按钮。
          5.3导出：
          5.4收藏：
              5.4.1 点击收藏按钮后是否变为取消收藏；
              5.4.2 查看收藏关注中是否有此条信息。 
          5.5删除：                                --- 待后台完成后实现
              5.5.1 删除原因广告，点击直接删除信息； 
              5.5.2 删除原因不重要，点击直接删除信息；
              5.5.3 删除原因旧文重复，点击直接删除信息；
              5.5.4 删除原因其他，点击直接删除信息。
          5.6页面跳转：
              5.6.1 点击标题后查看和原文标题是否一致
              5.6.2 点击摘要后查看和原文标题是否一致
        6.批量操作
          6.1 全选生成报告    --- 下载的word文档格式问题，无法读取
          6.2 全选修正：      
              6.2.1 不同类型时修正:
                  6.2.1.1 弹出提示信息；
                  6.2.1.2 点击关闭按钮；
                  6.2.1.3 点击确定按钮。
              6.2.2 同类型时修正：             
                  6.2.2.1 弹框点击关闭按钮；
                  6.2.2.2 状态选择告警，点击确认按钮；  --- 功能Bug，待实现
                  6.2.2.3 状态选择正常，点击确认按钮；  --- 功能Bug，待实现
                  6.2.2.4 情绪选择正，点击确认按钮；    --- 功能Bug，待实现
                  6.2.2.5 情绪选择负，点击确认按钮；    --- 功能Bug，待实现
                  6.2.2.6 情绪选择中，点击确认按钮。    --- 功能Bug，待实现
          6.3 全选导出；
          6.4 全选收藏；
        7.页码           
          7.1 顶部与底部的页码总条数是否一致；
          7.2 页码点击跳转；
          7.3 上一页操作；
          7.4 下一页操作。
        8.回到首页；
        9.回到顶部。
'''


class BusinessTest(myunit.MyTest):
    """ 业务统计页面测试 """

    # 简化-业务统计页面
    def bu(self):
        return businessPage.Business(self.driver)

    # 等待时间-测试用
    @staticmethod
    def waiting_time():
        return sleep(2)
        # return sleep(0)

    def test_business11(self):
        """ 检验展示区名称是否和左侧导航栏名称一致 """
        self.bu().front()
        a = self.bu().business_head_title_text()
        b = self.bu().business_left_navigation_text("1", "1")
        self.waiting_time()
        Function.insert_img(self.driver, "Business_展示区名称与导航栏名称个人储蓄一致.jpg")
        # 校验两个名称是否相等
        self.assertEqual(
            a, b)

    def test_business12(self):
        """ 检验展示区名称个人储蓄是否和首页业务统计名称下个人储蓄一致 """
        self.bu().front()
        a = self.bu().business_head_title_text()
        b = homePage.Home(self.driver).home_business_no1_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_展示区名称与首页业务统计下个人储蓄一致.jpg")
        # 校验两个名称是否相等
        self.assertEqual(
            a, b)

    def test_business21(self):
        """ 关键输入“中国” """
        self.bu().front()
        self.bu().business_search(keyword="中国")
        self.bu().business_time_select_time(2)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_查询关键词中国无数据.jpg")
        else:
            # 校验“中国”是否包含在标题文本中
            self.assertIn(
                "中国", self.bu().business_message_title_text())
            Function.insert_img(self.driver, "Business_查询关键词中国.jpg")

    def test_business311(self):
        """ 时间选择一周 """
        self.bu().bu_keyword()
        day_text = self.bu().business_totalnumber_up_text()
        day_number = Function.re_sub(day_text)
        self.bu().business_time_select_time(1)
        week_text = self.bu().business_totalnumber_up_text()
        week_number = Function.re_sub(week_text)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_查询时间选择一周.jpg")
        # 校验一周的数据量是否大于一天数据量
        self.assertEqual(
            week_number > day_number, True)

    def test_business312(self):
        """ 时间选择一月 """
        self.bu().bu_keyword()
        day_text = self.bu().business_totalnumber_up_text()
        day_number = Function.re_sub(day_text)
        self.bu().business_time_select_time(2)
        month_text = self.bu().business_totalnumber_up_text()
        month_number = Function.re_sub(month_text)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_查询时间选择一月.jpg")
        # 校验一月的数据量是否大于一天数据量
        self.assertEqual(
            month_number > day_number, True)

    def test_business313(self):
        """ 时间选择一天 """
        self.bu().bu_time()
        month_text = self.bu().business_totalnumber_up_text()
        month_number = Function.re_sub(month_text)
        self.bu().business_time_select_time(0)
        day_text = self.bu().business_totalnumber_up_text()
        day_number = Function.re_sub(day_text)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_查询时间选择一天.jpg")
        # 校验一周的数据量是否大于一天数据量
        self.assertEqual(
            month_number > day_number, True)

    def test_business314(self):
        """ 时间选择自定义 """
        self.bu().bu_keyword()
        self.bu().business_time_custom()
        custom_text = self.bu().business_totalnumber_up_text()
        custom_number = Function.re_sub(custom_text)
        self.bu().business_time_select_time(0)
        day_text = self.bu().business_totalnumber_up_text()
        day_number = Function.re_sub(day_text)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_查询时间选择自定义.jpg")
        # 校验自定义3天的数据量是否大于一天数据量
        self.assertEqual(
            custom_number > day_number, True)

    def test_business321(self):
        """ 统计情绪的总数与情绪正、负、中总和数是否一致 """
        self.bu().bu_time()
        self.bu().business_mood_all(1)
        negative = self.bu().business_totalnumber_up_text()
        negative_number = Function.re_sub(negative)
        self.bu().business_mood_all(2)
        neutral = self.bu().business_totalnumber_up_text()
        neutral_number = Function.re_sub(neutral)
        self.bu().business_mood_all(3)
        positive = self.bu().business_totalnumber_up_text()
        positive_number = Function.re_sub(positive)
        self.bu().business_mood_all(0)
        total = self.bu().business_totalnumber_up_text()
        total_number = Function.re_sub(total)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_统计情绪的总数与情绪正、负、中总和数是否一致.jpg")
        # 校验正、负、中的数据量是否等于全部数据量
        self.assertEqual(
            total_number, str(int(negative_number) + int(neutral_number) + int(positive_number)))

    def test_business322(self):
        """ 情绪选择正面 """
        self.bu().bu_time()
        self.bu().business_mood_all(1)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_查询情绪选择正面无数据.jpg")
        else:
            mood = self.bu().business_message_mood()
            # 校验首条信息情绪是否为“情绪倾向：正”
            self.assertEqual(
                mood, "情绪倾向：正")
            Function.insert_img(self.driver, "Business_查询情绪选择正面.jpg")

    def test_business323(self):
        """ 情绪选择中立 """
        self.bu().bu_time()
        self.bu().business_mood_all(2)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_查询情绪选择中立无数据.jpg")
        else:
            mood = self.bu().business_message_mood()
            # 校验首条信息情绪是否为“情绪倾向：中”
            self.assertEqual(
                mood, "情绪倾向：中")
            Function.insert_img(self.driver, "Business_查询情绪选择中立.jpg")

    def test_business324(self):
        """ 情绪选择负面 """
        self.bu().bu_time()
        self.bu().business_mood_all(3)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_查询情绪选择负面无数据.jpg")
        else:
            mood = self.bu().business_message_mood()
            # 校验首条信息情绪是否为“情绪倾向：负”
            self.assertEqual(
                mood, "情绪倾向：负")
            Function.insert_img(self.driver, "Business_查询情绪选择负面.jpg")

    def test_business325(self):
        """ 情绪选择全部 """
        self.bu().bu_time()
        text1 = self.bu().business_totalnumber_up_text()
        self.bu().business_mood_all(1)
        self.bu().business_mood_all(0)
        text2 = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_查询情绪选择全部.jpg")
        # 校验切换前与切换后的数据总量是否一致
        self.assertEqual(
            text1, text2)

    def test_business3311(self):
        """ 来源选择取消全部，弹窗提示是否正确 """
        self.bu().bu_time()
        self.bu().business_source_select(0)
        text = self.bu().business_source_all_error_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_来源选择取消全部弹窗提示文本'.jpg")
        # 校验弹窗提示本文是否为“媒体类型为必选项”
        self.assertEqual(
            text, "媒体类型为必选项")

    def test_business3312(self):
        """ 来源选择取消全部，弹窗确认 """
        self.bu().bu_time()
        self.bu().business_source_select(0)
        self.bu().business_source_all_error_ok()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_来源选择取消全部弹窗确认'.jpg")
        # 校验是否找到排序时间按钮文本
        self.assertTrue(
            self.bu().business_time_text(), "时间")

    def test_business3313(self):
        """ 来源选择取消全部，弹窗关闭 """
        self.bu().bu_time()
        self.bu().business_source_select(0)
        self.bu().business_source_all_error_close()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_来源选择取消全部弹窗关闭'.jpg")
        # 校验是否找到排序时间按钮文本
        self.assertTrue(
            self.bu().business_time_text(), "时间")

    def test_business332(self):
        """ 来源选择新闻 """
        self.bu().bu_time_sourcenull()
        self.bu().business_source_select(1)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_来源选择新闻无数据.jpg")
        else:
            text = self.bu().business_message_source()
            # 校验首条信息文本来源是否为“新闻”
            self.assertEqual(
                text, "新闻")
            Function.insert_img(self.driver, "Business_来源选择新闻.jpg")

    def test_business333(self):
        """ 来源选择论坛 """
        self.bu().bu_time_sourcenull()
        self.bu().business_source_select(2)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_来源选择论坛无数据.jpg")
        else:
            text = self.bu().business_message_source()
            # 校验首条信息文本来源是否为“论坛”
            self.assertEqual(
                text, "论坛")
            Function.insert_img(self.driver, "Business_来源选择论坛.jpg")

    def test_business334(self):
        """ 来源选择博客 """
        self.bu().bu_time_sourcenull()
        self.bu().business_source_select(3)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_来源选择博客无数据.jpg")
        else:
            text = self.bu().business_message_source()
            # 校验首条信息文本来源是否为“论坛”
            self.assertEqual(
                text, "博客")
            Function.insert_img(self.driver, "Business_来源选择博客.jpg")

    def test_business335(self):
        """ 来源选择微博 """
        self.bu().bu_time_sourcenull()
        self.bu().business_source_select(4)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_来源选择微博无数据.jpg")
        else:
            text = self.bu().business_message_source()
            # 校验首条信息文本来源是否为“论坛”
            self.assertEqual(
                text, "微博")
            Function.insert_img(self.driver, "Business_来源选择微博.jpg")

    def test_business336(self):
        """ 来源选择微信 """
        self.bu().bu_time_sourcenull()
        self.bu().business_source_select(5)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_来源选择微信无数据.jpg")
        else:
            text = self.bu().business_message_source()
            # 校验首条信息文本来源是否为“新闻”
            self.assertEqual(
                text, "微信")
            Function.insert_img(self.driver, "Business_来源选择微信.jpg")

    def test_business337(self):
        """ 来源选择平媒 """
        self.bu().bu_time_sourcenull()
        self.bu().business_source_select(6)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_来源选择平媒无数据.jpg")
        else:
            text = self.bu().business_message_source()
            # 校验首条信息文本来源是否为“新闻”
            self.assertEqual(
                text, "平媒")
            Function.insert_img(self.driver, "Business_来源选择平媒.jpg")

    def test_business338(self):
        """ 来源选择APP """
        self.bu().bu_time_sourcenull()
        self.bu().business_source_select(7)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_来源选择APP无数据.jpg")
        else:
            text = self.bu().business_message_source()
            # 校验首条信息文本来源是否为“新闻”
            self.assertEqual(
                text, "APP")
            Function.insert_img(self.driver, "Business_来源选择APP.jpg")

    def test_business339(self):
        """ 来源组合查询(APP+new) """
        self.bu().bu_time_sourcenull()
        self.bu().business_source_select(7)
        number1 = self.bu().business_totalnumber_up_text()
        self.bu().business_source_select(1)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_来源选择APP+NEW无数据.jpg")
        else:
            number2 = self.bu().business_totalnumber_up_text()
            # 校验组合查询的条数是否大于单独APP条数
            self.assertEqual(
                number1 < number2, True)
            Function.insert_img(self.driver, "Business_来源选择APP+NEW.jpg")

    def test_business3310(self):
        """ 来源选择全部 """
        self.bu().front()
        number1 = self.bu().business_totalnumber_up_text()
        self.bu().bu_time_sourcenull()
        self.bu().business_source_select(1)
        self.bu().business_source_select(2)
        self.bu().business_source_select(3)
        self.bu().business_source_select(4)
        self.bu().business_source_select(5)
        self.bu().business_source_select(6)
        self.bu().business_source_select(7)
        number = self.bu().business_totalnumber_up_text()
        self.waiting_time()
        if number == "共0条数据":
            kong = self.bu().business_message_null_text()
            self.assertEqual(kong, "无数据")
            Function.insert_img(self.driver, "Business_来源选择全部无数据.jpg")
        else:
            number2 = self.bu().business_totalnumber_up_text()
            # 校验刚进入时的总条数和筛选的总条数是否一致
            self.assertEqual(
                number1 == number2, True)
            Function.insert_img(self.driver, "Business_来源选择全部.jpg")
    
    def test_business41(self):
        """ 时间正序排序 """
        self.bu().bu_time()
        system_time1 = self.bu().business_message_time()
        self.bu().business_timesort()
        system_time2 = self.bu().business_message_time()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_时间正序排序.jpg")
        # 校验排序前时间是否大于排序后时间
        self.assertEqual(
            system_time1 > system_time2, True)

    def test_business42(self):
        """ 时间倒序排序 """
        self.bu().bu_time()
        self.bu().business_timesort()
        system_time1 = self.bu().business_message_time()
        self.bu().business_timesort()
        system_time2 = self.bu().business_message_time()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_时间倒序排序.jpg")
        # 校验2次点击，排序前时间是否大于排序后时间
        self.assertEqual(
            system_time1 < system_time2, True)

    def test_business511(self):
        """ 单条报告按钮弹框关闭 """
        self.bu().bu_time_messagereport()
        self.bu().business_message_report_closebtn()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条报告按钮弹框关闭.jpg")
        # 校验是否找到排序时间按钮文本
        self.assertEqual(
            self.bu().business_time_text(), "时间")

    def test_business512(self):
        """  输入小于10位的数字、字母、中文组合，选择任意标签，点击添加按钮 """
        self.bu().bu_time_messagereport()
        self.bu().business_message_report_input(text="测试新建报告")
        self.bu().business_message_report_addbtn()
        navigationPage.Navigation(self.driver).na_check('报告厅')
        method.Method(self.driver).js_bottom()
        text = auditoriumPage.Auditorium(self.driver).briefing_title()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_新建简报成功.jpg")
        # 校验在报告厅中是否新建的报告
        self.assertEqual(
            text, "测试新建报告")

    def test_business513(self):
        """  输入框为空，点击添加按钮 """
        self.bu().bu_time_messagereport()
        self.bu().business_message_report_input(text="")
        self.bu().business_message_report_addbtn()
        text = self.bu().business_message_report_fail()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_新建简报输入框为空.jpg")
        # 校验错误提示是否为“*不能为空”
        self.assertEqual(
            text, "*不能为空")
     
    def test_business514(self):
        """  输入空格，点击添加按钮 """
        self.bu().bu_time_messagereport()
        self.bu().business_message_report_input(text=" ")
        self.bu().business_message_report_addbtn()
        text = self.bu().business_message_report_fail()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_新建简报输入框为空格.jpg")
        # 校验错误提示是否为“*不能为空”
        self.assertEqual(
            text, "*不能为空")

    def test_business515(self):
        """  输入框输入大于十位字符，点击添加按钮 """
        self.bu().bu_time_messagereport()
        self.bu().business_message_report_input(text="一二三四为六七八九十一")
        self.bu().business_message_report_addbtn()
        text = self.bu().business_message_report_fail()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_新建简报输入框为大于十位字符.jpg")
        # 校验错误提示是否为“*最多十位”
        self.assertEqual(
            text, "*最多十位")

    def test_business516(self):
        """  输入框输入特殊字符，点击添加按钮 """
        self.bu().bu_time_messagereport()
        self.bu().business_message_report_input(text="！@#")
        self.bu().business_message_report_addbtn()
        text = self.bu().business_message_report_fail()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_新建简报输入框为特殊字符.jpg")
        # 校验错误提示是否为“*格式不对”
        self.assertEqual(
            text, "*格式不对")

    def test_business521(self):
        """ 单条修正按钮弹框关闭 """
        self.bu().bu_time_messageupdate()
        self.bu().business_message_update_close()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条修正按钮弹框关闭.jpg")
        # 校验是否找到排序时间按钮文本
        self.assertEqual(
            self.bu().business_time_text(), "时间")

    def test_business522(self):
        """ 单条修正按钮弹框，状态选择告警，点击确认按钮 """
        self.bu().bu_time_messageupdate()
        self.bu().business_message_update_alarm()
        self.bu().business_message_update_ok()
        text = self.bu().business_message_alarm(1)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条修正按钮弹框状态选择告警.jpg")
        # 校验是否找到首条信息的告警文本标识
        self.assertEqual(
            text, "告警")

    def test_business523(self):
        """ 单条修正按钮弹框，状态选择正常，点击确认按钮 """
        self.bu().bu_time_messageupdate()
        self.bu().business_message_update_normal()
        self.bu().business_message_update_ok()
        text = self.bu().business_message_alarm(1)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条修正按钮弹框状态选择正常.jpg")
        # 校验首条信息的告警文本标识是否为空
        self.assertEqual(
            text, "")

    def test_business524(self):
        """ 单条修正按钮弹框，情绪选择正，点击确认按钮 """
        self.bu().bu_time_messageupdate()
        self.bu().business_message_update_positive()
        self.bu().business_message_update_ok()
        text = self.bu().business_message_mood()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条修正按钮弹框情绪选择正.jpg")
        # 校验是否找到首条信息的情绪倾向为正
        self.assertEqual(
            text, "情绪倾向：正")

    def test_business525(self):
        """ 单条修正按钮弹框，情绪选择负，点击确认按钮 """
        self.bu().bu_time_messageupdate()
        self.bu().business_message_update_negative()
        self.bu().business_message_update_ok()
        text = self.bu().business_message_mood()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条修正按钮弹框情绪选择负.jpg")
        # 校验是否找到首条信息的情绪倾向为正
        self.assertEqual(
            text, "情绪倾向：负")

    def test_business526(self):
        """ 单条修正按钮弹框，情绪选择中，点击确认按钮 """
        self.bu().bu_time_messageupdate()
        self.bu().business_message_update_neutral()
        self.bu().business_message_update_ok()
        text = self.bu().business_message_mood()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条修正按钮弹框情绪选择中.jpg")
        # 校验是否找到首条信息的情绪倾向为中
        self.assertEqual(
            text, "情绪倾向：中")

    def test_business53(self):
        """ 单条数据导出 """
        Function.del_file()
        self.bu().business_time_select_time(2)
        text_page = self.bu().business_message_title_text()
        above = self.bu().business_message_mood_chains()
        ActionChains(self.driver).move_to_element(above).perform()
        self.bu().business_message_export()
        text_down = Function.read_excel(0, 3)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条数据导出校验.jpg")
        # 校验下载文件的标题和网页显示的表示是否一致
        self.assertEqual(
            text_page, text_down)
        Function.del_file()

    def test_business541(self):
        """ 单条数据收藏，点击收藏按钮后是否变为取消收藏 """
        self.bu().bu_time()
        chains = self.bu().business_message_mood_chains()
        ActionChains(self.driver).move_to_element(chains).perform()
        collect_text = self.bu().business_message_collect_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条数据收藏后按钮变为取消收藏.jpg")
        if collect_text == "收藏":
            self.bu().business_message_collect()
            text = self.bu().business_message_collect_text()
            # 校验是否找到首条信息的情绪倾向为中
            self.assertEqual(
                text, "取消收藏")
        elif collect_text == "取消收藏":
            self.bu().business_message_collect()
            text = self.bu().business_message_collect_text()
            # 校验是否找到首条信息的情绪倾向为中
            self.assertEqual(
                text, "收藏")

    def test_business542(self):
        """ 单条数据收藏，查看收藏关注中是否有此条信息 """
        self.bu().front()
        self.bu().business_time_select_time(2)
        text1 = self.bu().business_message_title_text()
        chains = self.bu().business_message_mood_chains()
        ActionChains(self.driver).move_to_element(chains).perform()
        collect_text = self.bu().business_message_collect_text()
        if collect_text == "取消收藏":
            self.bu().business_message_collect()
        self.bu().business_message_collect()
        navigationPage.Navigation(self.driver).na_personal_check('收藏关注')
        text2 = pca.Pca(self.driver).collection_title_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_单条数据收藏后查看收藏关注中是否有此条信息.jpg")
        # 校验是否找到首条信息的情绪倾向为中
        self.assertEqual(
            text1, text2)

    def test_business561(self):
        """ 点击标题后查看和原文标题是否一致 """
        self.bu().front()
        text1 = self.bu().business_message_title_text()
        self.bu().business_message_title()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        text2 = self.driver.title
        self.waiting_time()
        Function.insert_img(self.driver, "Business_系统标题和原文标题是否一致.jpg")
        # 校验系统和原文标题是否一致”
        self.assertEqual(
            text1 in text2, True)

    def test_business562(self):
        """ 点击摘要后查看和原文标题是否一致 """
        self.bu().front()
        text1 = self.bu().business_message_title_text()
        self.bu().business_message_title()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        text2 = self.driver.title
        self.waiting_time()
        Function.insert_img(self.driver, "Business_系统摘要跳转后和原文标题是否一致.jpg")
        # 校验系统摘要跳转后和原文标题是否一致”
        self.assertEqual(
            text1 in text2, True)

    def test_business6211(self):
        """ 不同类型时修正，弹出提示信息 """
        self.bu().front()
        self.bu().bu_mood_differ()
        text = self.bu().business_pagefoot_update_error_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_不同类型时修正弹框提示.jpg")
        # 校验类型不一致时弹出提示信息是否为“至少选择一条”
        self.assertEqual(
            text, "至少选择一条")

    def test_business6212(self):
        """ 不同类型时修正，弹出提示关闭 """
        self.bu().front()
        self.bu().bu_mood_differ()
        self.bu().business_pagefoot_update_error_close()
        text = self.bu().business_page_nextpage_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_不同类型时修正弹框关闭.jpg")
        # 校验类型不一致时弹出关闭后是否显示有“下一页”文本
        self.assertEqual(
            text, "下一页")

    def test_business6213(self):
        """ 不同类型时修正，弹出提示确定 """
        self.bu().front()
        self.bu().bu_mood_differ()
        self.bu().business_pagefoot_update_error_button()
        text = self.bu().business_page_nextpage_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_不同类型时修正弹框确定.jpg")
        # 校验类型不一致时弹出关闭后是否显示有“下一页”文本
        self.assertEqual(
            text, "下一页")

    def test_business6221(self):
        """ 同类型时修正，弹出提示关闭按钮 """
        self.bu().front()
        self.bu().bu_mood_equally()
        self.bu().business_message_update_close()
        text = self.bu().business_page_nextpage_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_同类型时修正弹框确定.jpg")
        # 校验类型一致时弹出关闭后是否显示有“下一页”文本
        self.assertEqual(
            text, "下一页")

    # def test_business6222(self):
    #     """ 同类型时修正，弹出修改状态为告警 """
    #     self.bu().front()
    #     self.bu().bu_mood_equally()
    #     self.bu().business_message_update_alarm()
    #     self.bu().business_message_update_ok()
    #     text1 = self.bu().business_message_alarm(14)
    #     text2 = self.bu().business_message_alarm(15)
    #     # 校验第14条信息和第15条信息的情绪是否一致为告警
    #     self.assertEqual(
    #         text1, text2)
    #     Function.insert_img(self.driver, "Business_同类型时修正状态为告警.jpg")
    #     self.bu().business_pagefoot_update()
    #     self.bu().business_message_update_normal()
    #     self.bu().business_message_update_ok()

    def test_business63(self):
        """ 第一页全部数据导出 """
        Function.del_file()
        self.bu().business_time_select_time(2)
        text_page = self.bu().business_message_title_text()
        method.Method(self.driver).js_bottom()
        self.bu().business_pagefoot_all()
        self.bu().business_pagefoot_export()
        text_down = Function.read_excel(0, 3)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_第一页全部数据导出校验.jpg")
        # 校验下载文件的标题和网页显示的标题是否一致
        self.assertEqual(
            text_page, text_down)
        Function.del_file()

    def test_business64(self):
        """ 第一页全部数据收藏 """
        loginPage.Login(self.driver).user_login_front()
        navigationPage.Navigation(self.driver).na_personal_check('收藏关注')
        positive = pca.Pca(self.driver).collection_number_all()
        number = Function.re_sub(positive)
        self.bu().business_time_select_time(2)
        method.Method(self.driver).js_bottom()
        self.bu().business_pagefoot_all()
        self.bu().business_pagefoot_collect()
        navigationPage.Navigation(self.driver).na_personal_check('收藏关注')
        positive = pca.Pca(self.driver).collection_number_all()
        number_new = Function.re_sub(positive)
        self.waiting_time()
        Function.insert_img(self.driver, "Business_第一页全部数据收藏校验.jpg")
        # 校验原收藏数量加上收藏数量是否收藏后总量
        self.assertEqual(
            number_new, number + 15)

    def test_business71(self):
        """ 顶部与底部的页码总条数是否一致 """
        self.bu().front()
        num1 = self.bu().business_totalnumber_up_text()
        method.Method(self.driver).js_bottom()
        num2 = self.bu().business_totalnumber_down_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_顶部与底部的页码总条数一致校验.jpg")
        # 校验页面顶部与底部的页码总条数是否一致
        self.assertEqual(
            num1, num2)

    def test_business72(self):
        """ 点击第二页页码跳转 """
        self.bu().front()
        method.Method(self.driver).js_bottom()
        self.bu().business_page_number2()
        method.Method(self.driver).js_bottom()
        text = self.bu().business_page_previouspage_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_点击第二页页码跳转校验.jpg")
        # 校验是否出现上一页页码
        self.assertEqual(
            text, "上一页")

    def test_business73(self):
        """ 上一页页码跳转 """
        self.bu().front()
        method.Method(self.driver).js_bottom()
        self.bu().business_page_number2()
        method.Method(self.driver).js_bottom()
        self.bu().business_page_previouspage()
        text = self.bu().business_page_previouspage_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_上一页页码跳转校验.jpg")
        # 校验是否上一页页码是否为空
        self.assertEqual(
            text, "")

    def test_business74(self):
        """ 下一页页码跳转 """
        self.bu().front()
        method.Method(self.driver).js_bottom()
        self.bu().business_page_nextpage()
        text = self.bu().business_page_previouspage_text()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_下一页页码跳转校验.jpg")
        # 校验是否出现上一页页码
        self.assertEqual(
            text, "上一页")

    def test_business8(self):
        """ 页面回到首页 """
        self.bu().front()
        method.Method(self.driver).js_bottom()
        method.Method(self.driver).back_homepage()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_回到首页.jpg")
        # 校验页面数据中是否出现“告警信息”文字
        self.assertEqual(
            homePage.Home(self.driver).home_alarm_text(), "告警信息")

    def test_business9(self):
        """ 页面回到顶部 """
        self.bu().front()
        method.Method(self.driver).js_bottom()
        method.Method(self.driver).back_top()
        self.waiting_time()
        Function.insert_img(self.driver, "Business_回到顶部.jpg")
        # 校验是否找到个人中心是否存在
        self.assertEqual(
            method.Method(self.driver).personal(), True)

if __name__ == '__main__':
    unittest.main()
