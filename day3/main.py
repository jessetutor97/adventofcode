import math
from graph import Graph

def main():
    num = int(input("Enter a number: "))

    layer = math.ceil(math.sqrt(num)) // 2
    corner = (layer * 2 + 1) ** 2
    middle = corner - layer 
    offset = middle - num 
    print(offset + layer)

    myGraph = Graph()
    myGraph.append(1)
    i = 2
    while myGraph.getLast().getData() <= num:
        myGraph.append(i)
        i += 1

    print(myGraph.getLast().getData())

main()
