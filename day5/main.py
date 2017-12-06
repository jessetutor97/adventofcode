from linkedlist import LinkedList

def part1():
    instructions = open('input.txt', 'r')

    # Linked list is a doubly linked list
    linkedList = LinkedList()
    for each in instructions:
        linkedList.append(int(each))
    instructions.close()

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
    instructions.close()

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

part1()
part2()
