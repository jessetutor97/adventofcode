import random

# Returns a word that is sorted alphabetically from A-Z
def sort(word):
    list1 = []
    for letter in word:
        list1.append(letter)

    index1 = 0
    for i in range(len(word) - 1, 0, -1):
        index2 = index1 + 1
        for j in range(i):
            if list1[index1] > list1[index2]:
                temp = list1[index1]
                list1[index1] = list1[index2]
                list1[index2] = temp
            index2 += 1
        index1 += 1

    newWord = ''
    for letter in list1:
        newWord += letter

    return newWord

def part1():
    myFile = open('input.txt', 'r')

    duplicates = 0
    numLines = 0
    for line in myFile:
        numLines += 1
        found = False
        wordList = line.split()

        index1 = 0
        for i in range(len(wordList) - 1, 0, -1):
            index2 = index1 + 1
            for j in range(i):
                if wordList[index1] == wordList[index2]:
                    duplicates += 1
                    found = True
                    break
                index2 += 1
            if found:
                break
            index1 += 1

    myFile.close()
    print(numLines - duplicates)

def part2():
    myFile = open('input.txt', 'r')

    duplicates = 0
    numLines = 0
    value = 0
    for line in myFile:
        numLines += 1
        found = False
        wordList = line.split()

        index1 = 0
        for i in range(len(wordList) - 1, 0, -1):
            index2 = index1 + 1
            for j in range(i):
                if sort(wordList[index1]) == sort(wordList[index2]):
                    duplicates += 1
                    found = True
                    break
                index2 += 1
            if found:
                break
            index1 += 1

    myFile.close()
    print(numLines - duplicates)

part1()
part2()
