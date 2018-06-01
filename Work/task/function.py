#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import time
from selenium import webdriver


class Function:

    @staticmethod
    def insert_img(driver,file_name):
        """截图"""
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        base_dir = base_dir.replace('\\', '/')
        base = base_dir.split('/task')[0]
        now = time.strftime("%y-%m-%d %H-%M-%S")
        file_path = base + "/report/image/" + now + "_" + file_name
        # file_path = base + "/report/image/"+ file_name
        driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':

    # 截图
    driver = webdriver.Chrome()
    driver.get("http://192.168.20.12:56366/rdms/login.jsp")
    Function.insert_img(driver, 'login111.png')
    driver.quit()

