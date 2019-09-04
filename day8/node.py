class Node:
    def __init__(self, name):
        self.__name = name
        self.__value = 0
        self.__inc = False

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def setInc(self, op):
        if op == 'inc':
            self.__inc = True
        elif op == 'dec':
            self.__inc = False

    def getValue(self):
        return self.__value

    def setValue(self, value):
        if self.__inc:
            self.__value += value
        else:
            self.__value -= value
