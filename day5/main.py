from linkedlist import LinkedList

def traverse(nodePtr):
    while nodePtr != None:
        print(nodePtr.getData())
        nodePtr = nodePtr.getNext()

def traverseBack(nodePtr):
    while nodePtr != None:
        print(nodePtr.getData())
        nodePtr = nodePtr.getPrev()

def part1():
    instructions = open('input.txt', 'r')

    linkedList = LinkedList()
    for each in instructions:
        linkedList.append(int(each))

    steps = 0
    nodePtr = linkedList.getFront()
    while nodePtr != None:
        steps += 1
        if nodePtr.getData() >= 0:
            offset = nodePtr.getData()
            nodePtr.setData(offset + 1)
            for i in range(offset):
                nodePtr = nodePtr.getNext()
                if nodePtr == None:
                    break
        else:
            offset = nodePtr.getData()
            nodePtr.setData(offset + 1)
            for i in range(abs(offset)):
                nodePtr = nodePtr.getPrev()
                if nodePtr == None:
                    break
    print(steps)

def part2():
    instructions = open('input.txt', 'r')

    linkedList = LinkedList()
    for each in instructions:
        linkedList.append(int(each))

    steps = 0 
    nodePtr = linkedList.getFront()
    while nodePtr != None:   
        steps += 1
        if nodePtr.getData() >= 0:
            offset = nodePtr.getData()
            if offset >= 3:
                nodePtr.setData(offset - 1)
            else:
                nodePtr.setData(offset + 1)
            for i in range(offset):
                nodePtr = nodePtr.getNext()
                if nodePtr == None:
                    break
        else:
            offset = nodePtr.getData() 
            nodePtr.setData(offset + 1) 
            for i in range(abs(offset)):
                nodePtr = nodePtr.getPrev()
                if nodePtr == None:
                    break
    print(steps)

def dev():
    myList = LinkedList()
    for num in range(5):
        myList.append(num)

    traverse(myList.getFront())

part2()
