# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: login_page.py 
@time: 2018/04/20 
"""
from .page_base import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):

    def __init__(self, driver):
        self.url = 'https://passport.fanli.com/login?spm=passport_login.pc.https'
        Page.__init__(self, self.url, driver)
    username_by_key = (By.ID, 'username')
    password_by_key = (By.ID, 'psw')
    verify_code_by_key = (By.ID, 'passcode')
    btn_login_by_key = (By.ID, 'btn-login')

    # 输入用户名
    def input_username(self, username):
        self.find_element(*self.username_by_key).send_keys(username)

    # 输入密码
    def input_password(self, password):
        self.find_element(*self.password_by_key).send_keys(password)

    # 输入验证码
    def input_verify_code(self, code):
        self.find_element(*self.verify_code_by_key).send_keys(code)

    # 点击登陆
    def click_btn_login(self):
        self.find_element(*self.btn_login_by_key).click()

    # 登录
    def user_login(self, username, password, code='a'):
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.input_verify_code(code)
        self.click_btn_login()


if __name__ == '__main__':
    pass