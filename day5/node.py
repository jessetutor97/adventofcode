class Node:
    def __init__(self, data = None, link = None):
        self.__data = data
        self.__next = link 
        self.__prev = None

    def setData(self, data):
        self.__data = data

    def getData(self):
        return self.__data

    def setNext(self, link):
        self.__next = link

    def getNext(self):
        return self.__next

    def setPrev(self, link):
        self.__prev = link

    def getPrev(self):
        return self.__prev
