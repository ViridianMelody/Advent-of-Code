from aocd import data
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# I vaguely know how to do part two, but I've spent too much time for now.


trench = [(0,0,0)]
lastPoint = (0,0,"#000000")
directions = {
    "U": (0,1),
    "D": (0,-1),
    "L": (-1,0),
    "R": (1,0)
}


def doStep(line, lastPoint):
    direction, length, color = line.split(" ")
    dirOffset = directions[direction]
    length = int(length)
    color = color[1:8]
    lastPoint = (lastPoint[0]+dirOffset[0]*length, lastPoint[1]+dirOffset[1]*length,color)
    trench.append(lastPoint)
    return lastPoint

def fillTrench(trench):
    result = 1
    dX = 1-min([x[0] for x in trench])
    dY = 1-min([x[1] for x in trench])
    minX = min([x[0] for x in trench])
    maxX = max([x[0] for x in trench])
    minY = min([x[1] for x in trench])
    maxY = max([x[1] for x in trench])
    #colors = [x[2] for x in trench]
    trench = [(x[0]+dX,x[1]+dY) for x in trench]
    x1 = dX
    y1 = dY
    matrix = np.zeros((maxX-minX+10,maxY-minY+10),dtype=np.int8)
    for x2,y2 in trench[1:]:
        matrix[min(x1,x2):max(x1,x2)+1,min(y1,y2):max(y1,y2)+1] = 2
        x1,y1 = x2,y2
    for i,row in enumerate(matrix):
        inside = False
        up = False
        down = False
        for j,space in enumerate(row):
            if space:
                if matrix[i-1][j] == 2: up = not up
                if matrix[i+1][j] == 2: down = not down
            else:
                if up and down:
                    inside = not inside
                up = False
                down = False
                if inside:
                    matrix[i][j] = 1

    plt.matshow(matrix)
    print(np.count_nonzero(matrix))
            

    
    


def makeBigTrench(inputStr = data):
    x = 0
    y = 0
    trench = [(0,0)]
    directions = [(1,0),(0,-1),(-1,0),(0,1)]
    for row in inputStr.split("\n"):
        instruction = row.split(" ")[2][2:8]
        print(instruction)
        mag = int(instruction[:5],base=16)
        direction = directions[int(instruction[5])]
        x += direction[0]*mag
        y += direction[1]*mag
        trench.append((x,y,"0"))
    return trench


    

def drawTrench(trench):
    fig, ax = plt.subplots()
    start = trench[0]
    segments = []
    for end in trench[1:]:
        segment = mpl.lines.Line2D((start[0],end[0]), (start[1],end[1]), color=end[2])
        ax.add_line(segment)
        start = end
    minX = min([x[0] for x in trench])
    maxX = max([x[0] for x in trench])
    minY = min([x[1] for x in trench])
    maxY = max([x[1] for x in trench])
    print(f"minX: {minX}, minY:{minY}, maxX:{maxX}, maxY:{maxY}")
    ax.set_xlim(minX, maxX)
    ax.set_ylim(minY, maxY)
    ax.set_aspect("equal", adjustable="box")
    plt.show()

    


def main():
    lastPoint = (0,0,"#000000")
    for line in data.split('\n'):
        lastPoint = doStep(line,lastPoint)
    fillTrench(trench)
    drawTrench(trench)
    bigTrench = makeBigTrench()
    drawTrench(bigTrench)

if __name__ == "__main__": 
    main()
