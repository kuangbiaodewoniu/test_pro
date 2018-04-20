# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: page_base.py
@time: 2018/04/20 
"""


class Page(object):

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        self.timeout = 30

    def open(self):
        self.driver.get(self.url)

    def find_element(self, *by_key):
        return self.driver.find_element(*by_key)

    def find_elements(self, *by_key):
        return self.driver.find_elements(*by_key)