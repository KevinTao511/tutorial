# -*- coding: utf-8 -*-

# @FileName :singleton.py
# @Time     :2/4/21 3:22 PM
# @Author   :Kevin Tao
# Copyright (c) all rights reserved.


class Singleton(object):
    """单例模式"""
    __instance = None
    __isInit = False

    def __new__(cls, name):
        if not cls.__instance:
            Singleton.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isInit:
            self.__name = name
            Singleton.__isInit = True

    def getName(self):
        return self.__name


if __name__ == '__main__':
    test = Singleton("Kevin")
    print(test.getName())
