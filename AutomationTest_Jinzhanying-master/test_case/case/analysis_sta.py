from test_case.models.function import Function
from test_case.models import myunit
from test_case.page import analysisPage
import unittest
from time import sleep

'''
@ name: 专题分析测试用例
@ test：1.专题分析页面：
          1.1 关键词查询条件：
            1.1.1 关键词输入框为空，点击查询。
            1.1.2 关键词输入框为空格，点击查询。
            1.1.3 关键词输入框为数字（如：111），点击查询。
            1.1.4 关键词输入框为字母（如：wee），点击查询。
            1.1.5 关键词输入框为特殊字符（如：#￥%），点击查询。
            1.1.6 关键词输入框为超长字符（如：#￥%1213314），点击查询。
            1.1.7 关键词输入框为汉字（如：火灾），点击查询。
          1.2 时间筛选：
            1.2.1 选择一周；
            1.2.2 选择一月；
            1.2.3 选择一天；
            1.2.4 选择自定义。
          1.3 业务筛选：
            1.3.1 筛选全部；
            1.3.2 筛选存在；
            1.3.3 筛选不存在。
          1.4 排序：
            1.4.1 生成时间排序；
            1.4.2 开始时间排序；
            1.4.3 结束时间排序；
            1.4.4 信息数排序。
        2.生成专题页面：
        3.态势分析页面：
        
'''


class AnalysisTest(myunit.MyTest):
    """ 登录测试 """

    # 简化-业务统计页面
    def an(self):
        return analysisPage.Analysis(self.driver)

    def test_analysis11(self):
        """ 检验展示区名称个人储蓄是否和左侧导航栏名称个人储蓄一致 """
        self.an().front()
        self.an().analysis_screen_time(0)
        sleep(10)
        # # 校验两个名称是否相等
        # self.assertEqual(
        #     a, b)
        # Function.insert_img(self.driver, "Business_展示区名称与导航栏名称个人储蓄一致.jpg")

if __name__ == '__main__':
    unittest.main()
