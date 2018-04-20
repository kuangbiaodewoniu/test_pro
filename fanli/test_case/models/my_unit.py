# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: my_unit.py 
@time: 2018/04/20 
"""
import unittest
from .driver import browser


class MyUnit(unittest.TestCase):

    def setUp(self):
        self.driver = browser()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
