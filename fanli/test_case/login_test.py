# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: login_test.py 
@time: 2018/04/20 
"""
import sys
sys.path.append('./models')
sys.path.append('./page_obj')

from models import my_unit
from page_obj import login_page
import unittest
from time import sleep


class LoginTest(my_unit.MyUnit):

    def login_util(self, username='username', password='password'):
        login_page.LoginPage(self.driver).user_login(username, password)

    # 用户名密码正确
    def test_correct_login(self):
        self.login_util()
        sleep(2)
        target_url = 'https://passport.fanli.com/center/welcome'
        self.assertEqual(self.driver.current_url, target_url, '未登录成功')


if __name__ == '__main__':
    unittest.main()

