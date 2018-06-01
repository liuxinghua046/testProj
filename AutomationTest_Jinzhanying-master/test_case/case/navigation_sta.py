from test_case.models import myunit
from test_case.models.function import Function
from test_case.page import navigationPage, loginPage
import unittest

'''
@ name: 导航菜单测试用例
@ test：1.分别校验导航：
          1.1 点击LOGO图标；
          1.2 点击首页；
          1.3 点击信息监控；
          1.4 点击告警预测；
          1.5 点击报告厅；
          1.6 点击业务统计；
          1.7 点击专题分析；
          1.8 点击自定义。
        2.个人中心内容：
          2.1 点击账号密码；
          2.2 点击告警提醒；     # 页面功能已去掉
          2.3 点击收藏关注；
          2.4 点击客服帮助；
          2.5 点击我的套餐；
          2.6 点击退出系统。
'''


class NavigationTest(myunit.MyTest):
    """ 导航菜单测试 """

    # 简化-导航部分
    def na(self):
        return navigationPage.Navigation(self.driver)

    def test_navigation11(self):
        """ 点击LOGO图标 """
        self.na().login_front()
        self.na().navigation_logo()
        Function.insert_img(self.driver, "Navigation_切换到LOGO图标.jpg")
        # 校验页面数据中是否出现“告警信息”文字
        self.assertEqual(
            self.na().navigation_logo_text(), "告警信息")

    # ====================================================================================
    # 实现方式：对系统固定的六个导航和自定义导航，分显示和隐藏进行校验，导航排序和不同账号使用无影响
    # ====================================================================================

    def test_navigation12(self):
        """ 点击导航首页 """
        self.na().login_front()
        self.na().na_check('首页')
        Function.insert_img(self.driver, "Navigation_切换到首页.jpg")
        # 校验页面数据中是否出现“告警信息”文字
        self.assertEqual(
            self.na().navigation_home_text(), "告警信息")

    def test_navigation13(self):
        """ 点击信息监控 """
        self.na().login_front()
        self.na().na_check('信息监控')
        Function.insert_img(self.driver, "Navigation_切换到信息监控.jpg")
        # 校验页面数据中是否出现“+添加标签”文字
        self.assertEqual(
            self.na().navigation_monitor_text(), "+添加标签")

    def test_navigation14(self):
        """ 点击导航告警预测 """
        self.na().login_front()
        self.na().na_check('告警预测')
        Function.insert_img(self.driver, "Navigation_切换到告警预测.jpg")
        # 校验页面数据中是否出现“告警提醒设置”文字
        self.assertEqual(
            self.na().navigation_alarm_text(), "告警提醒设置")

    def test_navigation15(self):
        """ 点击导航报告厅 """
        self.na().login_front()
        self.na().na_check('报告厅')
        Function.insert_img(self.driver, "Navigation_切换到报告厅.jpg")
        # 校验页面数据中是否出现“设置报告模板”文字
        self.assertEqual(
            self.na().navigation_auditorium_text(), "设置报告模板")

    def test_navigation16(self):
        """ 点击导航业务统计 """
        self.na().login_front()
        self.na().na_check('业务统计')
        Function.insert_img(self.driver, "Navigation_切换到业务统计.jpg")
        # 校验页面数据中是否出现“时间”文字
        self.assertEqual(
            self.na().navigation_business_text(), "时间")

    def test_navigation17(self):
        """ 点击导航专题分析 """
        self.na().login_front()
        self.na().na_check('专题分析')
        Function.insert_img(self.driver, "Navigation_切换到专题分析.jpg")
        # 校验页面数据中是否出现“生成专题”文字
        self.assertEqual(
            self.na().navigation_analysis_text(), "生成专题")

    def test_navigation18(self):
        """ 点击自定义导航 """
        self.na().login_front()
        custom = self.na().na_custom()[0]
        self.na().na_check(custom)
        Function.insert_img(self.driver, "Navigation_切换到自定义.jpg")
        # 校验页面数据中是否出现“自定义”文字
        self.assertEqual(
            self.na().navigation_custom_text(), custom)

    def test_navigation21(self):
        """ 点击个人中心账号密码 """
        self.na().na_personal()
        self.na().na_personal_check("账号密码")
        Function.insert_img(self.driver, "Navigation_切换到账号密码.jpg")
        # 校验页面数据中是否出现“修改密码”文字
        self.assertEqual(
            self.na().navigation_personal_accountpwd_text(), "修改密码")

    # def test_navigation22(self):
    #     """ 点击个人中心告警提醒 """
    #     self.na().na_personal()
    #     self.na().na_personal_check("告警预测")
    #     Function.insert_img(self.driver, "Navigation_切换到告警预测.jpg")
    #     # 校验页面数据中是否出现“邮件通知”文字
    #     self.assertEqual(
    #         self.na().navigation_personal_alarmreminding_text(), "邮件通知")

    def test_navigation23(self):
        """ 点击个人中心收藏关注 """
        self.na().na_personal()
        self.na().na_personal_check("收藏关注")
        Function.insert_img(self.driver, "Navigation_切换到收藏关注.jpg")
        # 校验页面数据中是否出现“收藏时间”文字
        self.assertEqual(
            self.na().navigation_personal_collectionattention_text(), "收藏时间")

    def test_navigation24(self):
        """ 点击个人中心客服帮助 """
        self.na().na_personal()
        self.na().na_personal_check("客服帮助")
        Function.insert_img(self.driver, "Navigation_切换到客服帮助.jpg")
        # 校验页面数据中是否出现“向网智天元反馈问题”文字
        self.assertEqual(
            self.na().navigation_personal_customerservice_text(), "向网智天元反馈问题")

    def test_navigation25(self):
        """ 点击个人中心我的套餐 """
        self.na().na_personal()
        self.na().na_personal_check("我的套餐")
        Function.insert_img(self.driver, "Navigation_切换到我的套餐.jpg")
        # 校验页面数据中是否出现“当前套餐内容”文字
        self.assertEqual(
            self.na().navigation_personal_mymeal_text(), "当前套餐内容")

    def test_navigation26(self):
        """ 点击个人中心退出系统 """
        self.na().na_personal()
        self.na().na_personal_check("退  出")
        Function.insert_img(self.driver, "Navigation_退出系统.jpg")
        # 校验页面数据中是否出现“尊敬的客户：”文字
        self.assertEqual(
            loginPage.Login(self.driver).login_notice_text(), "尊敬的客户：")

if __name__ == '__main__':
    unittest.main()
