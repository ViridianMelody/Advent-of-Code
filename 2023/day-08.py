from aocd import data
from math import lcm

# Had a surprisingly hard time confirming that there was a loop for each start point.

def parseData(inputStr=data):
    result = {}
    directions,nodes = data.split('\n\n')
    nodes = nodes.split('\n')
    for node in nodes:
        key = node[0:3]
        left = node[7:10]
        right = node[12:15]
        result[key] = (left,right)
    return directions, result
        
def followDirections(start, target, directions, nodes):
    current = start
    stepsTaken = 0
    while True:
        for step in directions:
            if step == "R":
                current = nodes[current][1]
            else:
                current = nodes[current][0]
            stepsTaken += 1
            if current == target:
                return stepsTaken

def followMultipleDirections(starts,target,directions,nodes):
    current = starts
    stepsTaken = 0
    while True:
        for step in directions:
            if step == "R": j = 1
            else: j = 0
            current = [nodes[x][j] for x in current]
            stepsTaken += 1
            if all(map(lambda x: x[2]==target, current)):
                return stepsTaken

def findDistances(start, target, directions, nodes):
    current = start
    stepsTaken = 0
    result = []
    while stepsTaken <100000000000:
        for step in directions:
            if step == "R":
                current = nodes[current][1]
            else:
                current = nodes[current][0]
            stepsTaken += 1
            if current[2] == target:
                result.append(stepsTaken)
        if current == start:
            print("loop")
            return result
    return result
    
def mapNode(start,directions,nodes):
    current = start
    result = []
    for i,step in enumerate(directions):
        if step == "R":
            current = nodes[current][1]
        else:
            current = nodes[current][0]
        if current[2] == "Z":
            result.append(i)
    return current,result

def solvePartTwo(directions, nodes):
    allStarts = [x for x in nodes.keys() if x[2]=="A"]
    loopLengths = []
    for start in allStarts:
        current = start
        i = 1
        visited = []
        visited.append(current)
        newMap = mapNode(current,directions,nodes)
        current = newMap[0]
        while current not in visited:
            visited.append(current)
            newMap = mapNode(current,directions,nodes)
            current = newMap[0]
            i+= 1
        print(visited)
        loopLengths.append(len(visited)-1)
    print(loopLengths)
    print(lcm(*loopLengths)*len(directions))



def main():
    directions, nodes = parseData()
    start = "AAA"
    target = "ZZZ"
    print(followDirections(start,target,directions,nodes))
    solvePartTwo(directions, nodes)




if __name__ == "__main__":
    main()