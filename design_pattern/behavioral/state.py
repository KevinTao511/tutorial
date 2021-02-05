# -*- coding: utf-8 -*-

# @FileName :state.py
# @Time     :2/4/21 5:10 PM
# @Author   :Kevin Tao
# Copyright (c) all rights reserved.


class State:
    """状态模式"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name
