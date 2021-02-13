# -*- coding: utf-8 -*-

# @FileName :adapter.py
# @Time     :2/5/21 3:57 PM
# @Author   :Kevin Tao
# Copyright (c) all rights reserved.


class SocketEntity:
    """插座接口类型定义"""

    def __init__(self, numOfPin, typeOfPin):
        self.__numOfPin = numOfPin
        self.__typeOfPin = typeOfPin

    def getNumOfPin(self):
        return self.__numOfPin

    def setNumOfPin(self, numOfPin):
        self.__numOfPin = numOfPin

    def getTypeOfPin(self):
        return self.__typeOfPin

    def setTypeOfPin(self, typeOfPin):
        self.__typeOfPin = typeOfPin


class ChineseSocket:
    """国内插座"""

    def getName(self):
        return "国内插座"

    def getSocket(self):
        return SocketEntity(3, "八字扁型")


class BritishSocket:
    """英国查表"""

    def getName(self):
        return "英国插座"

    def getSocket(self):
        return SocketEntity(3, "T字方型")


class AdapterSocket:
    """适配器模式"""

    def __init__(self, britishSocket):
        self.__britishSocket = britishSocket

    def getName(self):
        return self.__britishSocket.getName() + "转换器"

    def getSocket(self):
        socket = self.__britishSocket.getSocket()
        socket.setTypeOfPin("八字扁型")
        return socket


if __name__ == '__main__':
   britishSocket = BritishSocket()
   adapterSocket = AdapterSocket(britishSocket)
   print(adapterSocket.getName())
   print(adapterSocket.getSocket().getTypeOfPin())