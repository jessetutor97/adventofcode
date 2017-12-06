from linkedlist import LinkedList

# Takes a LinkedList object and returns a python list
def getConfig(linkedList):
    list1 = []
    nodePtr = linkedList.getFront()
    for i in range(linkedList.getSize()):
        list1.append(nodePtr.getData())
        nodePtr = nodePtr.getLink()

    return list1

def main():
    banks = open('input.txt', 'r')
    myList = banks.readline().split()
    banks.close()

    # Linked list is a circular linked list
    linkedList = LinkedList()
    for each in myList:
        linkedList.append(int(each))

    # configList is a two-dimensional list that stores each configuration state
    configList = []
    found = False
    steps = 0
    while not found:
        steps += 1
        configList.append(getConfig(linkedList))
        maxBlocks = 0
        maxBank = None
        nodePtr = linkedList.getFront()
        for i in range(linkedList.getSize()):
            if nodePtr.getData() > maxBlocks:
                maxBlocks = nodePtr.getData()
                maxBank = nodePtr
            nodePtr = nodePtr.getLink()

        maxBank.setData(0)
        nodePtr = maxBank
        for i in range(maxBlocks):
            nodePtr = nodePtr.getLink()
            nodePtr.setData(nodePtr.getData() + 1)

        if getConfig(linkedList) in configList:
            found = True

    print(steps)

    state = getConfig(linkedList)
    found = False
    steps = 0
    while not found:
        steps += 1
        maxBlocks = 0
        maxBank = None
        nodePtr = linkedList.getFront()
        for i in range(linkedList.getSize()):
            if nodePtr.getData() > maxBlocks:
                maxBlocks = nodePtr.getData()
                maxBank = nodePtr
            nodePtr = nodePtr.getLink()

        maxBank.setData(0)
        nodePtr = maxBank
        for i in range(maxBlocks):
            nodePtr = nodePtr.getLink()
            nodePtr.setData(nodePtr.getData() + 1)

        if getConfig(linkedList) == state:
            found = True

    print(steps)

main()
