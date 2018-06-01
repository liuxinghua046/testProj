from test_case.models import myunit
from test_case.models.function import Function
from test_case.page import peAccountPwdPage, loginPage, method
import unittest

'''
@ name: 个人中心-账号密码页面测试用例
@ test：1.修改密码校验：
          1.01 旧密码输入为空，其他项6-12位数字字母_，点击保存；
          1.02 旧密码输入为空格，其他项6-12位数字字母_，点击保存；
          1.03 旧密码输入小于6位，其他项6-12位数字字母_，点击保存；
          1.04 旧密码输入大于12位，其他项6-12位数字字母_，点击保存；
          1.05 旧密码输入非6-12位数字字母_，其他项6-12位数字字母_，点击保存；
          1.06 新密码输入为空，其他项6-12位数字字母_，点击保存；
          1.07 新密码输入为空格，其他项6-12位数字字母_，点击保存；
          1.08 新密码输入小于6位，其他项6-12位数字字母_，点击保存；
          1.09 新密码输入大于12位，其他项6-12位数字字母_，点击保存；
          1.10 新密码输入非6-12位数字字母_，其他项6-12位数字字母_，点击保存；
          1.11 确认密码输入为空，其他项6-12位数字字母_，点击保存；
          1.12 确认密码输入为空格，其他项6-12位数字字母_，点击保存；
          1.13 确认密码输入小于6位，其他项6-12位数字字母_，点击保存；
          1.14 确认密码输入大于12位，其他项6-12位数字字母_，点击保存；
          1.15 确认密码输入非6-12位数字字母_，其他项6-12位数字字母_，点击保存；
          1.16 单独点击保存按钮；
          1.17 新密码和确认输入密码6-12位数字字母_，但是内容不一致，点击保存；
          1.18 旧密码输入正确，新密码和确认密码输入6-12位数字字母_，且相等，点击保存。
        2.个人信息校验：
          2.01 真实姓名输入为空，其他项不做修改，点击保存；
          2.02 真实姓名输入为空格，其他项不做修改，点击保存；
          2.03 真实姓名输入小于2位，其他项不做修改，点击保存；
          2.04 真实姓名输入大于20位，其他项不做修改，点击保存；
          2.05 真实姓名输入非数字，字母，汉字，并在2-20之间，其他项不做修改，点击保存；
          2.06 微信号输入为空，其他项不做修改，点击保存；
          2.07 微信号输入为空格，其他项不做修改，点击保存；
          2.08 微信号输入小于6位，其他项不做修改，点击保存；
          2.09 微信号输入大于20位，其他项不做修改，点击保存；
          2.10 微信号输入非首字母加数字，并在6-20之间，其他项不做修改，点击保存；
          2.11 邮箱输入为空，其他项不做修改，点击保存；
          2.12 邮箱输入为空格，其他项不做修改，点击保存；
          2.13 邮箱输入非x@x.x格式，其他项不做修改，点击保存；
          2.14 手机号输入为空，其他项不做修改，点击保存；
          2.15 手机号输入为空格，其他项不做修改，点击保存；
          2.16 手机号输入小于11位，其他项不做修改，点击保存；
          2.17 手机号输入大于11位，其他项不做修改，点击保存；
          2.18 手机号输入非数字11位，其他项不做修改，点击保存；
          2.19 直接点击保存按钮；
          2.20 输入正确的真实姓名、微信号、邮箱、手机，点击保存。
        3.回到首页；
        4.回到顶部。
'''


