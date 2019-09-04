from node import Node

def getRegister(registers, name):
    for each in registers:
        if each.getName() == name:
            return each

def main():
    instructions = open('input.txt', 'r')
    registers = []

    for each in instructions:
        list1 = each.split()
        newNode = Node(list1[0])
        newNode.setInc(list1[1])
        registers.append(newNode)

    instructions.close()
    instructions = open('input.txt', 'r')

    i = 0
    for each in instructions:
        list1 = each.split()
        if list1[5] == '>':
            if getRegister(registers, list1[4]).getValue() > int(list1[6]):
                registers[i].setValue(int(list1[2]))
        if list1[5] == '<':
            if getRegister(registers, list1[4]).getValue() < int(list1[6]):
                registers[i].setValue(int(list1[2]))
        if list1[5] == '>=':
            if getRegister(registers, list1[4]).getValue() >= int(list1[6]):
                registers[i].setValue(int(list1[2]))
        if list1[5] == '<=':
            if getRegister(registers, list1[4]).getValue() <= int(list1[6]):
                registers[i].setValue(int(list1[2]))
        if list1[5] == '==':
            if getRegister(registers, list1[4]).getValue() == int(list1[6]):
                registers[i].setValue(int(list1[2]))
        if list1[5] == '!=':
            if getRegister(registers, list1[4]).getValue() != int(list1[6]):
                registers[i].setValue(int(list1[2]))
        i += 1

    instructions.close()

    maxVal = 0
    for register in registers:
        if register.getValue() > maxVal:
            maxVal = register.getValue()
            print(maxVal)

    # print(maxVal)

def dev():
    node1 = Node('a')
    # node1.setInc('inc')
    node1.setValue(-1)
    print(node1.getValue())

dev()
