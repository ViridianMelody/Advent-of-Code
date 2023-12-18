from aocd import data

# Really expected part two to make normal traversal 
# infeasible, but nope, same algorithm worked fine.

directory = {
    "-": {
        "N":"EW",
        "S":"EW",
        "E":"E",
        "W":"W"
        },
    "|": {
        "N":"N",
        "S":"S",
        "E":"NS",
        "W":"NS"
        },
    "/": {
        "N":"E",
        "S":"W",
        "E":"N",
        "W":"S"                
    },
    "\\": {
        "N":"W",
        "S":"E",
        "E":"S",
        "W":"N"                
    },
    ".": {
        "N":"N",
        "S":"S",
        "E":"E",
        "W":"W"                
    }
}
offsets = {
    "N": (-1,0),
    "S": (1,0),
    "E": (0,1),
    "W": (0,-1)
}

class Beam:
    def __init__(self,y=0,x=0,heading="E"):
        self.y = y
        self.x = x
        self.heading = heading

    def step(self, mapp):
        beams = []
        point = mapp[self.y][self.x]
        newDir = directory[point][self.heading]
        if len(newDir) == 2: 
            splitNode = self.split(newDir[1],mapp)
            if splitNode:
                beams.append(splitNode)
        self.heading = newDir[0]
        self.y += offsets[self.heading][0]
        self.x += offsets[self.heading][1]
        if 0 <= self.y < len(mapp) and 0 <= self.x < len(mapp[self.y]):
            beams.append(self)
        return beams
        
    def split(self, newDir, mapp):
        newY = self.y + offsets[newDir][0]
        newX = self.x + offsets[newDir][1]
        if 0 <= newY < len(mapp) and 0 <= newX < len(mapp[newY]):
            return Beam(newY, newX, newDir)
        return False

    def getCoords(self):
        return (self.y,self.x)

    def getHead(self):
        return (self.y,self.x,self.heading)


def traverse(mapp,start=(0,0,"E")):
    #display = [list(x) for x in mapp[:]]
    #display[0][0] = "#"
    path = set(start)
    energized = set((start[0],start[1]))
    beamStack = [Beam(*start)]
    while beamStack:
        newBeams = beamStack.pop().step(mapp)
        for beam in newBeams:
            beamSnap = beam.getHead()
            if beamSnap not in path:
                path.add(beamSnap)
                beamStack.append(beam)
            beamCoords = beam.getCoords()
            if beamCoords not in energized:
                energized.add(beamCoords)
                #if display[beamCoords[0]][beamCoords[1]] == ".":
                #    display[beamCoords[0]][beamCoords[1]] = "#"
                #for row in display:
                #    print("".join(row))
                #input()
    return energized

def solvePart1(inputStr=data):
    mapp = inputStr.split("\n")
    energized = traverse(mapp)
    print(len(energized))

def solvePart2(inputStr=data):
    mapp = inputStr.split("\n")
    entryPoints = [(y,0,"E") for y in range(len(mapp))]
    entryPoints += [(y,len(mapp[y])-1,"W") for y in range(len(mapp))]
    entryPoints += [(0,x,"S") for x in range(len(mapp[0]))]
    entryPoints += [(len(mapp)-1,x,"N") for x in range(len(mapp[0]))]
    print(max(map(lambda x: len(traverse(mapp,x)), entryPoints)))

def main():
    solvePart1()
    solvePart2()

if __name__ == "__main__":
    main()