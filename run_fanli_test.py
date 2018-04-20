# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: run_fanli_test.py 
@time: 2018/04/20 
"""
import time, sys
sys.path.append('./packgae')
from package import HTMLTestRunner
import unittest
# from mail_fixture.qq_mail import MailInit


# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './fanli/test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
# sender = '625642751@qq.com'
# receiver = 'dandan.zheng@fanli.com'


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './fanli/report/' + now + '_result.html'
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Fanli UI Test Report', description='xxx')
    runner.run(discover)
    fp.close()

    # # 发送测试邮件
    # mail = MailInit(sender, receiver, filename)
    # mail.send_mail()