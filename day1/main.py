from linkedlist import LinkedList

def part1():
    myFile = open('input.txt', 'r')
    line1 = myFile.readline().rstrip('\n')
    myFile.close()

    first = True
    total = 0
    for each in line1:
        if first:
            previous = each
            first = False
            continue
        if previous == each:
            total += int(previous)
        previous = each
    
    if previous == line1[0]:
        total += int(previous)

    print(total)

def part1_revised():
    myFile = open('input.txt', 'r')
    line1 = myFile.readline().rstrip('\n')
    myFile.close()

    myList = LinkedList()
    for each in line1:
        myList.append(int(each))

    nodePtr = myList.getFront()
    total = 0
    for num in range(myList.getSize()):
        if nodePtr.getData() == nodePtr.getLink().getData():
            total += nodePtr.getData()
        nodePtr = nodePtr.getLink()

    print(total)

def getOffset(start, offset):
    nodePtr = start
    for num in range(offset):
        nodePtr = nodePtr.getLink()

    return nodePtr.getData()

def part2():
    myFile = open('input.txt', 'r')
    line1 = myFile.readline().rstrip('\n')
    myFile.close()

    myList = LinkedList()
    for each in line1:
        myList.append(int(each))

    nodePtr = myList.getFront()
    total = 0
    offset = myList.getSize() // 2
    for num in range(myList.getSize()):
        if nodePtr.getData() == getOffset(nodePtr, offset):
            total += nodePtr.getData()
        nodePtr = nodePtr.getLink()

    print(total)

part1()
part2()
