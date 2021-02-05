# -*- coding: utf-8 -*-

# @FileName :decorator.py
# @Time     :2/4/21 3:53 PM
# @Author   :Kevin Tao
# Copyright (c) all rights reserved.


class Person:
    """装饰器模式"""

    def __init__(self, name):
        self.__name = name

    def wear(self):
        print("Wearing...")


class Engineer(Person):
    """工程师"""

    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def getSkill(self):
        return self.__skill

    def wear(self):
        super().wear()


class ClothingDecorator(Engineer):
    """工程师服装装饰器"""

    def __init__(self, engineer):
        self.__decorator = engineer

    def wear(self):
        self.__decorator.wear()
        self.decorate()

    def decorate(self):
        print("decorating...")


class ShoesDecorator(Engineer):
    """工程师鞋子装饰器"""

    def __init__(self, engineer):
        self.__decorator = engineer

    def wear(self):
        self.__decorator.wear()
        self.decorate()

    def decorate(self):
        print("engineer decorating...")


if __name__ == '__main__':
   person = Person("Kevin")
   cloth = ClothingDecorator(person)
   shoes = ShoesDecorator(cloth)
   shoes.wear()

