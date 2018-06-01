import re
import xlrd
import os
import time


class Function:

    @staticmethod
    def insert_img(driver, file_name):
        """截图"""
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        base_dir = base_dir.replace('\\', '/')
        base = base_dir.split('/test_case')[0]
        now = time.strftime("%m-%d %H-%M")
        file_path = base + "/report/image/" + now + "_" + file_name
        driver.get_screenshot_as_file(file_path)
        # pass

    @staticmethod
    def del_file():
        """删除系统下载文件夹下所有文件"""
        path = r'C:\Users\admin\Downloads'
        for i in os.listdir(path):
            path_file = os.path.join(path, i)
            if os.path.isfile(path_file):
                os.remove(path_file)

    @staticmethod
    def read_excel(col, row):
        """读取系统下载文件夹下Excel文件"""
        path = r'C:\Users\admin\Downloads'
        path_dir = os.listdir(path)
        # 打开文件
        excel = xlrd.open_workbook(path + "\\" + path_dir[0])
        # 获取第一个sheet
        first_sheet = excel.sheet_by_index(0)
        # 获取第几列第几行的数据
        return first_sheet.col(col)[row].value

    # # 读取系统下载文件夹下Word文件
    # @staticmethod
    # def read_word():
    #     path = r'C:\Users\admin\Downloads'
    #     path_dir = str(os.listdir(path))
    #     print(path_dir)
    #     # 打开文件
    #     word = docx.Document(path + "\\" + path_dir[0])
    #     print(word)
    #     for i in range(len(word.paragraphs)):
    #         return print("第" + str(i) + "段的内容是：" + word.paragraphs[i].text)
    #     # 获取第几列第几行的数据

    @staticmethod
    def re_sub(num):
        """总页数-字符串截取整数部分"""
        return re.sub(r'\D', "", num)

if __name__ == '__main__':

    # 测试截图
    # driver = webdriver.Chrome()
    # driver.get("http://www.baidu.com")
    # Function().insert_img(driver, 'baidu.png')
    # driver.quit()

    # 测试删除文件
    # Function().del_file()
    # 测试读取Excel文件
    print(Function().read_excel(1, 3))

    # 测试读取word文件
    # Function().read_word()
