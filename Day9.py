from aocd import data

class ropeSteps:
    offsets = {
        "U":(0,1),
        "D":(0,-1),
        "L":(-1,0),
        "R":(1,0)
    }
    def __init__(self, knots=2):
        self.knots = [[0,0] for x in range(knots)]
        self.tailVisited = set()
        self.tailVisited.add((0,0))

    def parseAllSteps(self):
        for step in data.splitlines():
            self.parseStep(step)

    def parseStep(self,step):
        step = step.split(" ")
        offset = self.offsets[step[0]]
        
        for i in range(int(step[1])):
            self.knots[0][0] += offset[0]
            self.knots[0][1] += offset[1]
            self.moveAllTails()
            self.tailVisited.add(tuple(self.knots[-1]))
    
    def moveAllTails(self):
        i = 1
        while i < len(self.knots):
            self.knots[i] = self.moveTail(self.knots[i-1],self.knots[i])
            i += 1
    
    def moveTail(self, head, tail):
        headX = head[0]
        headY = head[1]
        tailX = tail[0]
        tailY = tail[1]
        dx = headX - tailX
        dy = headY - tailY
        xOffset = 0
        yOffset = 0
        if   dx >=  2: xOffset = 1
        elif dx <= -2: xOffset = -1
        if   dy >=  2: yOffset = 1
        elif dy <= -2: yOffset = -1
        if   dx == 1 and yOffset != 0: xOffset = 1
        elif dy == 1 and xOffset != 0: yOffset = 1
        elif dx == -1 and yOffset != 0: xOffset = -1
        elif dy == -1 and xOffset != 0: yOffset = -1
        tailX += xOffset
        tailY += yOffset
        return [tailX,tailY]

    def countVisited(self):
        return len(self.tailVisited)


def main():
    rope = ropeSteps(10)
    rope.parseAllSteps()
    print(rope.countVisited())
    

if __name__ == "__main__":
    main()