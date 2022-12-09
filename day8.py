from aocd import data
from functools import reduce

class Trees:
    def __init__(self):
        self.visibleTrees = set()
        self.grid = self.generateGrid(data)

    def generateGrid(self, inputStr):
        return [[int(x) for x in row] for row in inputStr.splitlines()]
    
    def findTallestBothSides(self,trees,maxHeight=9):
        result = self.findTallest(trees,maxHeight)
        right = self.findTallest(trees[::-1],maxHeight)
        offset = len(trees)-1
        for i in right:
            result.add(offset-i)
        return result

    def findTallest(self, trees, maxHeight=9):
        result = set()
        tallest = -1
        for i,tree in enumerate(trees):
            if tree > tallest:
                tallest = tree
                result.add(i)
            if tallest == maxHeight:
                break
        return result

    def checkAllTrees(self):
        for y,row in enumerate(self.grid):
            for tree in self.findTallestBothSides(row):
                self.visibleTrees.add((tree,y))
        rotatedGrid = zip(*self.grid)
        for x,col in enumerate(rotatedGrid):
            for tree in self.findTallestBothSides(col):
                self.visibleTrees.add((x,tree))

    def oneSideScore(self, trees):
        maxHeight = trees.pop(0)
        result = 0
        for tree in trees:
            result += 1
            if tree >= maxHeight:
                break
        return result



    def getScore(self,x,y):
        column = [row[x] for row in self.grid]
        sides = [
            self.grid[y][x::-1],
            self.grid[y][x:],
            column[y::-1],
            column[y:]
        ]
        result = 1
        
        for trees in sides:
            result *= self.oneSideScore(trees)
        return result

    def findHighestScore(self):
        scores = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                scores.append(self.getScore(x,y))
        return max(scores)

                




def main():
    trees = Trees()
    trees.checkAllTrees()
    print(len(trees.visibleTrees))
    print(trees.findHighestScore())
    lyst = list(range(20))
    print(lyst[5::-1])


if __name__ == "__main__":
    main()