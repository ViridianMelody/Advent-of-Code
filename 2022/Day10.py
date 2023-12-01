from aocd import data

class CRT:
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.signalStrengths = {}
        self.cyclesToCheck = []
        self.image = ""

    def parseInput(self, inputStr=data):
        for line in inputStr.splitlines():
            if len(line) == 4:
                self.addCycle()
            else:
                self.addX(int(line.split(" ")[1]))

    def addX(self, x):
        self.addCycle(2)
        self.x += x
    
    def addCycle(self, cycles=1):
        for i in range(cycles):
            self.drawPixel()
            self.cycle += 1
            if self.cycle in self.cyclesToCheck:
                self.calcSignalStrength()
    
    def calcSignalStrength(self):
        self.signalStrengths[self.cycle] = self.cycle*self.x
    
    def addCycleCheck(self,cycle):
        self.cyclesToCheck.append(cycle)

    def drawPixel(self):
        drawX = self.cycle%40
        if drawX == 0:
            self.image += "\n"
        if self.x-1 <= drawX <= self.x+1:
            self.image += "#"
        else:
            self.image += " "

def main():
    crt = CRT()
    cycles = [20,60,100,140,180,220]
    for cycle in cycles:
        crt.addCycleCheck(cycle)
    crt.parseInput()
    print(sum(crt.signalStrengths.values()))
    print(crt.image)

    
if __name__ == "__main__":
    main()

