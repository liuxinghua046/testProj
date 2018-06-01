from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os


# ======= 定义发送邮件 =========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    '''
    smtp.connect("smtp.126.com")
    smtp.login("j131421@126.com", "xxxxxxxxx")
    smtp.sendmail("j131421@126.com", "312911698@qq.com", msg.as_string())
    '''
    smtp.connect("pop.exmail.qq.com")
    smtp.login("jimingpeng@wiseweb.com.cn", "xxxxxxxx")
    smtp.sendmail("jimingpeng@wiseweb.com.cn", "312911698@qq.com", msg.as_string())
    smtp.quit()
    print("email has send out!")


# ======= 查找测试报告目录，找到最新生成的测试报告文件 =========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print("生成报告位置名称：", file_new)
    return file_new

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = 'report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='金战鹰舆情自动化测试报告',
                            description='环境：windows 7 浏览器：chrome')
    discover = unittest.defaultTestLoader.discover('test_case/case/',
                                                   # pattern='*_sta.py')
                                                   pattern='login_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('report/')  # 查找新生成的报告
    print("发送邮件")
    # send_mail(file_path)
