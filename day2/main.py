from linkedlist import LinkedList

def main():
    spreadsheet = open('input.txt', 'r')
    checksum = 0
    for line in spreadsheet:
        numList = line.split()
        highNum = int(numList[0])
        lowNum = int(numList[0])
        for num in numList:
            if int(num) > highNum:
                highNum = int(num)
            if int(num) < lowNum:
                lowNum = int(num)
        difference = highNum - lowNum
        checksum += difference
    spreadsheet.close()

    print(checksum)

    spreadsheet = open('input.txt', 'r')
    linkedList = LinkedList()
    total = 0
    for line in spreadsheet:
        numList = line.split()
        for num in numList:
            linkedList.append(int(num))
        nodePtr1 = linkedList.getFront()
        for i in range(linkedList.getSize()):
            num = nodePtr1.getData()
            nodePtr2 = nodePtr1.getLink()
            for j in range(linkedList.getSize() - 1):
                if nodePtr1.getData() % nodePtr2.getData() == 0:
                    total += nodePtr1.getData() // nodePtr2.getData()
                nodePtr2 = nodePtr2.getLink()
            nodePtr1 = nodePtr1.getLink()
        linkedList.clear()
    spreadsheet.close()

    print(total)

main()

