from aocd import data

class Beacons:
    def __init__(self, inStr=data):
        self.sensors = []
        self.beacons = []
        self.parseInput(inStr)
        self.getAllDistances()

    def parseInput(self, inStr):
        for line in inStr.splitlines():
            line = line.split(": ")
            sensor = [int(x) for x in line[0][12:].split(", y=")]
            self.sensors.append(sensor)
            beacon = [int(x) for x in line[1][23:].split(", y=")]
            self.beacons.append(beacon)

    def beaconDistance(self, i):
        beacon = self.beacons[i]
        sensor = self.sensors[i]
        return abs(beacon[0]-sensor[0])+abs(beacon[1]-sensor[1])

    def getAllDistances(self):
        self.distances = []
        for i in range(len(self.sensors)):
            self.distances.append(self.beaconDistance(i))

    def blockedRange(self, y, i):
        sensor = self.sensors[i]
        distance = self.distances[i]
        rowDistance = abs(sensor[1] - y)
        width = distance-rowDistance
        if width < 0:
            return False
        left = sensor[0]-width
        right = sensor[0]+width
        return left,right
    
    def allRowBlocks(self, y):
        blocks = []
        for i in range(len(self.beacons)):
            blocked = self.blockedRange(y,i)
            if blocked:
                blocks.append(blocked)
        blocks.sort(key=lambda x: x[0])
        i = 0
        newBlocks = []
        block = blocks.pop(0)
        while blocks:
            nextBlock = blocks.pop(0)
            if nextBlock[1] >= block[1] >= nextBlock[0]:
                block = (block[0], nextBlock[1])
            elif block[1] < nextBlock[0]:
                newBlocks.append(block)
                block = nextBlock
        newBlocks.append(block)
        return newBlocks



def main():
    bs = Beacons()
    for i in range(4000001):
        blocks = bs.allRowBlocks(i)
        if len(blocks) > 1:
            print(i)
            print(blocks)
            result = i + (4000000 * (blocks[0][1]+1))
            print(result)
        elif blocks[-1][1]<=4000000:
            print(blocks)
        elif blocks[0][0]>0:
            print(blocks)


if __name__ == "__main__":
    main()