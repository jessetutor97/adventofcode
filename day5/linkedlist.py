from node import Node

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def isEmpty(self):
        return self.__head == None

    def append(self, data):
        if self.isEmpty():
            temp = Node(data)
            self.__head = temp
            self.__tail = temp
        else:
            temp = Node(data)
            self.__tail.setNext(temp)
            temp.setPrev(self.__tail)
            self.__tail = temp
        self.__size += 1

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def getSize(self):
        return self.__size

    def getFront(self):
        return self.__head

    def getBack(self):
        return self.__tail
