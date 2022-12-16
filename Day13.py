from aocd import data
from ast import literal_eval

class packetChecker:
    def __init__(self, inputStr=data):
        self.allPackets = []
        self.packetPairs = []
        self.parseInput(inputStr)

    def parseInput(self, inputStr):
        packetPairStrs = inputStr.split("\n\n")
        for pairStr in packetPairStrs:
            newPair = [Packet(x) for x in pairStr.split("\n")]
            self.addPair(newPair)
    
    def countCorrectPairs(self):
        result = 0
        for i,pair in enumerate(self.packetPairs):
            if pair[0] < pair[1]:
                result += i + 1
        return result
    
    def addPair(self, pair):
        for packet in pair:
            self.addPacket(packet)
        self.packetPairs.append(pair)


    def addPacket(self, packet):
        self.allPackets.append(packet)

    def findPacketIndex(self, term):
        self.allPackets.sort()
        return self.allPackets.index(term)


class Packet:
    def __init__(self, packetStr):
        self.data = literal_eval(packetStr)
    
    def __lt__(self, right):
        left = self.data
        result = self.compareLists(left, right.data)
        return result == 1

    def __eq__(self, other):
        return self.data == other

    def __repr__(self):
        return str(self.data)

    def get(self, i=-1):
        return self.data[i]

    def compareLists(self, left, right):
        i = 0
        while i < len(left) and i < len(right):
            nextLeft = left[i]
            nextRight = right[i]
            pendingResult = self.compareItems(nextLeft, nextRight)
            if pendingResult == 1:
                return 1
            if pendingResult == -1:
                return -1
            i += 1
        if i < len(left):
            return -1
        if i < len(right):
            return 1
        return 0

    def compareItems(self, left, right):
        if left == None:
            return 1
        if right == None:
            return -1
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            elif left > right:
                return -1
            else:
                return 0
        if isinstance(left, int):
            left = [left]
        elif isinstance(right, int):
            right = [right]
        return self.compareLists(left,right)

            

def main():
    checker = packetChecker()
    print(f"Part 1: {checker.countCorrectPairs()}")
    packet2 = Packet("[[2]]")
    packet6 = Packet("[[6]]")
    checker.addPacket(packet2)
    checker.addPacket(packet6)
    packet2Index = checker.findPacketIndex(packet2)+1
    packet6Index = checker.findPacketIndex(packet6)+1
    print(f"Part 2: {packet2Index*packet6Index}")

if __name__ == "__main__":
    main()