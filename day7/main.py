from node import Node

def checkWeight(nodePtr):
    if not nodePtr.isTopTower():
        first = True
        for node in nodePtr.getSubTowerLinks():
            if first:
                weight = node.getWeight()
                first = False
                continue
            if node.getWeight() != weight:
                return nodePtr

        for node in nodePtr.getSubTowerLinks():
            return checkWeight(node)

def getTrueWeight(nodePtr):
    if nodePtr.isTopTower():
        return nodePtr.getWeight()
    else:
        trueWeight = nodePtr.getWeight()
        for node in nodePtr.getSubTowerLinks():
            trueWeight += getTrueWeight(node)

        return trueWeight

def test():
    node1 = Node('a', 0, ['b', 'b', 'b'])
    node2 = Node('b', 3, ['c', 'c', 'c'])
    node3 = Node('c', 2, ['d', 'd', 'd'])
    node4 = Node('d', 1)

    for i in range(3):
        node3.setSubTowerLink(node4)

    for i in range(3):
        node2.setSubTowerLink(node3)

    for i in range(3):
        node1.setSubTowerLink(node2)

    print(getTrueWeight(node1))

def checkWeight2(nodePtr):
    if not nodePtr.isTopTower():
        for node in nodePtr.getSubTowerLinks():
            if node.getWeight() != getTrueWeight(node):
                return node.getName()

    return 'none'

def main():
    tower = open('input.txt', 'r')
    '''
    length = 0
    for program in tower:
        list1 = program.split()
        weight = int(list1[1].lstrip('(').rstrip(')'))
        if len(list1) > length:
            length = len(list1)
            bottom = list1

    print(bottom)
    '''

    nodeList = []
    nameList = []
    for program in tower:
        list1 = program.split()
        name = list1[0]
        weight = int(list1[1].lstrip('(').rstrip(')'))
        subTowerNames = []
        if len(list1) > 2:
            for i in range(3, len(list1)):
                subTowerNames.append(list1[i].rstrip(','))

        newNode  = Node(name, weight, subTowerNames)
        nodeList.append(newNode)
        nameList.append(name)

    for node in nodeList:
        if not node.isTopTower():
            for name in node.getSubTowerNames():
                index = nameList.index(name)
                node.setSubTowerLink(nodeList[index])
                nodeList[index].setLinked()

    for node in nodeList:
        if not node.isTopTower():
            if not node.isLinked():
                print(node.getName())
                bottomNode = node

    '''
    nodePtr = bottomNode
    found = False
    while not found:
        if not node.isTopTower():
            first = True
            for node in nodePtr.getSubTowerLinks():
                if first:
                    weight = node.getWeight()
                    first = False
                    continue
                if node.getWeight() != weight:
                    found = True
                    unbalancedTower = nodePtr
                    break
    '''
    # unbalancedTower = checkWeight2(bottomNode)
    # print(unbalancedTower)
    # print(bottomNode.getWeight())
    # print(getTrueWeight(bottomNode))
    for node1 in bottomNode.getSubTowerLinks():
        for node2 in node1.getSubTowerLinks():
            if getTrueWeight(node2) == 15378:
                for node3 in node2.getSubTowerLinks():
                    if getTrueWeight(node3) == 1060:
                        print(node3.getWeight() - 9)
    '''
    for program in unbalancedTower.getSubTowerLinks():
        print(program.getWeight())
    '''

    tower.close()

def dev():
    list1 = [1, 2, 3]
    print(list1.index(2))

main()

# azqje -> holcy, fwbang, inwmb
