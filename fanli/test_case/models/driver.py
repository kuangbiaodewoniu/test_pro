# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: driver.py 
@time: 2018/04/20
@function: 定义驱动
"""
from selenium import webdriver


def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


if __name__ == '__main__':
    driver = browser()
    url = 'http://www.fanli.com/'
    driver.get(url)
    driver.quit()