import math
from graph import Graph

def main():
    num = int(input("Enter a number: "))
    myGraph = Graph()
    myGraph.append(1)
    i = 2
    while myGraph.getLast().getData() <= num:
        myGraph.append(i)
        i += 1
    print(myGraph.getLast().getData())

def main2():
    num = int(input("Enter a number: "))

main()
