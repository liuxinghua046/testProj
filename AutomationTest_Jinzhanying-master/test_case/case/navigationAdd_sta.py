from test_case.models import myunit
from test_case.models.function import Function
from test_case.page import navigationAddPage
import unittest

'''
@ name: 新增导航页面测试用例
@ test：1.导航设置中新增按钮校验.
        2.导航名称输入框校验:
            2.1 输入小于10位的数字、字母、中文组合，选择任意标签，点击添加按钮；
            2.2 输入框为空，不选择标签，点击添加按钮；
            2.3 输入框为空，选择标签，点击添加按钮；
            2.4 输入空格，选择任意标签，点击添加按钮；
            2.5 输入框输入大于十位字符，选择任意标签，点击添加按钮；
            2.6 输入框输入特殊字符，选择任意标签，点击添加按钮。
        3.删除导航菜单校验：
            3.1 选择最后一个导航进行删除，弹框后选择否；
            3.2 选择最后一个导航进行删除，弹框后选择是。
'''


class NavigationTest(myunit.MyTest):
    """ 新增导航页面测试 """

    def na_add(self):
        """简化-新增导航页面"""
        return navigationAddPage.NavigationAdd(self.driver)

    def test_navigationAdd1(self):
        """ 导航设置中新增按钮 “+” 校验 """
        self.na_add().na_navigation_add()
        self.na_add().navigation_add_add()
        Function.insert_img(self.driver, "NavigationAdd_导航设置加号点击成功.jpg")
        # 校验导航名称输入框是否为空
        self.assertEqual(
            self.na_add().navigation_add_name_text(), "")

    def test_navigationAdd21(self):
        """ 输入小于10位的数字、字母、中文组合，选择任意标签，点击添加按钮 """
        self.na_add().na_navigation_add_newnavigation_operation("测试导航")
        self.na_add().na_navigation_add_text_label_btn(name="测试导航")
        self.na_add().navigation_add_button_button()
        Function.insert_img(self.driver, "NavigationAdd_添加导航成功.jpg")
        # 校验导航名称是否为“测试导航”
        self.assertEqual(
            self.na_add().na_navigation_add_newnavigation_if("测试导航"), True)

    def test_navigationAdd22(self):
        """ 输入框为空，不选择标签，点击添加按钮 """
        self.na_add().na_navigation_add()
        self.na_add().navigation_add_js()
        self.na_add().navigation_add_button()
        Function.insert_img(self.driver, "NavigationAdd_输入框为空无标签.jpg")
        # 校验错误弹框文本是否为“请选择至少一个标签”
        self.assertEqual(
            self.na_add().navigation_add_null_text(), "请选择至少一个标签")

    def test_navigationAdd23(self):
        """ 输入框为空，选择标签，点击添加按钮 """
        self.na_add().na_navigation_add_text_label_btn(name="")
        Function.insert_img(self.driver, "NavigationAdd_输入空有标签.jpg")
        # 校验弹框文本错误提示是否为“*导航名称不能重复”
        self.assertEqual(
            self.na_add().navigation_add_fail_text(), "*导航名称不能重复")

    def test_navigationAdd24(self):
        """ 输入空格，选择标签，点击添加按钮 """
        self.na_add().na_navigation_add_text_label_btn(name=" ")
        Function.insert_img(self.driver, "NavigationAdd_输入空格有标签.jpg")
        # 校验弹框文本错误提示是否为“*导航名称不能为空”
        self.assertEqual(
            self.na_add().navigation_add_fail_text(), "*导航名称不能为空")

    def test_navigationAdd25(self):
        """ 输入框输入大于十位字符，选择任意标签，点击添加按钮 """
        self.na_add().na_navigation_add_text_label_btn(name="测试导航长度测试导航长度")
        Function.insert_img(self.driver, "NavigationAdd_长度大于十位有标签.jpg")
        # 校验弹框文本错误提示是否为“*导航名称不能超过十个字符”
        self.assertEqual(
            self.na_add().navigation_add_fail_text(), "*导航名称不能超过十个字符")

    def test_navigationAdd26(self):
        """ 输入框输入特殊字符，选择任意标签，点击添加按钮 """
        self.na_add().na_navigation_add_text_label_btn(name="！@#")
        Function.insert_img(self.driver, "NavigationAdd_输入特殊字符有标签.jpg")
        # 校验弹框文本错误提示是否为“*导航名称不能含有特殊字符”
        self.assertEqual(
            self.na_add().navigation_add_fail_text(), "*导航名称不能含有特殊字符")

    def test_navigationDel31(self):
        """ 选择测试导航进行删除，弹框后选择否 """
        self.na_add().na_navigation_add_newnavigation_operation("测试导航")
        self.na_add().navigation_add_navigation_del_button_no()
        Function.insert_img(self.driver, "NavigationAdd_导航删除选否.jpg")
        # 校验导航名称是否存在为“测试导航，存在”
        self.assertEqual(
            self.na_add().na_navigation_add_newnavigation_if("测试导航"), True)

    def test_navigationDel32(self):
        """ 选择测试导航进行删除，弹框后选择是 """
        self.na_add().na_navigation_add_newnavigation_operation("测试导航")
        self.na_add().navigation_add_navigation_del_button_yes()
        Function.insert_img(self.driver, "NavigationAdd_导航成功删除.jpg")
        # 校验导航名称是否存在为“测试导航，不存在”
        self.assertFalse(
            self.na_add().na_navigation_add_newnavigation_if("测试导航"), False)

if __name__ == '__main__':
    unittest.main()
