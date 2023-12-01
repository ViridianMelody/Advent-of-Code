from aocd import data
import matplotlib.pyplot as plt
import numpy as np

class SandCave:
    def __init__(self, inputStr=data):
        self.grid = np.zeros((600,20))
        self.sandStart = (500,0)
        self.maxY = 0
        self.parseInput(inputStr)
    
    def parseInput(self, inputStr):
        lines = inputStr.splitlines()
        for line in inputStr.splitlines():
            rockPath = [list(map(int, x.split(","))) for x in line.split(" -> ")]
            self.addRock(rockPath)

    def addRock(self, path):
        currentPoint = path.pop(0)
        while path:
            nextPoint = path.pop(0)
            x1 = currentPoint[0]
            x2 = nextPoint[0]
            if x2 < x1:
                x1,x2 = x2,x1
            y1 = currentPoint[1]
            y2 = nextPoint[1]
            if y2 < y1:
                y1,y2 = y2,y1
            self.pad(max(x1,x2),max(y1,y2))
            x2 += 1
            y2 += 1
            
            self.grid[x1:x2,y1:y2] = 2
            currentPoint = nextPoint

        

    def pad(self, x, y):
        if y > self.maxY:
            self.maxY = y
        xLen, yLen = np.shape(self.grid)
        xPad = max(x-xLen+5, 0)
        yPad = max(y-yLen+5, 0)
        if xPad or yPad:
            self.grid = np.pad(self.grid, ((0,xPad),(0,yPad)))

    def fillSand(self):
        grains = 0
        grainsDropped = 1
        step = 0
        while grainsDropped > 0:
            grainsDropped = self.dropGrain()
            grains += grainsDropped
            step += 1
        return grains

    def dropGrain(self):
        gX = self.sandStart[0]
        gY = self.sandStart[1]
        grains = 0
        left = False
        right = False
        while gY < self.maxY:
            self.pad(gX, 0)
            if self.grid[gX, gY+1] == 0:
                left = False
                right = False
                grains = 1
                gY += 1
            elif self.grid[gX-1, gY+1] == 0:
                left = True
                grains += 1
                if right:
                    right = False
                    grains = 1
                gX -= 1
                gY += 1
            elif self.grid[gX+1, gY+1] == 0:
                right = True
                grains += 1
                if left:
                    left = False
                    grains = 1
                gX += 1
                gY += 1
            elif gY == 0:
                return 0
            else:
                result = 1
                self.grid[gX,gY] = 1
                if left: x = 1
                else: x = -1
                for pt in range(2,grains):
                    gX += x
                    gY -= 1
                    if left and self.grid[gX+1,gY+1] == 0: break
                    self.grid[gX,gY] = 1
                    result += 1
                return result
        return 0

    def setFloor(self):
        self.grid = np.pad(self.grid, ((0,400),(0,0)))
        self.grid[:,self.maxY+2] = 2
        self.maxY += 5

    def display(self):
        grid = np.transpose(self.grid)
        plt.imshow(grid,cmap="viridis",interpolation="nearest")
        plt.show()







def main():
    sandcave = SandCave()
    print(sandcave.fillSand())
    sandcave.display()
    sandcave2 = SandCave()
    sandcave2.setFloor()
    print(sandcave2.fillSand()+1)
    sandcave2.display()



if __name__ == "__main__":
    main()