import math

class Node:
    def __init__(self, index = None, data = None):
        self.__index = index
        self.__data = data
        self.__next = None
        self.__prev = None
        self.__left = None
        self.__right = None
        self.__up = None
        self.__down = None
        self.__bL = None
        self.__bR = None
        self.__uL = None
        self.__uR = None

    def getIndex(self):
        return self.__index

    def setIndex(self, index):
        self.__index = index

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getNext(self):
        return self.__next

    def setNext(self, link):
        self.__next = link 

    def getPrev(self):
        return self.__prev

    def setPrev(self, link):
        self.__prev = link

    def getLeft(self):
        return self.__left

    def setLeft(self, link):
        self.__left = link

    def getRight(self):
        return self.__right

    def setRight(self, link):
        self.__right = link

    def getUp(self):
        return self.__up

    def setUp(self, link):
        self.__up = link

    def getDown(self):
        return self.__down

    def setDown(self, link):
        self.__down = link

    def getbL(self):
        return self.__bL

    def setbL(self, link):
        self.__bL = link

    def getbR(self):
        return self.__bR

    def setbR(self, link):
        self.__bR = link

    def getuL(self):
        return self.__uL

    def setuL(self, link):
        self.__uL = link

    def getuR(self):
        return self.__uR

    def setuR(self, link):
        self.__uR = link
