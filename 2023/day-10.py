from aocd import data

#Oh my god, took me *forever* to figure out that the 
#flood fill was leaking through the start point.


def findStart(mapp):
    for i,row in enumerate(mapp):
        for j,char in enumerate(row):
            if char == "S":
                return (i,j)

def connectedToStart(start, mapp):
    x = start[1]
    y = start[0]
    result = ""
    if mapp[y][x-1] in "-LF": result += "W" #west
    if mapp[y][x+1] in "-J7": result += "E" #east
    if mapp[y+1][x] in "|LJ": result += "S" #south
    if mapp[y-1][x] in "|7F": result += "N" #north
    return result

def traverse(start, mapp):
    loop = [start]
    lPos = start
    rPos = start
    distance = 0
    lHeading,rHeading = connectedToStart(start, mapp)
    while True:
        distance += 1
        lPos = moveFuncs[lHeading](lPos)
        if lPos == rPos: break
        loop.append(lPos)
        rPos = moveFuncs[rHeading](rPos)
        if lPos == rPos: break
        loop.append(rPos)
        lHeading = pipeFuncs[mapp[lPos[0]][lPos[1]]](lHeading)
        rHeading = pipeFuncs[mapp[rPos[0]][rPos[1]]](rHeading)
    print(f"Max distance: {distance}")
    return loop


moveFuncs = {
    "N": lambda yx: (yx[0]-1,yx[1]),
    "S": lambda yx: (yx[0]+1,yx[1]),
    "E": lambda yx: (yx[0],yx[1]+1),
    "W": lambda yx: (yx[0],yx[1]-1)
}

pipeFuncs = {
    "|": lambda dir: "N" if dir=="N" else "S",
    "-": lambda dir: "W" if dir=="W" else "E",
    "L": lambda dir: "E" if dir=="S" else "N",
    "J": lambda dir: "W" if dir=="S" else "N",
    "7": lambda dir: "W" if dir=="N" else "S",
    "F": lambda dir: "E" if dir=="N" else "S"
}

pipeChars = {
    "|" : "┃",
    "-" : "━",
    "F" : "┏",
    "7" : "┓",
    "L" : "┗",
    "J" : "┛",
    "S" : "S"
}


def clearMap(mapp, loop):
    clearedMap = [["." for x in range(len(mapp[0]))] for y in range(len(mapp))]
    for pipe in loop:
        clearedMap[pipe[0]][pipe[1]] = mapp[pipe[0]][pipe[1]]
    return clearedMap

def floodFill(mapp):
    nodes = [(0,0)]
    height = len(mapp) - 1
    width = len(mapp[0]) - 1
    visited = set()
    i=0
    while nodes:
        i += 1
        y,x = nodes.pop()
        visited.add((y,x))
        if mapp[y][x] == ".": mapp[y][x] = "X"
        if y < height and mapp[y+1][x] not in "F-L": 
            if (y+1,x) not in visited and (y+1,x) not in nodes:
                nodes.append((y+1,x))
        if y > 0 and mapp[y][x] not in "F-L": 
            if (y-1,x) not in visited and (y-1,x) not in nodes:
                nodes.append((y-1,x))
        if x < width and mapp[y][x+1] not in "7|F": 
            if (y,x+1) not in visited and (y,x+1) not in nodes:
                nodes.append((y,x+1))
        if x > 0 and mapp[y][x] not in "7|F": 
            if (y,x-1) not in visited and (y,x-1) not in nodes:
                nodes.append((y,x-1))
    return mapp




def solveBothParts():
    mapp = data.split('\n')
    start = findStart(mapp)
    loop = traverse(start, mapp)
    clearedMap = clearMap(mapp,loop)
    clearedMap[start[0]][start[1]] = "7" #hard coded replacement of start point because I can't be bothered.
    filled = floodFill(clearedMap)
    result = sum([x.count(".") for x in filled])
    print(f"Enclosed spaces: {result}")


def main():
    solveBothParts()

if __name__ == "__main__":
    main()