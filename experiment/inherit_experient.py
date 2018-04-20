# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: inherit_experient.py
@time: 2018/04/20 
"""


class A:
    def __init__(self):
        print('In A')
        super(A, self).__init__()
        print('Out A')


# 缺点：当继承类改变时，类中所有引用都需要改变
class B:
    def __init__(self):
        print('In B')
        super(B, self).__init__()
        print('Out B')


class C(A):
    def __init__(self):
        print('In C')
        super(C, self).__init__()
        print('Out C')


class D(A):
    def __init__(self):
        print('In D')
        super(D, self).__init__()
        print('Out D')


class E(B, C):
    def __init__(self):
        print('In E')
        super(E, self).__init__()
        print('Out E')


class F(E, D):
    def __init__(self):
        print('In F')
        super(F, self).__init__()
        print('Out F')


if __name__ == '__main__':
    # IN F
        # IN E
            # IN B
            # OUT B
            # IN C
                # IN A
                # OUT A
            # OUT C
        # OUT E
        # IN D
            # IN A
            # OUT A
        # OUT D
    # OUT F
    F()