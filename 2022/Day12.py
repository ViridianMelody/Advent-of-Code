from aocd import data

class Djikstra:
    def __init__(self):
        self.grid = data.splitlines()
        self.visited = set()
        self.nodes = {}
        self.createNodes()
        self.queue = []

    def createNodes(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                elevation = self.getElevation(i,j)
                newNode = Node(elevation)
                self.nodes[(i,j)] = newNode
                if self.grid[i][j] == "S":
                    self.current = (i,j)
                    newNode.distance = 0
                elif self.grid[i][j] == "E":
                    self.end = (i,j)
    
    def checkAdjacent(self, reverse=False):
        i = self.current[0]
        j = self.current[1]
        node = self.nodes[(i,j)]
        elevation = node.elevation
        self.visited.add((i,j))
        adjacent = []
        if i > 0:
            adjacent.append((i-1,j))
        if i < len(self.grid)-1:
            adjacent.append((i+1,j))
        if j > 0:
            adjacent.append((i,j-1))
        if j < len(self.grid[i])-1:
            adjacent.append((i,j+1))
        for cell in adjacent:
            newNode = self.nodes[cell]
            if cell in self.visited:
                continue
            if (reverse and elevation-1 <= newNode.elevation) or (not reverse and elevation + 1 >= newNode.elevation):
                newNode.distance = min(newNode.distance, node.distance+1)
                if cell not in self.queue:
                    self.queue.append(cell)
        
    def findPath(self):
        while self.end not in self.visited:
            self.checkAdjacent()
            self.current = self.queue.pop(0)
        return self.nodes[self.end].distance

    def findAPath(self):
        self.queue = [self.end]
        self.nodes[self.end].distance = 0
        while self.grid[self.current[0]][self.current[1]] != "a":
            self.current = self.queue.pop(0)
            self.checkAdjacent(True)
        
        return self.nodes[self.current].distance
        


                

    def getElevation(self,i,j):
        base = ord("a")
        elevation = ord(self.grid[i][j])-base
        if self.grid[i][j] == "S":
            elevation = 0
            self.start = (i,j)
        elif self.grid[i][j] == "E":
            elevation = 25
            self.end = (i,j)
        return elevation
                    
class Node:
    def __init__(self,elevation):
        self.distance = 1000000000
        
        self.elevation = elevation





def main():
    dji = Djikstra()
    print(dji.findPath())
    dji2 = Djikstra()
    print(dji2.findAPath())

if __name__ == "__main__":
    main()