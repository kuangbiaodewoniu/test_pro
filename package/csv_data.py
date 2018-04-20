# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: csv_data.py 
@time: 2018/04/20 
"""
import csv


def get_user_info(file_name):
    with open(file_name, encoding='utf-8') as f:
        result = {}
        values = {}
        user_infos = csv.reader(f)
        for value in user_infos:
            values['username'] = value[1]
            values['password'] = value[2]
            result[value[0]] = values
        return result


if __name__ == '__main__':
    file_name = r'F:\study\python\test_pro\fanli\data\user_login_info.csv'
    r = get_user_info(file_name)
    print(r)
