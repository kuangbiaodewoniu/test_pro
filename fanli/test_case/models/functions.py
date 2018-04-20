# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: functions.py 
@time: 2018/04/20 
"""
from .driver import browser


def capture_image(driver, file_name):
    driver.get_screenshot_as_file(file_name)


if __name__ == '__main__':
    driver = browser()
    driver.get('http://www.fanli.com/')
    capture_image(driver, '首页.png')
    driver.quit()

