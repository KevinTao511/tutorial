# -*- coding: utf-8 -*-

# @FileName :observer.py
# @Time     :2/13/21 9:45 PM
# @Author   :Kevin Tao
# Copyright (c) all rights reserved.

from __future__ import annotations
from typing import List


class Observer:
    def update(self, subject: Subject):
        pass


class Subject(object):
    def __init__(self):
        self.__observers: List[Observer] = []

    def addObserver(self, observer: Observer):
        if observer not in self.__observers:
            self.__observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.__observers.remove(observer)

    def notifyObservers(self):
        for observer in self.__observers:
            observer.update(self)


class WaterHeater(Subject):
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        self.notifyObservers()


class WashingModel(Observer):
    def update(self, subject: WaterHeater):
        if 50 <= subject.getTemperature() <= 65:
            print("当前温度可用于洗澡。")


class DrinkingModel(Observer):
    def update(self, subject: WaterHeater):
        if subject.getTemperature() >= 90:
            print("当前温度可用于饮用。")


if __name__ == '__main__':
    waterHeater = WaterHeater()
    washingModel = WashingModel()
    drinkingModel = DrinkingModel()
    waterHeater.addObserver(washingModel)
    waterHeater.addObserver(drinkingModel)
    waterHeater.setTemperature(90)
    waterHeater.setTemperature(60)
