import math
from node import Node

class Graph:
    def __init__(self):
        self.__port = None
        self.__last = None
        self.__size = 0

    def getPort(self):
        return self.__port

    def getLast(self):
        return self.__last

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

    def __getSum(self):
        total = 0
        if self.__last.getLeft() != None:
            total += self.__last.getLeft().getData()
        if self.__last.getRight() != None:
            total += self.__last.getRight().getData()
        if self.__last.getUp() != None:
            total += self.__last.getUp().getData()
        if self.__last.getDown() != None:
            total += self.__last.getDown().getData()
        if self.__last.getuL() != None:
            total += self.__last.getuL().getData()
        if self.__last.getuR() != None:
            total += self.__last.getuR().getData()
        if self.__last.getbL() != None:
            total += self.__last.getbL().getData()
        if self.__last.getbR() != None:
            total += self.__last.getbR().getData()

        self.__last.setData(total)

    def getLayer(self):
        return math.ceil(math.sqrt(self.__last.getIndex())) // 2

    def append(self, index):
        if self.isEmpty():
            newNode = Node(index, 1)
            self.__port = newNode
            self.__last = newNode
            self.__size += 1
            return

        newNode = Node(index)
        self.__last.setNext(newNode)
        newNode.setPrev(self.__last)

        layer = math.ceil(math.sqrt(index)) // 2
        width = layer * 2

        i = 2
        count = 1
        char = ''
        if layer == 0:
            char = 'r'
        for num in range(layer):
            char = 'r'
            count += 1
            if count >= index:
                break
            char = 'u'
            count += i - 1
            if count >= index:
                break
            char = 'l'
            count += i
            if count >= index:
                break
            char = 'd'
            count += i
            if count >= index:
                break
            char = 'r'
            count += i
            if count >= index:
                break
            i += 2 

        if char == 'r':
            self.__last.setRight(newNode)
            newNode.setLeft(self.__last)
        elif char == 'u':
            self.__last.setUp(newNode)
            newNode.setDown(self.__last)
        elif char == 'l':
            self.__last.setLeft(newNode)
            newNode.setRight(self.__last)
        elif char == 'd':
            self.__last.setDown(newNode)
            newNode.setUp(self.__last)

        if layer == 0:
            self.__last = newNode
            self.__size += 1
            return

        layer1list = [1, 2, 3, 2, 3, 2, 4, 3, 2]
        if layer == 1:
            adj = layer1list[self.__size - 1]

        i = 4
        count = 9
        for num in range(layer - 1):
            adj = 2
            count += 1
            if count >= index:
                break
            adj = 4
            count += i - 3
            if count >= index:
                break
            adj = 3
            count += 1
            if count >= index:
                break
            adj = 2
            count += 1
            if count >= index:
                break
            adj = 4
            count += i - 2
            if count >= index:
                break
            adj = 3
            count += 1
            if count >= index:
                break
            adj = 2
            count += 1
            if count >= index:
                break
            adj = 4
            count += i - 2
            if count >= index:
                break
            adj = 3
            count += 1
            if count >= index:
                break
            adj = 2
            count += 1
            if count >= index:
                break
            adj = 4
            count += i - 1
            if count >= index:
                break
            adj = 3
            count += 1
            if count >= index:
                break
            i += 2

        if char == 'u' and adj == 2:
            newNode.setbL(self.__last.getLeft())
        elif char == 'u' and adj == 3:
            newNode.setbL(self.__last.getLeft())
            newNode.setLeft(newNode.getbL().getUp())
        elif char == 'u' and adj == 4:
            newNode.setbL(self.__last.getLeft())
            newNode.setLeft(newNode.getbL().getUp())
            newNode.setuL(newNode.getLeft().getUp())
        elif char == 'l' and adj == 2:
            newNode.setbR(self.__last.getDown())
        elif char == 'l' and adj == 3:
            newNode.setbR(self.__last.getDown())
            newNode.setDown(newNode.getbR().getLeft())
        elif char == 'l' and adj == 4:
            newNode.setbR(self.__last.getDown())
            newNode.setDown(newNode.getbR().getLeft())
            newNode.setbL(newNode.getDown().getLeft())
        elif char == 'd' and adj == 2:
            newNode.setuR(self.__last.getRight())
        elif char == 'd' and adj == 3:
            newNode.setuR(self.__last.getRight())
            newNode.setRight(newNode.getuR().getDown())
        elif char == 'd' and adj == 4:
            newNode.setuR(self.__last.getRight())
            newNode.setRight(newNode.getuR().getDown())
            newNode.setbR(newNode.getRight().getDown())
        elif char == 'r' and adj == 2:
            newNode.setuL(self.__last.getUp())
        elif char == 'r' and adj == 3:
            newNode.setuL(self.__last.getUp())
            newNode.setUp(newNode.getuL().getRight())
        elif char == 'r' and adj == 4:
            newNode.setuL(self.__last.getUp())
            newNode.setUp(newNode.getuL().getRight())
            newNode.setuR(newNode.getUp().getRight())

        self.__last = newNode
        self.__size += 1
        self.__getSum()
