class Node:
    def __init__(self, name = None, weight = None, subTowerNames = []):
        self.__name = name
        self.__weight = weight
        self.__subTowerNames = subTowerNames
        self.__subTowerLinks = []
        self.__linked = False

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        self.__weight = weight

    def getSubTowerNames(self):
        return self.__subTowerNames

    def setSubTowerNames(self, names):
        self.__subTowerNames = names

    def getSubTowerLinks(self):
        return self.__subTowerLinks

    def setSubTowerLink(self, link):
        self.__subTowerLinks.append(link)

    def isTopTower(self):
        return len(self.__subTowerNames) == 0

    def setLinked(self):
        self.__linked = True

    def isLinked(self):
        return self.__linked

