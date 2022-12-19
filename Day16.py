from aocd import data
import numpy as np

class Volcano:
    def __init__(self, inputStr=data):
        self.valves = []
        self.parseInput(inputStr)
        self.findDistances()

    def parseInput(self,inputStr):
        for i,line in enumerate(inputStr.splitlines()):
            name = line[6:8]
            flow = int(line[23:25].strip(";"))
            try:
                tunnels = line.split("valves ")[1].split(", ")
            except:
                tunnels = line.split("valve ")[1].split(", ")
            valve = Valve(name, flow, tunnels)
            self.valves.append(valve)
            if name == "AA":
                self.start = i

    def findDistances(self):
        matrix = np.full((len(self.valves),len(self.valves)),999)
        vCount = len(self.valves)
        for i in range(vCount):
            matrix[i,i] = 0
        for i,valve1 in enumerate(self.valves):
            for j,valve2 in enumerate(self.valves):
                if valve2.name in valve1.tunnels:
                    matrix[i,j] = 1
        for k in range(vCount):
            for i in range(vCount):
                for j in range(vCount):
                    matrix[i,j] = min(matrix[i,j],matrix[i,k] + matrix[k,j])
        self.distances = matrix
        print(matrix)
    
    def solve(self):
        return self.findMoves(self.start,[],30)

    def checkScore(self,start,end,timeLeft):
        flow = self.valves[end].flow
        time = self.distances[start,end]+1
        return flow * (timeLeft - time) 

    def findMoves(self,current,opened,timeLeft):
        scores = {}
        opened = opened.copy()
        opened.append(current)
        for i in range(len(self.valves)):
            if i not in opened:
                score = self.checkScore(current,i,timeLeft)
                if score > 0:
                    scores[i] = score
        if len(scores) == 0:
            return 0
        for i, score in scores.items():
            newTime = timeLeft - self.distances[current,i] - 1
            if newTime > 0:
                scores[i] += self.findMoves(i,opened,newTime)
        return max(scores.values())

    def solve2(self):
        human, opened = self.findMoves2(self.start,[],26)
        elephant = self.findMoves(self.start,opened,26)
        return human+elephant

    def findMoves2(self,current,opened,timeLeft):
        scores = {}
        opened = opened.copy()
        paths = {}
        opened.append(current)
        for i in range(len(self.valves)):
            if i not in opened:
                score = self.checkScore(current,i,timeLeft)
                if score > 0:
                    scores[i] = score
        if len(scores) == 0:
            return 0, opened
        for i, score in scores.items():
            newTime = timeLeft - self.distances[current,i] - 1
            if newTime > 0:
                newScore,newOpened = self.findMoves2(i,opened,newTime)
                scores[i] += newScore
                paths[i] = newOpened
        maxKey = max(scores, key=scores.get)
        return max(scores.values()),paths[maxKey]

class Valve:
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels

def main():
    volcano = Volcano()
    print(volcano.solve())
    print(volcano.solve2())

if __name__ == "__main__":
    main()