class PeAccountPwdTest(myunit.MyTest):
    """ 个人中心账号密码测试 """

    # 简化-账号密码页面
    def pap(self):
        return peAccountPwdPage.PersonalAccountPwd(self.driver)

    def test_PeAccountPwd101(self):
        """ 旧密码输入为空，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('', '123456', '123456')
        text = self.pap().password_old_error_text()
        # 校验错误提示是否为“旧密码不能为空”
        self.assertEqual(
            text, "旧密码不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_旧密码输入为空.jpg")

    def test_PeAccountPwd102(self):
        """ 旧密码输入为空格，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified(' ', '123456', '123456')
        text = self.pap().password_old_error_text()
        # 校验错误提示是否为“旧密码不能为空”
        self.assertEqual(
            text, "旧密码不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_旧密码输入为空格.jpg")

    def test_PeAccountPwd103(self):
        """ 旧密码输入小于6位，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123', '123456', '123456')
        text = self.pap().password_old_error_text()
        # 校验错误提示是否为“密码必须是由 6-12位字母数字_ 组合”
        self.assertEqual(
            text, "密码必须是由 6-12位字母数字_ 组合")
        Function.insert_img(self.driver, "PeAccountPwd_旧密码输入小于6位.jpg")

    def test_PeAccountPwd104(self):
        """ 旧密码输入大于12位，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('1234567890123', '123456', '123456')
        text = self.pap().password_old_error_text()
        # 校验错误提示是否为“密码必须是由 6-12位字母数字_ 组合”
        self.assertEqual(
            text, "密码必须是由 6-12位字母数字_ 组合")
        Function.insert_img(self.driver, "PeAccountPwd_旧密码输入小于6位.jpg")

    def test_PeAccountPwd105(self):
        """ 旧密码输入非6-12位数字字母_，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123￥#@#￥', '123456', '123456')
        text = self.pap().password_old_error_text()
        # 校验错误提示是否为“密码必须是由 6-12位字母数字_ 组合”
        self.assertEqual(
            text, "密码必须是由 6-12位字母数字_ 组合")
        Function.insert_img(self.driver, "PeAccountPwd_旧密码输入非6-12位数字字母_.jpg")

    def test_PeAccountPwd106(self):
        """ 新密码输入为空，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', '', '123456')
        text = self.pap().password_new_error_text()
        # 校验错误提示是否为“新密码不能为空”
        self.assertEqual(
            text, "新密码不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_新密码输入为空.jpg")

    def test_PeAccountPwd107(self):
        """ 新密码输入为空格，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', ' ', '123456')
        text = self.pap().password_new_error_text()
        # 校验错误提示是否为“新密码不能为空”
        self.assertEqual(
            text, "新密码不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_新密码输入为空格.jpg")

    def test_PeAccountPwd108(self):
        """ 新密码输入小于6位，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', '123', '123456')
        text = self.pap().password_new_error_text()
        # 校验错误提示是否为“密码必须是由 6-12位字母数字_ 组合”
        self.assertEqual(
            text, "密码必须是由 6-12位字母数字_ 组合")
        Function.insert_img(self.driver, "PeAccountPwd_新密码输入小于6位.jpg")

    def test_PeAccountPwd109(self):
        """ 新密码输入大于12位，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', '1234567890123', '123456')
        text = self.pap().password_new_error_text()
        # 校验错误提示是否为“密码必须是由 6-12位字母数字_ 组合”
        self.assertEqual(
            text, "密码必须是由 6-12位字母数字_ 组合")
        Function.insert_img(self.driver, "PeAccountPwd_新密码输入大于12位.jpg")

    def test_PeAccountPwd110(self):
        """ 新密码输入非6-12位数字字母_，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', '123aa$@#%', '123456')
        text = self.pap().password_new_error_text()
        # 校验错误提示是否为“密码必须是由 6-12位字母数字_ 组合”
        self.assertEqual(
            text, "密码必须是由 6-12位字母数字_ 组合")
        Function.insert_img(self.driver, "PeAccountPwd_新密码输入非6-12位数字字母_.jpg")

    def test_PeAccountPwd111(self):
        """ 确认密码输入为空，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', '123456', '')
        text = self.pap().password_confirm_error_text()
        # 校验错误提示是否为“确认密码不能为空”
        self.assertEqual(
            text, "确认密码不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_确认密码输入为空.jpg")

    def test_PeAccountPwd112(self):
        """ 确认密码输入为空格，其他项6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', '123456', ' ')
        text = self.pap().password_confirm_error_text()
        # 校验错误提示是否为“确认密码不能为空”
        self.assertEqual(
            text, "确认密码不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_确认密码输入为空格.jpg")

    def test_PeAccountPwd113(self):
        """ 确认密码输入小于6位，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', '123456', '123')
        text = self.pap().password_confirm_error_text()
        # 校验错误提示是否为“与新密码不一致,请重新输入”
        self.assertEqual(
            text, "与新密码不一致,请重新输入")
        Function.insert_img(self.driver, "PeAccountPwd_确认密码输入小于6位.jpg")

    def test_PeAccountPwd114(self):
        """ 确认密码输入大于12位，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', '123456', '1234567890123')
        text = self.pap().password_confirm_error_text()
        # 校验错误提示是否为“与新密码不一致,请重新输入”
        self.assertEqual(
            text, "与新密码不一致,请重新输入")
        Function.insert_img(self.driver, "PeAccountPwd_确认密码输入大于12位.jpg")

    def test_PeAccountPwd115(self):
        """ 确认密码输入非6-12位数字字母_，点击保存 """
        self.pap().front()
        self.pap().password_unified('123456', '123456', '123fd#@')
        text = self.pap().password_confirm_error_text()
        # 校验错误提示是否为“与新密码不一致,请重新输入”
        self.assertEqual(
            text, "与新密码不一致,请重新输入")
        Function.insert_img(self.driver, "PeAccountPwd_确认密码输入非6-12位数字字母_.jpg")

    def test_PeAccountPwd116(self):
        """ 直接点击保存 """
        self.pap().front()
        self.pap().password_button()
        self.pap().error_button()
        text1 = self.pap().password_old_error_text()
        # 校验错误提示是否为“新密码不能为空”
        self.assertEqual(
            text1, "旧密码不能为空")
        text2 = self.pap().password_new_error_text()
        # 校验错误提示是否为“新密码不能为空”
        self.assertEqual(
            text2, "新密码不能为空")
        text3 = self.pap().password_confirm_error_text()
        # 校验错误提示是否为“确认密码不能为空”
        self.assertEqual(
            text3, "确认密码不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_修改密码直接点击保存.jpg")

    def test_PeAccountPwd117(self):
        """ 新密码和确认输入密码6-12位数字字母_，但是内容不一致 """
        self.pap().front()
        self.pap().password_unified('123456', '123456789', '123456987')
        text = self.pap().password_confirm_error_text()
        # 校验错误提示是否为“与新密码不一致,请重新输入”
        self.assertEqual(
            text, "与新密码不一致,请重新输入")
        Function.insert_img(self.driver, "PeAccountPwd_新密码和确认密码不一致.jpg")

    def test_PeAccountPwd118(self):
        """ 旧密码输入正确，新密码和确认密码输入6-12位数字字母_，且相等 """
        self.pap().front()
        self.pap().password_unified('123456', '123456', '123456')
        text = loginPage.Login(self.driver).login_notice_text()
        # 校验错误提示是否为“尊敬的客户：”
        self.assertEqual(
            text, "尊敬的客户：")
        Function.insert_img(self.driver, "PeAccountPwd_修改密码全部输入正确.jpg")

    def test_PeAccountPwd201(self):
        """ 真实姓名输入为空，其他项不做修改，点击保存 """
        text = self.pap().account_unified_name('')
        # 校验错误提示是否为“姓名不能为空”
        self.assertEqual(
            text, "姓名不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_真实姓名输入为空.jpg")

    def test_PeAccountPwd202(self):
        """ 真实姓名输入为空格，其他项不做修改，点击保存 """
        text = self.pap().account_unified_name(' ')
        # 校验错误提示是否为“姓名不能为空”
        self.assertEqual(
            text, "姓名不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_真实姓名输入为空格.jpg")

    def test_PeAccountPwd203(self):
        """ 真实姓名输入为小于2位，其他项不做修改，点击保存 """
        text = self.pap().account_unified_name('1')
        # 校验错误提示是否为“必须由2-20位数字，字母，汉字组成”
        self.assertEqual(
            text, "必须由2-20位数字，字母，汉字组成")
        Function.insert_img(self.driver, "PeAccountPwd_真实姓名输入为小于2位.jpg")

    def test_PeAccountPwd204(self):
        """ 真实姓名输入为大于20位，其他项不做修改，点击保存 """
        text = self.pap().account_unified_name('123456789012345678901')
        # 校验错误提示是否为“必须由2-20位数字，字母，汉字组成”
        self.assertEqual(
            text, "必须由2-20位数字，字母，汉字组成")
        Function.insert_img(self.driver, "PeAccountPwd_真实姓名输入为大于20位.jpg")

    def test_PeAccountPwd205(self):
        """ 真实姓名输入非数字，字母，汉字，并在2-20之间，其他项不做修改，点击保存 """
        text = self.pap().account_unified_name('！@#￥')
        # 校验错误提示是否为“必须由2-20位数字，字母，汉字组成”
        self.assertEqual(
            text, "必须由2-20位数字，字母，汉字组成")
        Function.insert_img(self.driver, "PeAccountPwd_真实姓名输入非数字字母汉字.jpg")

    def test_PeAccountPwd206(self):
        """ 微信号输入为空，其他项不做修改，点击保存 """
        text = self.pap().account_unified_wexin('')
        # 校验错误提示是否为“微信不能为空”
        self.assertEqual(
            text, "微信不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_微信号输入为空.jpg")

    def test_PeAccountPwd207(self):
        """ 微信号输入为空格，其他项不做修改，点击保存 """
        text = self.pap().account_unified_wexin(' ')
        # 校验错误提示是否为“微信不能为空”
        self.assertEqual(
            text, "微信不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_微信号输入为空格.jpg")

    def test_PeAccountPwd208(self):
        """ 微信号输入为小于6位，其他项不做修改，点击保存 """
        text = self.pap().account_unified_wexin('1222')
        # 校验错误提示是否为“微信格式不正确”
        self.assertEqual(
            text, "微信格式不正确")
        Function.insert_img(self.driver, "PeAccountPwd_微信号输入为小于6位.jpg")

    def test_PeAccountPwd209(self):
        """ 微信号输入为大于20位，其他项不做修改，点击保存 """
        text = self.pap().account_unified_wexin('asd123asd123asd123123')
        # 校验错误提示是否为“微信格式不正确”
        self.assertEqual(
            text, "微信格式不正确")
        Function.insert_img(self.driver, "PeAccountPwd_微信号输入为大于20位.jpg")

    def test_PeAccountPwd210(self):
        """ 微信号输入非首位字母加数字，并在6-20之间，其他项不做修改，点击保存 """
        text = self.pap().account_unified_wexin('123aaasss')
        # 校验错误提示是否为“微信格式不正确”
        self.assertEqual(
            text, "微信格式不正确")
        Function.insert_img(self.driver, "PeAccountPwd_微信号输入非首位字母加数字.jpg")

    def test_PeAccountPwd211(self):
        """ 邮箱输入为空，其他项不做修改，点击保存 """
        text = self.pap().account_unified_email('')
        # 校验错误提示是否为“邮箱不能为空”
        self.assertEqual(
            text, "邮箱不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_邮箱输入为空.jpg")

    def test_PeAccountPwd212(self):
        """ 邮箱输入为空格，其他项不做修改，点击保存 """
        text = self.pap().account_unified_email(' ')
        # 校验错误提示是否为“邮箱不能为空”
        self.assertEqual(
            text, "邮箱不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_邮箱输入为空格.jpg")

    def test_PeAccountPwd213(self):
        """ 邮箱输入非x@x.x格式，其他项不做修改，点击保存 """
        text = self.pap().account_unified_email('ss@ss')
        # 校验错误提示是否为“邮箱格式不正确”
        self.assertEqual(
            text, "邮箱格式不正确")
        Function.insert_img(self.driver, "PeAccountPwd_邮箱输入非正确格式.jpg")

    def test_PeAccountPwd214(self):
        """ 手机号输入为空，其他项不做修改，点击保存 """
        text = self.pap().account_unified_phone('')
        # 校验错误提示是否为“手机号不能为空”
        self.assertEqual(
            text, "手机号不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_手机号输入为空.jpg")

    def test_PeAccountPwd215(self):
        """ 手机号输入为空格，其他项不做修改，点击保存 """
        text = self.pap().account_unified_phone(' ')
        # 校验错误提示是否为“手机号不能为空”
        self.assertEqual(
            text, "手机号不能为空")
        Function.insert_img(self.driver, "PeAccountPwd_手机号输入为空格.jpg")

    def test_PeAccountPwd216(self):
        """ 手机号输入为小于11位，其他项不做修改，点击保存 """
        text = self.pap().account_unified_phone('1352122')
        # 校验错误提示是否为“手机号格式不正确”
        self.assertEqual(
            text, "手机号格式不正确")
        Function.insert_img(self.driver, "PeAccountPwd_手机号输入为小于11位.jpg")

    def test_PeAccountPwd217(self):
        """ 手机号输入为大于11位，其他项不做修改，点击保存 """
        text = self.pap().account_unified_phone('13518729872')
        # 校验错误提示是否为“手机号格式不正确”
        self.assertEqual(
            text, "手机号格式不正确")
        Function.insert_img(self.driver, "PeAccountPwd_手机号输入为大于11位.jpg")

    def test_PeAccountPwd218(self):
        """ 手机号输入为非数字11位，其他项不做修改，点击保存 """
        text = self.pap().account_unified_phone('wisiwiewdiri')
        # 校验错误提示是否为“手机号格式不正确”
        self.assertEqual(
            text, "手机号格式不正确")
        Function.insert_img(self.driver, "PeAccountPwd_手机号输入为非数字11位.jpg")

    def test_PeAccountPwd219(self):
        """ 个人信息，直接点击保存 """
        self.pap().front()
        self.pap().account_button()
        text = self.pap().account_success_text()
        # 校验提示是否为“保存成功”
        self.assertEqual(
            text, "保存成功")
        Function.insert_img(self.driver, "PeAccountPwd_个人信息直接点击保存.jpg")

    def test_PeAccountPwd220(self):
        """ 输入正确的真实姓名、微信号、邮箱、手机，点击保存 """
        text = self.pap().account_unified('纪明朋', 'EraPose', 'jimingpeng@wiseweb.com.cn', '17777786550')
        # 校验提示是否为“保存成功”
        self.assertEqual(
            text, "保存成功")
        Function.insert_img(self.driver, "PeAccountPwd_个人信息输入正确.jpg")

    def test_PeAccountPwd3(self):
        """ 账号密码页面，回到首页 """
        self.pap().front()
        method.Method(self.driver).js_bottom()
        method.Method(self.driver).back_homepage()
        # 校验页面数据中是否出现“告警信息”文字
        self.assertEqual(
            method.Method(self.driver).home_text(), "告警信息")
        Function.insert_img(self.driver, "PeAccountPwd_回到首页.jpg")

    def test_PeAccountPwd4(self):
        """ 账号密码页面，回到顶部 """
        self.pap().front()
        method.Method(self.driver).js_bottom()
        method.Method(self.driver).back_top()
        # 校验是否找到个人中心是否存在
        self.assertEqual(
            method.Method(self.driver).personal(), True)
        Function.insert_img(self.driver, "PeAccountPwd_回到顶部.jpg")

if __name__ == '__main__':
    unittest.main()
