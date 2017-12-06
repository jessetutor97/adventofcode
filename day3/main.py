import math
from graph import Graph

def main():
    num = int(input("Enter a number: "))

    graph1 = Graph()
    for i in range(1, num + 1):
        graph1.append(i)

    index = graph1.getLast().getIndex()
    layer = graph1.getLayer()
    corner = (layer * 2 + 1) ** 2
    middle = corner - layer 
    offset = middle - num
    print(offset + layer)

    graph2 = Graph()
    graph2.append(1)
    i = 2
    while graph2.getLast().getData() <= num:
        graph2.append(i)
        i += 1

    print(graph2.getLast().getData())

def main2():
    num = int(input("Enter a number: "))

main()
