class Node:
    def __init__(self, data = None, link = None):
        self.__data = data
        self.__link = link

    def setData(self, data):
        self.__data = data

    def getData(self):
        return self.__data

    def setLink(self, link):
        self.__link = link

    def getLink(self):
        return self.__link

