from aocd import data

# Techincally this only solves part 2, but you only have to change the ranges
# in findAdjacentNodes to solve part 1.
# Djikstra's, with two nodes per location representing moving vertical or horizontal.
# Each node is adjacent to nodes in the opposite grid within the range of movement (1-3 or 4-10)

dataList = [[int(y) for y in x] for x in data.split('\n')]
height = len(dataList)
width = len(dataList[0])
directions = [(0,1),(0,-1),(1,0),(-1,0)]
nodes = {}
nodesByCoords = {}

hGrid = [[9999999999 for j in range(width)] for i in range(height)]
hGrid[0][0] = 0
vGrid = [[9999999999 for j in range(width)] for i in range(height)]
vGrid[0][0] = 0
grids = {
    "H":hGrid,
    "V":vGrid
}

def findAdjacentNodes(dir,y,x):
    result = []
    if dir == "H":
        distance = hGrid[y][x]
        rightD = distance
        leftD = distance
        for i in range(1,4):
            if x+i < width:
                rightD += dataList[y][x+i]
            if x-i >= 0:
                leftD += dataList[y][x-i]
        for i in range(4,11):
            right = x+i
            if 0 <= right < width: 
                rightD += dataList[y][right]
                if rightD < vGrid[y][right]:
                    vGrid[y][right] = rightD
                    result.append(("V",y,right))
            left = x-i
            if 0 <= left < width:
                leftD += dataList[y][left]
                if leftD < vGrid[y][left]:
                    vGrid[y][left] = leftD
                    result.append(("V",y,left))
    else:
        distance = vGrid[y][x]
        downD = distance
        upD = distance
        for i in range(1,4):
            if y+i < height:
                downD += dataList[y+i][x]
            if y-i >= 0:
                upD += dataList[y-i][x]
        for i in range(4,11):
            down = y+i
            if down < height: 
                downD += dataList[down][x]
                if downD < hGrid[down][x]:
                    hGrid[down][x] = min(hGrid[down][x],downD)
                    result.append(("H",down,x))
            up = y-i
            if up >= 0:
                upD += dataList[up][x]
                if upD < hGrid[up][x]:
                    hGrid[up][x] = min(hGrid[up][x],upD)    
                    result.append(("H",up,x))
    return result

def popMinNode(stack):
    minVal = 999999999999
    minIdx = 0
    for i,val in enumerate(stack):
        newVal = grids[val[0]][val[1]][val[2]]
        if newVal < minVal: 
            minVal = newVal
            minIdx = i
    return stack.pop(minIdx)

def traverse():
    nodeStack = [("H",0,0),("V",0,0)]
    visited = set()
    while nodeStack:
        currentNode = popMinNode(nodeStack)
        newNodes = findAdjacentNodes(*currentNode)
        for node in newNodes:
            nodeStack.append(node)
    return min(hGrid[-1][-1], vGrid[-1][-1])
        




def main():
    print(traverse())

if __name__ == "__main__":
    main()
