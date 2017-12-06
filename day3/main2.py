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

def main():
    num = int(input("Enter a number: "))
    myGraph = Graph()
    myGraph.append(1)
    i = 2
    while myGraph.getLast().getData() < num:
        myGraph.append(i)
        i += 1
    print(myGraph.getLast().getData())

main()